from django.contrib import admin
from .models import SizePizza, Dough, Discount, Menu
# Register your models here.

admin.site.register(SizePizza)
admin.site.register(Dough)
admin.site.register(Discount)
admin.site.register(Menu)