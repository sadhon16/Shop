from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

def Index(request):
    return render(request, 'index.html')

@login_required(login_url="index")
def OrderM(requst):
    order = Order.objects.all()
    return render(requst, "order.html", {"order":order})