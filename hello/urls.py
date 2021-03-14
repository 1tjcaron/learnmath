from django.urls import path

from . import views

urlpatterns = [    
    path('', views.hello, name='hello'),
    path('1', views.hi2, name='hi2'),
    path('quiz/percentage/<int:problem_number>', views.quiz_percentage, name='perc'),
    path('quiz/percentage/success', views.pass_quiz_percentage, name='pass-perc'),
    path('quiz/numberline/', views.quiz_number_line, name='number-line'),
]
