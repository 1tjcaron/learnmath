import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class PercForm(forms.Form):
    # https://stackoverflow.com/questions/871037/django-overriding-init-for-custom-forms
    # perc = 0;

    problem_one = forms.DecimalField(
        help_text="Find 0% of 60", 
        widget=forms.NumberInput(attrs={'style':'max-width: 40px; border-color:darkgoldenrod; border-radius: 10px;'}),
        decimal_places=0)
    problem_two = forms.DecimalField(
        help_text="Find 100% of 60", 
        widget=forms.NumberInput(attrs={'style':'max-width: 40px; border-color:darkgoldenrod; border-radius: 10px;'}),
        decimal_places=0)
        
class ZeroPercForm(PercForm):
     def __init__(self,  *args, **kwargs):   
        super(ZeroPercForm, self ).__init__(*args, **kwargs)
        self.fields["problem_one"].help_text = "HELP PLEASE"

class NumberLineForm(forms.Form):
    problem_one = forms.DecimalField(decimal_places=0, 
        widget=forms.NumberInput(attrs={'style':'max-width: 40px; border-color:darkgoldenrod; border-radius: 10px;'}))

# class ZeroPercForm(forms.Form):
#     def __init__(self, **kwargs):
#         # Define one message for all fields.
#         error_messages = {
#             'incomplete': 'Enter a country calling code and a phone number.',
#         }
#         # Or define a different message for each field.
#         fields = (
#             CharField(
#                 error_messages={'incomplete': 'Enter a country calling code.'},
#                 validators=[
#                     RegexValidator(r'^[0-9]+$', 'Enter a valid country calling code.'),
#                 ],
#             ),
#             CharField(
#                 error_messages={'incomplete': 'Enter a phone number.'},
#                 validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')],
#             ),
#             CharField(
#                 validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid extension.')],
#                 required=False,
#             ),
#         )
#         super().__init__(
#             fields=fields,
#             require_all_fields=False, **kwargs
#         )
