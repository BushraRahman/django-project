from django import forms


class MoviesForm(forms.Form):
    name = forms.CharField(label="Name", min_length=3, max_length=100, required=True)
    #need to add min and max value to year
    year = forms.IntegerField(label="Year", required=True)
    actors = forms.CharField(required=True, widget=forms.Textarea)