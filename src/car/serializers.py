from rest_framework import serializers

from src.car.models import *


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'brand', 'slug')


class DriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drive
        fields = ('id', 'drive', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category', 'slug')


class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = ('id', 'transmission', 'slug')


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'model', 'slug', 'brand')


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id', 'title', 'slug', 'car_model', 'year', 'mileage', 'price', 'engine_size', 'description', 'published',
            'created_date', 'user', 'brand', 'category', 'drive', 'transmission'
        )


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ('id', 'image', 'car')
