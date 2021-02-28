from django.urls import path

from . import views

urlpatterns = [    
    path('', views.hello, name='hello'),
]
urlpatterns += [
    path('quiz/zeroperc/', views.quiz_zero_perc, name='zero-perc'),
    path('quiz/numberline/', views.quiz_number_line, name='number-line'),
]
