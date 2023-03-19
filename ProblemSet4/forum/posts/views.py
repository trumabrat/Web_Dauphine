from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'home.html')

def add(request):
    if request.method == 'POST':
        author = request.POST['author']
        body = request.POST['body']
        post = Post(author=author, body=body)
        post.save()
        return redirect("/")
    
    return render(request, 'add.html')

def get_entry(request,post_id):
    return HttpResponse(f"Hello, world. You're at the posts get_entry. Post id is {post_id}.")