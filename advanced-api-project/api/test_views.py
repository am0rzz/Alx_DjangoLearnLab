from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")

        # Create an author
        self.author = Author.objects.create(name="George Orwell")

        # Create a sample book
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

        # Endpoints
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book.id])
        self.delete_url = reverse('book-delete', args=[self.book.id])


    def test_list_books(self):
        """Test getting the list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_book(self):
        """Test getting a single book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "1984")

    def test_create_book_authenticated(self):
        """Test creating a book with authentication"""
        self.client.login(username="testuser", password="testpass123")
        data = {
            "title": "Haerry Potter",
            "publication_year": 1999,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """Test creating a book without authentication"""
        data = {
            "title": "Harry Potter",
            "publication_year": 1919,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """Test updating a book"""
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "Nineteen", "publication_year": 1949, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Nineteen Eighty-Four")

    def test_delete_book(self):
        """Test deleting a book"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)


    def test_filter_books_by_title(self):
        """Test filtering books by title"""
        response = self.client.get(f"{self.list_url}?title=1984")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        """Test searching books by partial title"""
        response = self.client.get(f"{self.list_url}?search=198")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_year(self):
        """Test ordering books by publication year"""
        Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author)
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "1984")