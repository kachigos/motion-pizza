from django.db import models
 

class SizePizza(models.Model):
    size = models.CharField(verbose_name='Размер пиццы', max_length=50)
    
    def __str__(self):
        return self.size
    
    class Meta:
        verbose_name = 'Размер пиццы'
        verbose_name_plural = 'Размер пиццы'
    
    
class Dough(models.Model):
    dough = models.CharField(verbose_name='Тип пиццы', max_length=30)
    
    def __str__(self):
        return self.dough
    
    class Meta:
        verbose_name = 'Тип пиццы'
        verbose_name_plural = 'Тип пиццы'
    
    
class Discount(models.Model):
    discount = models.CharField(verbose_name='Скидка', max_length=10)
    
    def __str__(self):
        return self.discount
    
    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'
        

class OrderMain(models.Model):
    price = models.IntegerField(verbose_name='Цена', blank=True, null=True)
    
    def __str__(self):
        return self.price
       

class Pizza(models.Model):
    is_new = models.BooleanField(default=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(verbose_name='Фотография', upload_to='image/pizza/')
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
        
        
class CategorySushi(models.Model):
    name = models.CharField(verbose_name='Категороя Суши', max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория суши'
        verbose_name_plural = 'Категория суши'  
        
        
class Category(models.Model):
    name = models.CharField(verbose_name='Категороя Food', max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
        
class Food(models.Model):                         # Для разных Блюд
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_sushi = models.ForeignKey(CategorySushi, on_delete=models.CASCADE, blank=True, null=True)
    is_new = models.BooleanField(default=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(verbose_name='Фотография', upload_to='image/food/')
    name = models.CharField(verbose_name='Название', max_length=30)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    price = models.IntegerField(verbose_name='Цена')  
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Еда'
        verbose_name_plural = 'Еда' 
        
        
class Drinks(models.Model):
    image = models.ImageField(verbose_name='Фотография', upload_to='image/drinks/')
    name = models.CharField(verbose_name='Название', max_length=30)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    price = models.IntegerField(verbose_name='Цена') 
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'
        
        
class Combo(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Комбо'
        verbose_name_plural = 'Комбо'
        
        
class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, blank=True, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, blank=True, null=True)
    drinks = models.ForeignKey(Drinks, on_delete=models.CASCADE, blank=True, null=True)
    ordermain = models.ForeignKey(OrderMain, on_delete=models.CASCADE, verbose_name='Заказ', blank=True, null=True)
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE, verbose_name='Комбо', blank=True, null=True)
      
    def __str__(self):
        return f'{self.pizza}'f'{self.food}'f'{self.drinks}'f'{self.ordermain}'f'{self.combo}'
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        
        
class Stock(models.Model):
    name = models.CharField(verbose_name='Название акции', max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
        
        
class StockMain(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, blank=True, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, blank=True, null=True)
    drinks = models.ForeignKey(Drinks, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.stock}'f'{self.pizza}'f'{self.food}'f'{self.drinks}'
    
    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'