from django.shortcuts import render, redirect
from .models import Book

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        if title and author:
            Book.objects.create(title=title, author=author)
        return redirect('home')

    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})
