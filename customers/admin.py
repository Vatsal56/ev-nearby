from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Customer, PhoneOTP, Vehicle, Host, Socket, Charger, Coupon, CreditType, Credit, Photo, FavouriteCharger, Appointment, Bill_Detail, BannerAd

admin.site.site_header = 'Charging Station Admin'

class HostAdmin(admin.ModelAdmin):
    list_display = ('host_id', 'host_name', 'host_active')
    list_filter = ('host_active',)
    search_fields = ('host_id', 'host_name', 'host_address')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name', 'customer_active')
    list_filter = ('customer_active',)
    search_fields = ('customer_id', 'customer_name', 'customer_address')

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id', 'vehicle_customer', 'vehicle_number', 'vehicle_type')
    list_filter = ('vehicle_type',)
    search_fields = ('vehicle_customer', 'vehicle_id', 'vehicle_type')

class SocketAdmin(admin.ModelAdmin):
    list_display = ('socket_id', 'socket_name')
    search_fields = ('socket_id', 'socket_name',)

class ChargerAdmin(admin.ModelAdmin):
    list_display = ('charger_id', 'charger_name', 'charger_avaliability', 'charger_capacity', 'charger_rate')
    list_filter = ('charger_capacity', 'charger_socket',)

class CouponAdmin(admin.ModelAdmin):
    list_display = ('coupon_id', 'customer_limit')
    list_filter = ('customer_limit',)

class FavouriteChargerAdmin(admin.ModelAdmin):
    list_display = ('favourite_ID', 'favourite_charger', 'favourite_customer')
    list_filter = ('favourite_ID', 'favourite_charger', 'favourite_customer',)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('app_id', 'app_customer', 'app_charger', 'app_date_time', 'app_duration', 'app_pay')
    search_fields = ('app_id', 'app_customer', 'app_charger',)
    list_filter = ('app_charger', 'app_date_time')

class Bill_DetailAdmin(admin.ModelAdmin):
    list_display = ('bill_id', 'bill_date', 'bill_time', 'bill_amount')
    search_fields = ('bill_id', 'bill_date',)
    list_filter = ('bill_date',)

class BannerAdAdmin(admin.ModelAdmin):
    list_display = ('banner_id', 'banner_subadmin_id')
    search_fields = ('banner_id', 'banner_subadmin_id',)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(PhoneOTP)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(Socket, SocketAdmin)
admin.site.register(Charger, ChargerAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(CreditType)
admin.site.register(Credit)
admin.site.register(Photo)
admin.site.register(FavouriteCharger, FavouriteChargerAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Bill_Detail, Bill_DetailAdmin)
admin.site.register(BannerAd, BannerAdAdmin)