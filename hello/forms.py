import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_match(value, expected_value):
    if value != expected_value:
        raise ValidationError(f"Oops!  Looks like {value} is incorrect. Tap the yellow help button below.")

        
NUM_STYLE ={'class':"form-control-inline", 'style':'max-width: 80px;'};
class AnyPercForm(forms.Form):
    # https://stackoverflow.com/questions/871037/django-overriding-init-for-custom-forms
    problem_one = forms.IntegerField(
        widget=forms.NumberInput(
            attrs=NUM_STYLE),
            )
    problem_two = forms.IntegerField(
        widget=forms.NumberInput(
            attrs=NUM_STYLE)
        )
        
class DefinedPercForm(AnyPercForm):
     def __init__(self, p1, p2, n, *args, **kwargs):   
        super(DefinedPercForm, self ).__init__(*args, **kwargs)
        def validator_one(value):
            validate_match(value, p1 * .01 * n)
        def validator_two(value):
            validate_match(value, p2 * .01 * n)

        
        self.fields["problem_one"].help_text = f"Find {p1}% of {n}"
        self.fields["problem_one"].validators = [validator_one]
        self.fields["problem_two"].help_text = f"Find {p2}% of {n}"
        self.fields["problem_two"].validators = [validator_two]

class NumberLineForm(forms.Form):
    problem_one = forms.DecimalField(
        decimal_places=0,
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs=NUM_STYLE))

