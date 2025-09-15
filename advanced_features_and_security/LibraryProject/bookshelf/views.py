from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required


# Create your views here.


def add_book(request):
    return HttpResponse('Added')

@permission_required('bookshelf.can_edit',raise_exception=True)
def edit_book(request):
    return HttpResponse('Edit')


def delete_book(request):
    return HttpResponse('Delete')

