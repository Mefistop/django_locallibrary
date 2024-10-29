from django.shortcuts import render
from django.views.generic import ListView, DetailView

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


class BookListView(ListView):
    model = Book
    paginate_by = 10


class BookDetailView(DetailView):
    model = Book
    queryset = Book.objects.select_related('author').prefetch_related('bookinstance_set').all()
    paginate_by = 10


class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author



# Create your views here.
