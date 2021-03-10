from django.urls import path

from . import views

urlpatterns = [    
    path('', views.hello, name='hello'),
]
urlpatterns += [
    path('quiz/percentage/', views.quiz_percentage, name='perc'),
    path('quiz/numberline/', views.quiz_number_line, name='number-line'),
]
