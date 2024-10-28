from django.shortcuts import render
from .models import Book, BookInstance, Author


def index(request):
    """
    View function for the home page of the website.
    """
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available': num_instances_available,
        'num_authors':num_authors,
    }
    return render(request, 'index.html', context=context)


# Create your views here.
