from django.urls import path

from . import views

urlpatterns = [    
    path('', views.hello, name='hello'),
]
urlpatterns += [
    path('book/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]
