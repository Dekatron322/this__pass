from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from datetime import datetime
import datetime as dt
import requests
from order.models import *
from .forms import UserForm
from .models import *
#from resume.models import Resume

import random
import string

def muri_randomiser(length=4):
	landd = string.ascii_letters + string.digits
	return ''.join((random.choice(landd) for i in range(length)))

def MuriSendMail(request, subject, message, to_email, code=None):

    try:
        context = {"subject": subject, "message": message, "code": code}
        html_message = render_to_string('app_user/message.html', context)
        message = strip_tags(message)
    
        send_mail(
            subject,
            message,
            'thispass@thispass.io',
            [to_email,],
            html_message=html_message,
            fail_silently=False,
        )

    except:
        pass


def SignInView(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)

				app_user = AppUser.objects.get(user__pk=request.user.id)
				
				if app_user.ec_status == True:
				
					print("11111111111111111111111111111111")
					messages.success(request, "Welcome Onboard")
					return HttpResponseRedirect(reverse("app_user:dashboard"))
				
				else:
					print("22222222222222222222222222222222")
					messages.warning(request, "Sorry, validate your account")
					return HttpResponseRedirect(reverse("app_user:sign_in"))
				
			else:
				print("22222222222222222222222222222222")
				messages.warning(request, "Invalid Email or Password")
				return HttpResponseRedirect(reverse("app_user:sign_in"))

		else:
			print("33333333333333333333333333333333333333")
			messages.warning(request, "Invalid Email or Password")
			return HttpResponseRedirect(reverse("app_user:sign_in"))

	else:
		context = {}
		return render(request, "app_user/sign_in.html", context )




def SignUpView(request):
	if request.method == "POST":

		form = UserForm(request.POST or None, request.FILES or None)
		email = request.POST.get("username")
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		phone_no = request.POST.get("phone_no")
		user_name = request.POST.get('user_name')
		#account_type = request.POST.get("account_type")


		if request.POST.get("password2") != request.POST.get("password1"):
			messages.warning(request, "Make sure both passwords match")
			return HttpResponseRedirect(reverse("app_user:sign_up"))
			
		elif AppUser.objects.filter(user_name=request.POST.get("user_name")).exists(): 
		    messages.warning(request, "Username Taken")
		    return HttpResponseRedirect(reverse("app_user:sign_up"))
			
		else:
			try:
				AppUser.objects.get(user__email=request.POST.get("username"))
				messages.warning(request, "Email Address already taken, try another one!")
				return HttpResponseRedirect(reverse("app_user:sign_up"))


			except:
				user = form.save()
				user.set_password(request.POST.get("password1"))
				user.save()

				app_user = AppUser.objects.create(user=user)
				app_user.otp_code = muri_randomiser()


				user = app_user.user
				user.email = email
				user.save()
				app_user.phone_no = phone_no
				app_user.user_name = user_name
				app_user.save()
				
				#MuriSendMail(request, subject="Email Confirmation.", message="Thank you for signing up with Thispass, Your OTP code is %s" % (app_user.otp_code), to_email=app_user.user.username, code=app_user.otp_code)

				if user:
					if user.is_active:
						login(request, user)

						app_user = AppUser.objects.get(user__pk=request.user.id)
						messages.warning(request, "Enter the verification code that was sent to your mail.")
						return HttpResponseRedirect(reverse("app_user:complete_sign_up"))

	else:
		form = UserForm()
		context = {"form": form}
		return render(request, "app_user/sign_up.html", context )



	return render(request, "app_user/sign_up.html", context )


def DashboardView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	card = CardInfo.objects.filter(app_user=app_user).order_by('-id')[:1]
	if request.method == "POST":
		app_user = AppUser.objects.get(user__pk=request.user.id)
		card_first_name = request.POST.get("card_first_name")
		card_last_name = request.POST.get("card_last_name")
		card_email = request.POST.get("card_email")
		card_company = request.POST.get("card_company")
		card_phone_no = request.POST.get("card_phone_no")
		card_website = request.POST.get("card_website")
		card_job_title = request.POST.get("card_job_title")

		card_address = request.POST.get("card_address")
		card_city = request.POST.get("card_city")
		card_state = request.POST.get("card_state")
		card_zip_code = request.POST.get("card_zip_code")
		card_country = request.POST.get("card_country")

		facebook_link = request.POST.get("facebook_link")
		twitter_link = request.POST.get("twitter_link")
		instagram_link = request.POST.get("instagram_link")
		linkedin_link = request.POST.get("linkedin_link")


		card.card_first_name = card_first_name
		card.card_last_name = card_last_name
        
		card.card_email = card_email
		card.card_company = card_company
		card.card_phone_no = card_phone_no
		card.card_website = card_website
		card.card_job_title = card_job_title

		card.card_address = card_address
		card.card_city = card_city
		card.card_state = card_state
		card.card_zip_code = card_zip_code
		card.card_country = card_country

		card.facebook_link = facebook_link
		card.twitter_link = twitter_link
		card.instagram_link = instagram_link
		card.linkedin_link = linkedin_link

		card.save()

        
		return HttpResponseRedirect(reverse("order:dashboard", args=[card.id]))


	else:
		order = Order.objects.all()
		
		context = {"app_user": app_user, "card":card, "order":order}
		return render(request, "app_user/dashboard.html", context )


def CompleteSignUpView(request):
	if request.method == "POST":
		otp = request.POST.get("otp")
		
		app_user = AppUser.objects.get(user__pk=request.user.id)
		if otp == app_user.otp_code:
			app_user.ec_status = True
			app_user.save()

			
			return HttpResponseRedirect(reverse("app_user:verified"))

		else:
			messages.warning(request, "Sorry, Invalid OTP Code.")
			return HttpResponseRedirect(reverse("app_user:complete_sign_up"))


	else:
		context = {}
		return render(request, "app_user/complete_sign_up.html", context )

def SignOutView(request):

	logout(request)
	return HttpResponseRedirect(reverse("app_user:sign_in"))

def VerifiedView(request):
	if request.method == "POST":
		pass

	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)

		context = {"app_user": app_user}
		return render(request, "app_user/verified.html", context )
		
def ForgotPasswordView(request):
    
    if request.method == "POST":
        email = request.POST.get("username")
        
        app_users = AppUser.objects.filter(user__username=email)
        
        if len(app_users) > 0:
            app_user = app_users.last()
            app_user.otp_code = muri_randomiser()
            app_user.save()
            
            #MuriSendMail(request, subject="Password Reset.", message="Looks like you lost your password. Kindly use this OTP code; %s to retrieve your account." % (app_user.otp_code), to_email=app_user.user.username, code=app_user.otp_code)

        
            messages.warning(request, "Set new password.")
            return HttpResponseRedirect(reverse("app_user:set_new_p"))
        
        else:
            messages.warning(request, "Sorry, Invalid OTP code.")
            return HttpResponseRedirect(reverse("app_user:forgot_password"))
        
        
    else:
        
        context = {}
        return render(request, "app_user/forgot_password.html", context)


def SetNewPView(request):
    
    if request.method == "POST":
        otp = request.POST.get("otp")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        app_users = AppUser.objects.filter(otp_code=otp)
        
        if request.POST.get("password2") != request.POST.get("password1"):
            messages.warning(request, "Make sure both passwords match")
            return HttpResponseRedirect(reverse("app_user:set_new_p"))
            
        elif len(app_users) > 0:
            app_user = app_users.last()
            
            user = app_user.user
            user.set_password(str(password2))
            user.save()
        
            messages.warning(request, "New Password Created!")
            return HttpResponseRedirect(reverse("app_user:sign_in"))
            
        else:
            messages.warning(request, "Sorry, Invalid OTP code.")
            return HttpResponseRedirect(reverse("app_user:set_new_p"))
        
        
    else:
        context = {}
        return render(request, "app_user/set_new_p.html", context)
 



