from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'hello.html', {})


import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms



def pass_quiz_percentage(request):
    return HttpResponse('Great Job! Go <a href="/"> back home</a>')

def quiz_percentage(request, problem_number):
    problems = {
        1: (10, 20, 60),
        2: (10, 30, 60),
        3: (10, 15, 100),
        4: (15, 30, 100),
        5: (0, 100, 20),
    }

    
    # book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = forms.DefinedPercForm(*problems.get(problem_number, (0, 0, 0)), request.POST)

        # Check if the form is valid:
        if form.is_valid():
            if problem_number < max(problems.keys()):
                return HttpResponseRedirect(f"/quiz/percentage/{problem_number + 1}")
            else:
                return HttpResponseRedirect(f"/quiz/percentage/success")
    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = forms.DefinedPercForm(*problems.get(problem_number, (0, 0, 0)), initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'problem': f"Problem ({problem_number}/5)"
        # 'book_instance': book_instance,
    }

    return render(request, 'quiz_zero_perc.html', context)

def quiz_number_line(request):
    # book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = forms.NumberLineForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            return HttpResponseRedirect("/" )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = forms.NumberLineForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        # 'book_instance': book_instance,
    }

    return render(request, 'quiz_number_line.html', context)
