from django.contrib import admin
from .models import *


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand')
    list_display_links = ('id', 'brand')
    search_fields = ('brand',)
    prepopulated_fields = {'slug': ('brand',)}


@admin.register(Drive)
class DriveAdmin(admin.ModelAdmin):
    list_display = ('id', 'drive')
    list_display_links = ('id', 'drive')
    search_fields = ('drive',)
    prepopulated_fields = {'slug': ('drive',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_display_links = ('id', 'category')
    search_fields = ('category',)
    prepopulated_fields = {'slug': ('category',)}


@admin.register(Transmission)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'transmission')
    list_display_links = ('id', 'transmission')
    search_fields = ('transmission',)
    prepopulated_fields = {'slug': ('transmission',)}


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model')
    list_display_links = ('id', 'brand', 'model')
    search_fields = ('model',)
    prepopulated_fields = {'slug': ('model',)}


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'brand', 'car_model', 'user', 'year', 'mileage', 'price', 'engine_size', 'created_date', 'category',
        'drive', 'transmission', 'published'
    )
    list_display_links = ('id', 'car_model', 'brand')

    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('published',)

    search_fields = ('model', 'year', 'mileage', 'price', 'engine_size', 'brand', 'category', 'drive', 'transmission',)
    list_filter = ('id', 'year', 'created_date', 'price', 'mileage', 'engine_size')


@admin.register(CarImage)
class ImageCarAdmin(admin.ModelAdmin):
    list_display = ('id', 'car')
    list_display_links = ('id', 'car')
    search_fields = ('car__model',)
