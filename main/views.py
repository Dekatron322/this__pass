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
from app_user.models import *
from card.models import *
from order.models import *
from .models import *
#from resume.models import Resume
#if request.method == "POST":
        
        #pass
    #else:
        #context = {}
        #return render(request, "main/index.html", context )



def IndexView(request):
    if request.method == "POST":
        pass
    else:
        context = {}
        return render(request, "main/index.html", context)
	
def URLProfileView(request, app_user):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass
	else:

		card = CardInfo.objects.all().order_by('-id')[:1]
		context = {"app_user": app_user, "card":card}
		return render(request, "order/url_profile.html", context )	
    
