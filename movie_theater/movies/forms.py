from django import forms
from django.core.exceptions import ValidationError
from django.forms import ValidationError

class MoviesForm(forms.Form):
    name = forms.CharField(
        label="Name",
        min_length=3,
        max_length=100,
        required=True,
        )
    year = forms.IntegerField(
        label="Year",
        min_value=1880,
        max_value=2025,
        required=True,
        )
    actors = forms.CharField(
        required=True,
        widget=forms.Textarea,
        )