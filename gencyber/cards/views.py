from django.shortcuts import render
from .models import Card
# Create your views here.
def card_detail_view(request):
    blue_cards = Card.objects.filter(color='Blue')
    context = {
        'list': blue_cards,
    }
    return render(request, "card/detail.html", context)