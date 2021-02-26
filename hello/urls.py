from django.urls import path

from . import views

urlpatterns = [    
    path('', views.hello, name='hello'),
]
urlpatterns += [
    path('test/zeroperc/', views.renew_book_librarian, name='zero-perc'),
]
