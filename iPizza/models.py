from django.db import models


class SizePizza(models.Model):
    size = models.CharField(verbose_name='Размер пиццы', max_length=50)
    
    def __str__(self):
        return self.size
    
    
class Dough(models.Model):
    dough = models.CharField(verbose_name='Тип пиццы', max_length=30)
    
    def __str__(self):
        return self.dough
    
    
class Discount(models.Model):
    discount = models.CharField(verbose_name='Скидка', max_length=10)
    
    def __str__(self):
        return self.discount
    

class Pizza(models.Model):
    is_new = models.BooleanField(default=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(verbose_name='Фотография', upload_to='imange/food/')
    name = models.CharField(verbose_name='Название', max_length=30)
    description = models.TextField(verbose_name='Описание')
    size = models.ForeignKey(SizePizza, on_delete=models.CASCADE)
    dough = models.ForeignKey(Dough, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена') 
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'
        
        
class Drinks(models.Model):
    image = models.ImageField(verbose_name='Фотография', upload_to='imange/drinks/')
    name = models.CharField(verbose_name='Название', max_length=30)
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена') 
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
        
class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    drinks = models.ForeignKey(Drinks, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.pizza
    