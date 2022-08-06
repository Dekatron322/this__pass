from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput
from card.models import Card
from app_user.models import AppUser
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput


# Create your models here.
class ShopCart(models.Model):
	app_user = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True)
	card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=1)



	def __str__(self):
		return self.card.name

	@property
	def price(self):
		return (self.card.price)

	@property
	def amount(self):
		return (self.quantity * self.card.price)




class Order(models.Model):
	STATUS = (
			('New', 'New'),
			('Accepted', 'Accepted'),
			('Preapparing', 'Preapparing'),
			('OnShipping', 'OnShipping'),
			('Completed', 'Completed'),
			('Cancelled', 'Cancelled'),
		)
	app_user = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True)
	code = models.CharField(max_length=5, editable=False)
	first_name = models.CharField(max_length=125)
	last_name = models.CharField(max_length=125)
	email = models.CharField(max_length=125)
	phone = models.CharField(blank=True, max_length=125)
	address = models.CharField(blank=True, max_length=150)
	city = models.CharField(blank=True, max_length=125)
	state = models.CharField(blank=True, max_length=125)
	postal_code = models.CharField(blank=True, max_length=125)
	country = models.CharField(blank=True, max_length=125)
	total=models.FloatField()
	status = models.CharField(max_length=15, choices=STATUS, default='New')
	adminnote = models.CharField(blank=True ,max_length=125)
	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

    
	

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = ['first_name', 'last_name', 'email', 'address', 'phone', 'city', 'state', 'postal_code', 'country']


	def __str__(self):
		return self.user.first_name

	def __str__(self):
		return self.card_first_name

class OrderProduct(models.Model):
	STATUS = (
		('New', 'New'),
		('Accepted', 'Accepted'),
		('Cancelled', 'Cancelled'),
		)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	card = models.ForeignKey(Card, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	price = models.FloatField()
	status = models.CharField(max_length=15, choices=STATUS, default='New')
	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.card.name


class CardInfo(models.Model):
	
    app_user = models.ForeignKey(AppUser, on_delete=models.SET_NULL, null=True)
    card_code = models.CharField(default="",max_length=2000)
    card_first_name = models.CharField(default="",max_length=2000)
    card_last_name = models.CharField(default="",max_length=2000)
    card_phone_no = models.CharField(default="",max_length=100)
    card_email = models.CharField(default="",max_length=2000)
    card_profile_photo = models.FileField(upload_to='account_files/profile_photos/', blank=True, default="default_files/default_face.jpg")
    card_website = models.CharField(default="",max_length=1000)
    card_job_title = models.CharField(default="",max_length=1000)
    card_company = models.CharField(default="",max_length=30, null=True)

    #card address info
    card_address = models.CharField(default="",max_length=30, null=True)
    card_city = models.CharField(default="",max_length=30, null=True)
    card_state = models.CharField(default="",max_length=30, null=True)
    card_zip_code = models.CharField(default="",max_length=30, null=True)
    card_country = models.CharField(default="",max_length=30, null=True)

    #card social links
    facebook_link = models.CharField(default="",max_length=30, null=True)
    twitter_link = models.CharField(default="",max_length=30, null=True)
    instagram_link = models.CharField(default="",max_length=30, null=True)
    linkedin_link = models.CharField(default="",max_length=30, null=True)

    def __str__(self):
    	return self.card_code




	





