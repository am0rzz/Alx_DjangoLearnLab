# Import the model

from bookself.models import Book

# Command

Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

-- OR --

book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Output ==> FROM CODE 1

<Book: Book object (1)>
