from django.db import models


class Topic(models.Model):
    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

    topic = models.CharField(verbose_name='Тема', max_length=100)

    def __str__(self):
        return self.topic


class City(models.Model):

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    city = models.CharField(verbose_name='Город', max_length=100)

    def __str__(self):
        return self.city


class Data(models.Model):
    phone_number = models.TextField(verbose_name='Номера телефонов')
    city = models.ForeignKey(City, verbose_name='Выберите город', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Опишите суть вопроса, ситуацию')
    topic = models.ForeignKey(Topic, verbose_name='Тема', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.phone_number


class About(models.Model):
    text_1 = models.TextField(verbose_name='Описание')
    img_1 = models.ImageField(verbose_name='Картинка', upload_to='image/food')
    text_2 = models.TextField(verbose_name='Описание', blank=True)
    img_2 = models.ImageField(verbose_name='Картинка', upload_to='image/food', blank=True)
    certificate = models.ImageField(verbose_name='сертификат', upload_to='image/document', blank=True)
    adress = models.CharField(verbose_name='Адрес', max_length=100)

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

