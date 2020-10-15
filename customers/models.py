from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Customers(models.Model):
    def __str__(self):
        return self.customer_name

    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    email_regex = RegexValidator(
        regex=r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', message="Not a valid email")
    customer_email = models.CharField(max_length=100, validators=[
                                      email_regex], unique=True)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format +919999999999. Up to 10 digits allowed.")
    customer_phone = models.CharField('Phone', validators=[
        phone_regex], max_length=10, unique=True, null=True)

    customer_address = models.CharField(max_length=100)
    customer_credits = models.FloatField(max_length=200)
    customer_active = models.BooleanField(default=True)

    # remove bookmark
    # add function for creadit
    created_at = models.DateTimeField(auto_now_add=True)
    customer_referal = models.CharField(max_length=100, default='')
    # reg for number and email

    def __str__(self):
        return self.customer_name


class PhoneOTP(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format +919999999999. Up to 14 digits allowed.")
    phone = models.CharField(
        validators=[phone_regex], max_length=17, unique=True)
    otp = models.CharField(max_length=9, blank=True, null=True)
    count = models.IntegerField(default=0, help_text='Number of otp_sent')
    validated = models.BooleanField(
        default=False, help_text='If it is true, that means user have validate otp correctly in second API')
    otp_session_id = models.CharField(max_length=120, null=True, default="")
    username = models.CharField(
        max_length=20, blank=True, null=True, default=None)
    email = models.CharField(max_length=50, null=True,
                             blank=True, default=None)
    password = models.CharField(
        max_length=100, null=True, blank=True, default=None)

    def __str__(self):
        return str(self.phone) + ' is sent ' + str(self.otp)


class Vehicle(models.Model):
    def __str__(self):
        return self.vehicle_type+" "+self.vehicle_number

    vehicle_id = models.AutoField(primary_key=True)
    vehicle_customer = models.ForeignKey(
        Customers,  on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100)
    is_favourite = models.BooleanField(default=True)


class Host(models.Model):
    host_id = models.AutoField(primary_key=True)
    host_name = models.CharField(max_length=100)
    host_phone = models.IntegerField()
    host_address = models.CharField(max_length=100)
    host_credit = models.IntegerField()
    host_active = models.BooleanField(default=True)
    host_referal = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.host_name



class Socket(models.Model):
    def __str__(self):
        return self.socket_name
    socket_id = models.AutoField(primary_key=True)
    socket_name = models.CharField(max_length=100, default="")
    socket_image = models.ImageField(upload_to=None)
    socket_rating = models.IntegerField()


class Charger(models.Model):
    def __str__(self):
        return self.charger_name + str(self.charger_socket)

    charger_id = models.AutoField(primary_key=True)
    charger_name = models.CharField(max_length=100)
    charger_longitude = models.FloatField()
    charger_latitude = models.FloatField()
    charger_avaliability = models.IntegerField()
    charger_capacity = models.IntegerField()
    charger_rate = models.IntegerField()
    charger_socket = models.ForeignKey(
        Socket, on_delete=models.CASCADE)
    charger_socket_amt = models.IntegerField(default=0)
    charger_photos = models.ImageField(upload_to=None)
    charger_brand_logo = models.ImageField(upload_to=None)
    charger_host = models.ForeignKey(Host,
                                     on_delete=models.CASCADE)
    power_available = models.CharField(max_length=100, default='')
    Other_details = models.CharField(max_length=100, default='')


class Coupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    coupon_code = models.CharField(max_length=50, default='')
    valid_date = models.DateTimeField()
    customer_limit = models.IntegerField(default=0)
    open_to = [('All', 'All'), ('Nobody',
                                'Nobody'), ('selected_customer_type_only', 'Selected customer type only')]


class CreditType(models.Model):
    credit_name = models.CharField(max_length=100, default="")
    credit_amt = models.FloatField(default=0.0)


class Credit(models.Model):
    credit_id = models.AutoField(primary_key=True)
    credit_customer = models.ForeignKey(
        Customers, on_delete=models.CASCADE)
    credit_type = models.ForeignKey(
        CreditType, on_delete=models.CASCADE)
    # status: True means credit was increased, false means credit was decreased
    credit_status = models.BooleanField(default=True)


class Photo(models.Model):
    charger_photo = models.ImageField(upload_to=None)
    Charger_id = models.ForeignKey(
        Charger, on_delete=models.CASCADE)


class FavouriteCharger(models.Model):
    def __str__(self):
        return str(self.favourite_customer)

    favourite_ID = models.AutoField(primary_key=True)
    favourite_charger = models.ForeignKey(
        Charger, on_delete=models.CASCADE)
    favourite_customer = models.ForeignKey(
        Customers,  on_delete=models.CASCADE)


class Appointment(models.Model):
    def __str__(self):
        return "APP"+str(self.app_customer)+"/"+str(self.app_id)
    app_id = models.AutoField(primary_key=True)
    app_customer = models.ForeignKey(
        Customers, on_delete=models.CASCADE)
    app_charger = models.ForeignKey(
        Charger,  on_delete=models.CASCADE)
    app_date_time = models.DateTimeField(blank=True, null=True)
    app_create_date = models.DateField(auto_now_add=True)
    app_create_time = models.TimeField(auto_now_add=True)
    app_duration = models.FloatField(max_length=100)
    app_pay = models.FloatField(max_length=100)
    app_success = models.BooleanField(default=False)


class Bill_Details(models.Model):
    def __str__(self):
        return "BILL"+str(self.bill_id)

    bill_id = models.AutoField(primary_key=True)
    bill_date = models.DateField(auto_now_add=True)
    bill_time = models.TimeField(auto_now_add=True)
    bill_amount = models.FloatField(max_length=100)

    # function for amount

    bank_transaction = models.CharField(max_length=100, default="")
    coupon = models.ForeignKey(
        Coupon, on_delete=models.CASCADE)
    bill_ticket_number = models.IntegerField()
    bill_app = models.ForeignKey(
        Appointment, on_delete=models.CASCADE)


class SubAdmin(models.Model):
    subadmin = models.OneToOneField(
        User, on_delete=models.CASCADE, default=1)
    subadmin_email = models.CharField(max_length=100)
    subadmin_active = models.FloatField()

    def __str__(self):
        return self.subadmin.username


class SubAdminAccess(models.Model):
    access_id = models.AutoField(primary_key=True)
    edit_user = models.BooleanField(default=False)
    edit_host = models.BooleanField(default=False)
    edit_billdetails = models.BooleanField(default=False)
    edit_pumpdetails = models.BooleanField(default=False)
    edit_appointments = models.BooleanField(default=False)
    access_subadmin = models.ForeignKey(
        SubAdmin,   on_delete=models.CASCADE)


class BannerAds(models.Model):
    def __str__(self):
        return "ad"+self.banner_id
    banner_id = models.AutoField(primary_key=True)
    banner_subadmin_id = models.ForeignKey(
        SubAdmin, on_delete=models.CASCADE)
    file_path = models.FilePathField(default=None)


class SubscriptionType(models.Model):
    def __str__(self):
        return self.s_type+" Subscription"
    s_type_id = models.AutoField(primary_key=True)
    s_type = models.CharField(max_length=100)
    s_title = models.CharField(max_length=100)
    s_description = models.CharField(max_length=100)
    s_price_pm = models.IntegerField(default=0)


class Subscription(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    subscription_type = models.ForeignKey(
        SubscriptionType, on_delete=models.CASCADE)
    subscription_customer = models.ForeignKey(
        Customers, on_delete=models.CASCADE)
