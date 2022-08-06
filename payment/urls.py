from django.urls import path
from . import views

app_name = "payment"

urlpatterns = [

    path("make-payment/<int:order_id>/pay-now/", views.PayNow, name="make_payment"),
	path("confirm-payment/<int:order_id>/", views.ConfirmPayment, name="confirm_payment"),
	path("success/", views.Success, name="success"),

]