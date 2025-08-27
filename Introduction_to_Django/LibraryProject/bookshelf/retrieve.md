# Import the model

from bookself.models import Book

# Command

Book.objects.get(title="1984")

# Output

<Book: Book object (1)>
