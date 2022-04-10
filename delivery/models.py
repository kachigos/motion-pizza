from django.db import models


class Delivery(models.Model):
    recommendation = models.ForeignKey('Recommendation', on_delete=models.CASCADE, verbose_name='Рекомендация', blank=True, null=True)
    name = models.CharField(verbose_name='Имя', max_length=50)
    number = models.CharField(verbose_name='Номер телефона', max_length=15)
    address = models.IntegerField(verbose_name='Адрес')
    flat = models.IntegerField(verbose_name='Квартира', blank=True, null=True)
    entrance = models.IntegerField(verbose_name='Пподъезд', blank=True, null=True)
    floor = models.IntegerField(verbose_name='Этаж', blank=True, null=True)
    intercom = models.CharField(verbose_name='Домофон', max_length=10, blank=True, null=True)
    house = models.IntegerField(verbose_name='Дом', blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'
        
    
class Address(models.Model):
    boo = models.BooleanField()
    name = models.CharField(verbose_name='Адрес', max_length=50)
    address = models.CharField(verbose_name='Адрес для самовызова', max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адресы'
    
    
class Payment(models.Model):
    payment = models.IntegerField(verbose_name='Оплата')
    
    def __str__(self):
        return self.payment
    
    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
        
        
class Recommendation(models.Model):
    image = models.ImageField(verbose_name='Фото', upload_to='image/recommendation/')
    name = models.CharField(verbose_name='Название', max_length=50)
    price = models.IntegerField(verbose_name='Цена')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Рекомендация'
        verbose_name_plural = 'Рекомендации'