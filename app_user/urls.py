from django.urls import path
from . import views

app_name = "app_user"

urlpatterns = [

	path("sign-in/", views.SignInView, name="sign_in"),
	path("sign-up/", views.SignUpView, name="sign_up"),
	path("sign-up/complete/", views.CompleteSignUpView, name="complete_sign_up"),
	path("sign-out/", views.SignOutView, name="sign_out"),
	path("verified/", views.VerifiedView, name="verified"),
    path("", views.DashboardView, name="dashboard"),

]