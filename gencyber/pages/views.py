from django.shortcuts import render
from django.http import HttpResponse
from cards.models import Card

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Card Home Page</h1>")
    return render(request, "home.html", {})

def card_detail_view(request):
    blue_cards = Card.objects.filter(color='Blue')
    context = {
        'list': blue_cards,
    }
    return render(request, "card/detail.html", context)

def blue_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Blue Card Page</h1>")
    blue_cards = Card.objects.filter(color='Blue')
    context = {
        'list': blue_cards,
    }
    return render(request, "blue.html", context)


def darkblue_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Dark Blue Card Page</h1>")
    darkblue_cards = Card.objects.filter(color='Dark Blue')
    context = {
        'list': darkblue_cards,
    }
    return render(request, "darkblue.html", context)


def red_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Dark Blue Card Page</h1>")
    red_cards = Card.objects.filter(color='Red')
    context = {
        'list': red_cards,
    }
    return render(request, "red.html", context)

def darkred_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Dark Blue Card Page</h1>")
    darkred_cards = Card.objects.filter(color='Dark Red')
    context = {
        'list': darkred_cards,
    }
    return render(request, "darkred.html", context)

def green_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Dark Blue Card Page</h1>")
    green_cards = Card.objects.filter(color='Green')
    context = {
        'list': green_cards,
    }
    return render(request, "green.html", context)

def darkgreen_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Dark Blue Card Page</h1>")
    darkgreen_cards = Card.objects.filter(color='Dark Green')
    context = {
        'list': darkgreen_cards,
    }
    return render(request, "darkgreen.html", context)