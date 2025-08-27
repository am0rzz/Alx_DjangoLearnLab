# Import the model

from bookself.models import Book

# Command

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
book.save()
Book.objects.all()

# Output

(1, {'bookshelf.Book': 1})
<QuerySet []>
