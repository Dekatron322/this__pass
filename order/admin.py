
from django.contrib import admin
from order.models import ShopCart, Order, OrderProduct, CardInfo

# Register your models here.

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['card', 'app_user', 'quantity', 'price',]
    list_filter = ['app_user']

class OrderProductLine(admin.TabularInline):
	model = OrderProduct
	readonly_fields = ('app_user', 'card', 'price', 'quantity', 'status')
	can_delete = False
	extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'address', 'phone', 'city', 'total', 'status', 'code']
    list_filter = ['status']
    readonly_fields = ('app_user', 'first_name', 'last_name', 'phone', 'city', 'total', 'code')
    can_delete = False
    inlines = [OrderProductLine]

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['status', 'card', 'app_user', 'quantity', 'price', ]
    list_filter = ['app_user']



admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(CardInfo)
admin.site.register(OrderProduct, OrderProductAdmin)
