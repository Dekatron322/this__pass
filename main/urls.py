from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.IndexView, name="index"),
    path("<str:app_user>/", views.URLProfileView, name="profile"),
]