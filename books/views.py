from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import booksForm
from .models import books

def index(request):
    allbooks = books.objects.all() 
    return render(request,"books/index.html",{
        "books": allbooks
    })

def create(request):
    form = booksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    
    return render(request,"books/create.html", {
        "form": form
    })

def edit(request,id):
    book = books.objects.get(pk=id)
    form = booksForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("index")
    
    return render(request,"books/edit.html", {
        "form": form,
        "book": book
    })

def delete(request,id):
    book = books.objects.get(pk=id)
    book.delete()
    return redirect("index")

def show(request,id):
    book = books.objects.get(pk=id)
    return render(request,"books/show.html",{
        "book": book
    })
    