from django.contrib import admin
from .models import Delivery, Address, Payment


admin.site.register(Delivery)
admin.site.register(Address)
admin.site.register(Payment)