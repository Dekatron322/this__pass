from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate



from datetime import datetime
import datetime as dt
import requests


from .models import *
#from resume.models import Resume


def CardView(request):
	if request.method == "POST":
		pass
