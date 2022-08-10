from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path 


urlpatterns = [
    path("", include("main.urls")),
    path('admin/', admin.site.urls),
    path("app/", include("app_user.urls")),
    path("card", include("card.urls")),
    path("order/", include("order.urls")),
    path("payment/", include("payment.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
