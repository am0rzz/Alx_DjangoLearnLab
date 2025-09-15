from django.contrib import admin
from .models import Book
from .models import CustomUser
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
admin.site.register(Book, BookAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')


admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
