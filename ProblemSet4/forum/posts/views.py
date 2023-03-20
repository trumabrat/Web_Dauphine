from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post


def index(request):
    posts = Post.objects.all()
    posts = posts.order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})


def add(request):
    if request.method == 'POST':
        author = request.POST['author']
        author = author[0].upper() + author[1:]

        body = request.POST['content']

        if (len(author) > 20 or len(body) < 10 or len(body) > 120):
            return HttpResponse("Invalid entry. Author's name can't be more than 20 characters. The post must contain between 10 and 120 characters")
        post = Post(author=author, body=body)
        post.save()
        return redirect("/")

    return render(request, 'add.html')


def get_entry(request, post_id):
    post = Post.objects.get(id=post_id)
    return HttpResponse(post)
