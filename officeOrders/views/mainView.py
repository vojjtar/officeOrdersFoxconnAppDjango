from django.http import HttpResponse
from django.shortcuts import render


def orderPage(request):
    return render(request, 'order/orderPage.html')