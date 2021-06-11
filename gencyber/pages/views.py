from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Card Home Page</h1>")


def blue_view(*args, **kwargs):
    return HttpResponse("<h1>Blue Card Page</h1>")


def darkblue_view(*args, **kwargs):
    return HttpResponse("<h1>Dark Blue Card Page</h1>")