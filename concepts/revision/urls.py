from .views import homepage_view, ContactView
from django.urls import path

urlpatterns = [
    path('', homepage_view, name='home'),
    path('contact/', ContactView.as_view(), name = 'contact'),
]