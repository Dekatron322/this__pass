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
from .models import *
#from resume.models import Resume


def ShopCartView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	card = Card.objects.get()
	if request.method == "POST":
		quantity = request.POST.get("quantity")

		cart = ShopCart.objects.create(app_user=app_user, card=card, quantity=quantity)
		cart.save()

		messages.warning(request, "Welldone! Profile Data Updated")
		return HttpResponseRedirect(reverse("order:shipping"))


	else:
		shopcart = Card.objects.all()

		context = {"shopcart":shopcart, "app_user":app_user, "card":card}
		return render(request, "order/cart.html", context )


def ShippingView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	cards = ShopCart.objects.filter(app_user=app_user)
	total=0
	for rs in cards:
		total += rs.card.price * rs.quantity + rs.card.shipping_charge
	if request.method == "POST":
		form = OrderForm(request.POST)
		if form.is_valid():
			data = Order()
			data.first_name = form.cleaned_data['first_name']
			data.last_name = form.cleaned_data['last_name']
			data.email = form.cleaned_data['email']
			data.address = form.cleaned_data['address']
			data.city = form.cleaned_data['city']
			data.state = form.cleaned_data['state']
			data.phone = form.cleaned_data['phone']
			data.country = form.cleaned_data['country']
			data.postal_code = form.cleaned_data['postal_code']
			data.user_id = app_user.id
			data.total = total
			data.ip = request.META.get('REMOTE_ADDR')
			ordercode = get_random_string(5).upper()
			data.code = ordercode
			data.app_user = app_user
			data.save()

			cards = ShopCart.objects.filter(app_user=app_user.id)
			for rs in cards:
				detail = OrderProduct()
				detail.order_id = data.id
				detail.card_id = rs.card_id
				detail.app_user = app_user
				detail.quantity = rs.quantity
				detail.price = rs.card.price
				detail.save()

				card = Card.objects.get(id=rs.card_id)
				card.save()	

			ShopCart.objects.filter(app_user=app_user.id).delete()
			request.session['cart_items']=0

			return HttpResponseRedirect(reverse("payment:make_payment", args=[data.id,]))

			
			#return render(request, 'order/order_complete.html', {'ordercode':ordercode})
		else:
			messages.warning(request, form.errors)
			return HttpResponseRedirect("/order/shipping")	

	else:

		shipping = 0
		for rs in cards:
			shipping = rs.card.shipping_charge

		price = 0
		for rs in cards:
			price = rs.card.price 

		subtotal=0
		for rs in cards:
			subtotal += rs.card.price * rs.quantity


		added=0
		for rs in cards:
			added +=  rs.quantity + shipping

		form = OrderForm()
		context = {
			"app_user":app_user, 
			"cards":cards, 
			"price":price, 
			"subtotal":subtotal,
			'added':added, 
			'total':total, 
			'shipping':shipping,
			'form':'form',}
		return render(request, "order/shipping.html", context )

def CompleteView(request, id):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		pass
	else:
		card = CardInfo.objects.get(id=id)
		context = {"app_user":app_user, "card":card}
		return render(request, "order/order_complete.html", context )

def UpdateAppuserView(request, order_id):
	order = Order.objects.get(id=order_id)
	app_user = AppUser.objects.get(user__pk=request.user.id)
	if request.method == "POST":
		#card primary info
		try:
			card_profile_photo = request.FILES["card_profile_photo"]
		except:
			card_profile_photo = card.card_profile_photo
		app_user = AppUser.objects.get(user__pk=request.user.id)
		card_first_name = request.POST.get("card_first_name")
		card_last_name = request.POST.get("card_last_name")
		card_code = request.POST.get("card_code")
		card_email = request.POST.get("card_email")
		card_company = request.POST.get("card_company")
		card_phone_no = request.POST.get("card_phone_no")
		card_website = request.POST.get("card_website")
		card_job_title = request.POST.get("card_job_title")

		#card address info
		card_address = request.POST.get("card_address")
		card_city = request.POST.get("card_city")
		card_state = request.POST.get("card_state")
		card_zip_code = request.POST.get("card_zip_code")
		card_country = request.POST.get("card_country")

		#card socil info
		facebook_link = request.POST.get("facebook_link")
		twitter_link = request.POST.get("twitter_link")
		instagram_link = request.POST.get("instagram_link")
		linkedin_link = request.POST.get("linkedin_link")

		app_user = CardInfo.objects.create(
			card_profile_photo=card_profile_photo,
			app_user=app_user, 
			card_code=card_code,
			card_first_name=card_first_name, 
			card_last_name=card_last_name, 
			card_email=card_email, 
			card_company=card_company, 
			card_phone_no=card_phone_no,
			card_website=card_website,
			card_job_title=card_job_title,
			card_address=card_address,
			card_country=card_country,
			card_city=card_city,
			card_state=card_state,
			card_zip_code=card_zip_code,
			facebook_link=facebook_link,
			twitter_link=twitter_link,
			instagram_link=instagram_link,
			linkedin_link=linkedin_link,
		)
		app_user.save()
	
			
		
		return HttpResponseRedirect(reverse("order:confirm"))
			
	else:
		app_user = AppUser.objects.get(user__pk=request.user.id)

		context = {"app_user":app_user, "order":order}
		return render(request, "order/update_profile.html", context )

def ConfirmView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	card_info = CardInfo.objects.all().order_by('-id')[:1]
	if request.method == "POST":
		pass


	else:


		context = {"app_user": app_user, "card_info":card_info}
		return render(request, "order/confirm_details.html", context )


def DashboardView(request, id):
	order = Order.objects.all()
	card = CardInfo.objects.get(id=id)
	app_user = AppUser.objects.get(user__pk=request.user.id)
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
		

		context = {"app_user": app_user, 'card':card, "order":order}
		return render(request, "order/dashboard.html", context )



