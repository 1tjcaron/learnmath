from django.urls import path

from . import views

urlpatterns = [    
    path('', views.hello, name='hello'),
]
urlpatterns += [
    path('quiz/zeroperc/', views.quiz_zero_perc, name='zero-perc'),
]
