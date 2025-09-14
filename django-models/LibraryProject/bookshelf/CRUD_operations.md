# Create

Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Retrieve

Book.objects.all()

# Update

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Delete

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
book.save()
