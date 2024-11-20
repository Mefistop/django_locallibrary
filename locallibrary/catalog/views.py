import datetime
from sunau import Au_read

from django.contrib.admin.models import DELETION
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models.sql import UpdateQuery
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Book, BookInstance, Author
from .forms import RenewBookForm


def index(request):
    """
    View function for the home page of the website.
    """
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available': num_instances_available,
        'num_authors':num_authors,
        'num_visits':num_visits,
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
    paginate_by = 10


class AuthorDetailView(DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    model = BookInstance
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status='o').order_by('due_back')



class LoanedBooksAllListView(PermissionRequiredMixin, ListView):
    """
    Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission.
    """
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/bookinstance_list_borrowed_all.html'
    model = BookInstance
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status='o').order_by('due_back')

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    book_inst = get_object_or_404(BookInstance, pk=pk)
    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        if form.is_valid():
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()
            return HttpResponseRedirect(reverse_lazy('all-borrowed'))
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})
    return render(request, 'catalog/book_renew_librarian.html', {'form':form, 'bookinst': book_inst})


class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '12/10/2024'}
    permission_required = 'catalog.add_author'


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth','date_of_death']


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')


class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')

