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