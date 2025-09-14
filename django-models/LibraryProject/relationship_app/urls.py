from django.urls import path
from .views import list_books
from .views import LibraryDetailView
urlpatterns = [
    path('', list_books, name='books'),
    path('library/',LibraryDetailView.as_view(),name='library-detail')
]