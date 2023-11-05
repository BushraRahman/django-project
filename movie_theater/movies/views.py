from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.messages import get_messages
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
            messages.add_message(request,messages.INFO,f"{request.POST['name']} was added.")
            return response
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MoviesForm()
    return render(request, "movies/form.html", {"form": form})

def edit(request, id):
    response = redirect('/')
    cookieDict = json.loads(request.COOKIES['movie_list'])
    form = MoviesForm(cookieDict[str(id)])
    if (str(id) not in cookieDict):
        messages.add_message(request, messages.ERROR, f"Error: ID {id} cannot be edited since it does not exist.")
        return render(request, "movies/edit.html")
    elif (form.is_valid()):
        return render(request, "movies/edit.html", context={'form': form})

def maxID(list):
    if len(list) == 0:
        return 1
    ids = []
    for element in reversed(list):
        for key in element:
            ids.append(int(key))
    return max(ids)+1
    return max(ids)+1

def checkValid(name, list):
    print(type(list))
    for key, element in list.items():
        if(element['name'].casefold() == name):
            return False
    return True

def delete(request, id):
    response = redirect("list")
    #messages.add_message(request,messages.SUCCESS,"yass")
    cookieDict = json.loads(request.COOKIES['movie_list'])
    if (str(id) not in cookieDict):
        messages.add_message(request, messages.ERROR, f"Error: ID {id} cannot be deleted since it does not exist.")
        return render(request, "movies/delete.html")
    else:
        name = cookieDict[str(id)]['name']
        messages.add_message(request, messages.SUCCESS,f"{id}")
        storage = get_messages(request)
        for message in storage:
            print(message)
        if(request.GET.get('yes')):
            del cookieDict[str(id)]
            response.set_cookie(key="movie_list",value=json.dumps(cookieDict))
            messages.add_message(request,messages.INFO,f"{name} was deleted.")
            return response
        if(request.GET.get('no')):
            messages.add_message(request,messages.INFO,f"Deletion of {name} was cancelled.")
            return response
        return render(request, "movies/delete.html", context={'cookie': json.loads(request.COOKIES['movie_list'])[str(id)], 'id': id})
# Create your views here.