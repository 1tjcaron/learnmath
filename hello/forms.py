import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

NUM_STYLE ={'class':"form-control-inline", 'style':'max-width: 100px;'};
class AnyPercForm(forms.Form):
    # https://stackoverflow.com/questions/871037/django-overriding-init-for-custom-forms
    problem_one = forms.DecimalField(
        widget=forms.NumberInput(
            attrs=NUM_STYLE),
        decimal_places=0,
        min_value=0,
        max_value=100)
    problem_two = forms.DecimalField(
        widget=forms.NumberInput(
            attrs=NUM_STYLE),
        decimal_places=0,
        min_value=0,
        max_value=100
        )
        
class DefinedPercForm(AnyPercForm):
     def __init__(self, p1, p2, n, *args, **kwargs):   
        super(DefinedPercForm, self ).__init__(*args, **kwargs)
        
        self.fields["problem_one"].help_text = f"Find {p1}% of {n}"
        self.fields["problem_two"].help_text = f"Find {p2}% of {n}"

class NumberLineForm(forms.Form):
    problem_one = forms.DecimalField(
        decimal_places=0,
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs=NUM_STYLE))

