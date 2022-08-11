from django.urls import path
from . import views

app_name = "order"

urlpatterns = [

    path("order/", views.ShopCartView, name="shopcart"),
    path("shipping/", views.ShippingView, name="shipping"),
    path("complete/<int:id>/", views.CompleteView, name="complete"),
    path("update-profile/<int:order_id>/", views.UpdateAppuserView, name="update_appuser"),

    path("dashboard/<int:id>/", views.DashboardView, name="dashboard"),
    #path("<str:app_user>/", views.URLProfileView, name="profile"),
    path("confirm/", views.ConfirmView, name="confirm"),

]