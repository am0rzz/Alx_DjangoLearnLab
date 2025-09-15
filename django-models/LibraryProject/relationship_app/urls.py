from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/',views.LibraryDetailView.as_view(),name='libray_detail'),
    path('register/', views.SignUpView.as_view(),name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('ad/',views.admin_view,name='admin'),
    path('mb/',views.member_view,name='member'),
    path('li/',views.librarian_view,name='librarian'),
    path('add_book/',views.can_add_book,name='add'),
    path('edit_book/',views.can_edit_book,name='edit'),
    path('delete_book/',views.can_delete_book,name='delete')
]
