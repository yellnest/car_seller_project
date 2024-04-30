from datetime import date

from django.contrib.auth.models import User
from django.db import models

from src.car.base.servieces import car_image_path


class Brand(models.Model):
    """Модель бренда автомобиля
    """
    brand = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Бренд авто'
        verbose_name_plural = 'Бренды авто'


class Drive(models.Model):
    """Модель привода автомобиля
    """
    drive = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.drive

    class Meta:
        verbose_name = 'Привод авто'
        verbose_name_plural = 'Привод авто'


class Category(models.Model):
    """Модель категории автомобиля
    """
    category = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория авто'
        verbose_name_plural = 'Категории авто'


class Transmission(models.Model):
    """Модель коробки передач
    """
    transmission = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.transmission

    class Meta:
        verbose_name = 'Коробка передач'
        verbose_name_plural = 'Коробки передач'
        

class CarModel(models.Model):
    """Модель коробки передач
    """
    model = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='model_brand')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Модель авто'
        verbose_name_plural = 'Модели авто'


class Car(models.Model):
    """Модель автомобиля
    """
    YEAR_CHOICES = [(r, r) for r in range(1970, date.today().year + 1)]

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=60)
    year = models.IntegerField(choices=YEAR_CHOICES)
    mileage = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    engine_size = models.DecimalField(max_digits=2, decimal_places=1)
    description = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cars')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='car_brands')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='car_categories')
    drive = models.ForeignKey(Drive, on_delete=models.CASCADE, related_name='car_drives')
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE, related_name='car_transmissions')
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='car_model')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class CarImage(models.Model):
    """Модель фотографий автомобиля
    """
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_images')
    image = models.ImageField(null=True, blank=True, upload_to=car_image_path)

    class Meta:
        verbose_name = 'Фотография авто'
        verbose_name_plural = 'Фотографии авто'
