from django.urls import path
from .views import index, BookListView, BookDetailView, AuthorListView, AuthorDetailView

urlpatterns = [
    path('', index, name="index"),
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('author/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

]
