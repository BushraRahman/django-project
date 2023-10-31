from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

from .forms import MoviesForm


def create(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = MoviesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/movies/list")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MoviesForm()
    return render(request, "movies/form.html", {"form": form})

def list(request):
	return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
