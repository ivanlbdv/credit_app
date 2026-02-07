from django.shortcuts import render
from .models import CreditOffer


def index(request):
    offers = CreditOffer.objects.all()
    return render(request, 'offers/index.html', {'offers': offers})
