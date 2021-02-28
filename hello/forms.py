import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class ZeroPercForm(forms.Form):
    problem_one = forms.DecimalField(help_text="Find 0% of 60", decimal_places=0)
    problem_two = forms.DecimalField(help_text="Find 100% of 60", decimal_places=0)

class NumberLineForm(forms.Form):
    problem_one = forms.DecimalField(decimal_places=0, 
        widget=forms.NumberInput(attrs={'style':'max-width: 40px; border-color:darkgoldenrod; border-radius: 10px;'}))
