from .models import Book,Author,Librarian,Library
from django.shortcuts import get_object_or_404

def list_all_books(request,author_name):
    author = Author.objects.get(name = author_name)
    books = Book.objects.filter(author = author)
    return books

def books_in_library(request,library_name):
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    return books_in_library

def get_librarian(request,library_name):
    library = Library.objects.get(name=library_name)
    librarians = library.librarian
    return librarians
