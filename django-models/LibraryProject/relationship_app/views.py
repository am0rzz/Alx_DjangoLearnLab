from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test, permission_required

# Custom permission function
from .models import UserProfile

def is_admin(user):
    if not user.is_authenticated:
        return False
    try:
        profile = UserProfile.objects.get(user=user)
        return profile.role == 'Admin'
    except UserProfile.DoesNotExist:
        return False

def is_librarian(user):
    if not user.is_authenticated:
        return False
    try:
        profile = UserProfile.objects.get(user=user)
        return profile.role == 'Librarian'
    except UserProfile.DoesNotExist:
        return False

def is_member(user):
    if not user.is_authenticated:
        return False
    try:
        profile = UserProfile.objects.get(user=user)
        return profile.role == 'Member'
    except UserProfile.DoesNotExist:
        return False

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Library, Book

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponse

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

@user_passes_test(is_admin, login_url='ad/')
def admin_view(request):
    return HttpResponse("You are an admin")

@user_passes_test(is_librarian, login_url='li/')
def librarian_view(request):
    return HttpResponse("You are a librarian")

@user_passes_test(is_member, login_url='mb/')
def member_view(request):
    return HttpResponse("You are a member")

@permission_required("relationship_app.can_add_book")
def can_add_book(request):
    return render(request,"relationship_app/add_book.html")

@permission_required("relationship_app.can_change_book")
def can_edit_book(request, pk):
    book = Book.objects.get(Book, pk=pk)
    return render(request, "relationship_app/edit_book.html", {"book": book})

@permission_required("relationship_app.can_delete_book")
def can_delete_book(request, pk):
    book = Book.objects.get(Book, pk=pk)
    return render(request, "relationship_app/delete_book.html", {"book": book})
