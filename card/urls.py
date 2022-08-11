from django.urls import path
from . import views

app_name = "card"

urlpatterns = [

    path("<str:app_user>/", views.MyCardView, name="card"),
    
    path("card/", views.CardView, name="card"),

]