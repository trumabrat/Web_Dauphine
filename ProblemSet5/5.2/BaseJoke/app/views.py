from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Quote
from .models import Person
from django import forms

# Form for entering a joke
class JokeForm(forms.Form):
    joke = forms.CharField(label='Quote', max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.ModelChoiceField(queryset=Person.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

# index page displaying all entries
def index(request):
    highlight = request.GET.get('highlight')
    try:
        highlight = int(highlight)
    except: 
        highlight = None
    # get all quotes from quote model
    quotes = Quote.objects.all()
    return render(request, 'app/index.html', {
        'jokes': quotes,
        'highlight': highlight
    })

# page for adding new entries
def add(request):
    global id

    if request.method == 'POST':
        form = JokeForm(request.POST)
        if form.is_valid():
            # id is len(quotes) + 1
            id = len(Quote.objects.all()) + 1
            # add new entry to quotes model, and set id to our id
            quote = Quote(text=form.cleaned_data['joke'], author=form.cleaned_data['author'])
            quote.id = id
            quote.save()
            
            # add GET request parameter to highlight correct joke
            response = redirect('app:index')
            response['Location'] += f'?highlight={id}'
            return response
    else:
        form = JokeForm()

    return render(request, 'app/add.html', { 'form': form })

# get JSON version of an entry
def get_user_entry(request, id):
    # get entry from quotes model
    entry = Quote.objects.get(id=id)
    if entry is None:
        return JsonResponse({'error': 'Entry does not exist'}, status=404)
    else:
        #return entry as an JSON object
        return JsonResponse({"text": entry.text, "author": entry.author.name})