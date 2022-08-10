from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone


class AppUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	phone_no = models.CharField(default="", max_length=100)
	user_name = models.CharField(default="", max_length=100)

	pub_date = models.DateTimeField(default=timezone.now)

	otp_code = models.CharField(default="none",max_length=10)

	ec_status = models.BooleanField(default=False)
	status = models.BooleanField(default=False)


	def __str__(self):
		return self.user.username
