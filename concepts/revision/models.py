from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Custom Manager Example
class AvailableManager(models.Manager):
    def available(self):
        return self.filter(is_available=True)

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, choices=[('US', 'United States'), ('UK', 'United Kingdom'), ('IN', 'India')])

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    established_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    publication_date = models.DateField(default=timezone.now)
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    is_available = models.BooleanField(default=True)

    # Meta options
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Books'

    # Custom Manager
    objects = models.Manager()  # The default manager
    available_books = AvailableManager()  # Custom manager for available books

    def __str__(self):
        return self.title

    # Custom method
    def available_status(self):
        return "Available" if self.is_available else "Not Available"

class Borrower(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    borrowed_books_new = models.ManyToManyField(Book, through='Borrow')

    def __str__(self):
        return self.user.username

class Borrow(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.borrower.user.username} borrowed {self.book.title}"

    # Example of a model method
    def is_overdue(self):
        return self.return_date and self.return_date < timezone.now()
