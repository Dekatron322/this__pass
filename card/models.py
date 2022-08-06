from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

class Card(models.Model):
	name = models.CharField(max_length=150, default="ThisPass")
	tag_title = models.CharField(max_length=150, default="Sale")

	color = models.CharField(max_length=150, default="ThisPass Black Card")
	image = models.FileField(upload_to='card/image/', blank=True, default="default_files/default_face.jpg")


	quantity = models.IntegerField(default=1)
	threshold = models.IntegerField(blank=True, null=True, default=1)
	price = models.IntegerField(default=1)
	shipping_charge = models.FloatField(default=1)

	delivery_info = models.CharField(max_length=150, default="none")


	slug = models.SlugField(unique=True, default="myslug")
	pub_date = models.DateTimeField(default=timezone.now)

	
	def save(self, *args, **kwargs):
		var = self.name +"-" + str(self.pub_date)
		self.slug = slugify(var)
		super().save(*args, **kwargs)
		
	def get_absolute_url(self):
		return "/product-detail/%s/"%self.slug
		
	def __str__(self):
		return self.name