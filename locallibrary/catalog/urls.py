from django.urls import path
from .views import (index,
                    BookListView,
                    BookDetailView,
                    AuthorListView,
                    AuthorDetailView,
                    LoanedBooksByUserListView,
                    LoanedBooksAllListView,
                    renew_book_librarian)

urlpatterns = [
    path('', index, name="index"),
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('author/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', LoanedBooksAllListView.as_view(), name='all-borrowed'),
    path('book/<uuid:pk>/renew/', renew_book_librarian,name='renew-book-librarian')

]
