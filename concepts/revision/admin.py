from django.contrib import admin
from .models import Author, Publisher, Book

# Register your models here.

class BookInline(admin.TabularInline):
    model = Book
    extra = 1

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','nationality', 'birth_date')
    search_fields = ('name', 'nationality')
    inlines = [BookInline] 

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'established_year')
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'publication_date', 'isbn')
    search_fields = ('title', 'author__name', 'publisher__name')
    list_filter = ('author', 'publisher')
    date_hierarchy = 'publication_date'
    fields = ('title', 'author', 'publisher', 'isbn')  # Only show specific fields in the form
    readonly_fields = ('isbn',) 