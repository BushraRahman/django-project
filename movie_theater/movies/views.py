from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
import json
from .forms import MoviesForm

def list(request):
    movie_cookies = request.COOKIES
    movie_list = {}
    response = render(request, "movies/cookies.html")
    if 'movie_list' in movie_cookies:
        print(request.COOKIES['movie_list'])
        return render(request, "movies/cookies.html", context={'movie_list': json.loads(request.COOKIES['movie_list'])})
    else:
        response.set_cookie(key="movie_list", value=json.dumps({}))
        return render(request, "movies/cookies.html", context={'movie_list': {}})

def create(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        form = MoviesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            response = redirect("list")
            formData = {
            'name': request.POST['name'],
                'year': request.POST['year'],
                'actors': request.POST['actors']}
            #maxID(json.loads(request.COOKIES['movie_list']))
            if 'movie_list' not in request.COOKIES:
                response.set_cookie(key="movie_list", value=json.dumps({1: formData}))
            else:
                cookieDict = json.loads(request.COOKIES['movie_list'])
                newData = json.loads(request.COOKIES['movie_list'])
                newData[maxID(cookieDict)] = formData
                if(checkValid(request.POST['name'].casefold(),cookieDict)):
                    response.set_cookie(key="movie_list",value=json.dumps(newData))
                else:
                    form.add_error("name",ValidationError((f"{request.POST['name']} is already in the list."), code="invalid"))
                    return render(request, "movies/form.html", {"form": form})
            return response
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MoviesForm()
    return render(request, "movies/form.html", {"form": form})

def maxID(list):
    if len(list) == 0:
        return 1
    ids = []
    for element in reversed(list):
        for key in element:
            ids.append(int(key))
    return max(ids)+1

def checkValid(name, list):
    print(type(list))
    for key, element in list.items():
        if(element['name'].casefold() == name):
            return False
    return True

def edit(request, id):
    return HttpResponse("yo let's edit")

def delete(request, id):
    return HttpResponse("you sure about that...?")
# Create your views here.
