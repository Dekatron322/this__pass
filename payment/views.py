from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate

from django.utils.crypto import get_random_string

from datetime import datetime
import datetime as dt
import requests

from card.models import *
from payment.models import *
from order.models import *

#from resume.models import Resume



def PayNow(request, order_id):
    order = Order.objects.get(id=order_id)
    app_user = AppUser.objects.get(user__pk=request.user.id)
    if request.method == "POST":
        return HttpResponseRedirect(reverse("payment:confirm_payment", args=[order.id,]))



    else:

        context = {"order": order, "app_user":app_user}
        return render(request, "payment/make_payment.html", context )


def ConfirmPayment(request, order_id):
    app_user = AppUser.objects.get(user__pk=request.user.id)
    order = Order.objects.get(id=order_id)
    if request.method == "POST":
        

        payment = Payment.objects.create(order=order)
        payment.status = True
        payment.save()

        return HttpResponseRedirect(reverse("order:update_appuser", args=[order.id,]))

    else:
        context = {"order": order, "app_user":app_user}
        return render(request, "payment/confirm_payment.html", context )


def Success(request):
    if request.method == "POST":
        pass
    

    else:
        context = {}
        return render(request, "payment/success.html", context )