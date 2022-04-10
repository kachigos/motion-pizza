from django.contrib import admin
from .models import SizePizza, Dough, Discount, OrderMain, Pizza, Drinks, Food, Order, Combo, Category, CategorySushi, Stock, StockMain

class Orderinlini(admin.StackedInline):
    model = Order
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [Orderinlini]
    
    
class Stocklini(admin.StackedInline):
    model = StockMain
    extra = 0


class StockAdmin(admin.ModelAdmin):
    inlines = [Stocklini]


admin.site.register(SizePizza)
admin.site.register(Dough)
admin.site.register(Discount)
admin.site.register(Pizza)
admin.site.register(Drinks)
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Stock, StockAdmin)
admin.site.register(CategorySushi)
# admin.site.register(OrderMain, OrderAdmin)
admin.site.register(Combo, OrderAdmin)
