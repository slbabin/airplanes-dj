from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def say_hello(request):
    return HttpResponse("Hello!")


def index(request):
    return HttpResponse("This is index page!")


def category(request, cat):
    return HttpResponse(f"<h1>Category</h1><p>{cat}</p>")


def archive(request, year):
    if int(year) > 2020:
        raise Http404()

    return HttpResponse(f"<h1> Archive by years</h1> <p>{year}</p>")

    # return redirect('home', permanent=False)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>The page not found!</h1>')

