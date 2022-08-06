from django.db import models
from django.utils import timezone

from app_user.models import *
from card.models import *
from order.models import *


# Create your models here.

class Payment(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	status = models.BooleanField(default=False)

	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.order.code