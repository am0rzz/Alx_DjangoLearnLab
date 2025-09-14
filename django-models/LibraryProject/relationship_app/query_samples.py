from . import models
author_name = 'amr'
filtered_books = models.Book.objects.filter(author__name = author_name)

for book in filtered_books:
    print(book)


library_name = 'amr library'
library = models.Library.objects.get(name = library_name)
library_books = library.books.all()

for book in library_books:
    print(book)


librarians = models.Librarian.objects.filter(library__name = library_name)

for librarian in librarians:
    print(librarian)