from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("hello")


import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms


def quiz_zero_perc(request):
    # book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = forms.ZeroPercForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            return HttpResponseRedirect("/" )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = forms.ZeroPercForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        # 'book_instance': book_instance,
    }

    return render(request, 'quiz_zero_perc.html', context)
