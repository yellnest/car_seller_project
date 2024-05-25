from rest_framework import serializers

from src.car.models import *


class BrandSerializer(serializers.ModelSerializer):
    brand_cars = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='car-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Brand
        fields = ('id', 'brand', 'slug', 'brand_cars')


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

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['brand'] = instance.brand.brand
        return rep


class CarSerializer(serializers.ModelSerializer):
    car_images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Car
        fields = (
            'id', 'title', 'slug', 'year', 'mileage', 'price', 'engine_size', 'description', 'published',
            'created_date', 'user', 'brand', 'car_model', 'category', 'drive', 'transmission', 'car_images'
        )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = instance.user.username  # Заменяем id пользователя на его имя
        rep['brand'] = instance.brand.brand  # Заменяем id бренда на его название
        rep['car_model'] = instance.car_model.model  # Заменяем id модели на её название
        rep['category'] = instance.category.category  # Заменяем id категории на её название
        rep['drive'] = instance.drive.drive  # Заменяем id привода на его название
        rep['transmission'] = instance.transmission.transmission  # Заменяем id коробки передач на её название
        return rep

    def validate(self, attrs):
        """
        Проверка на то что выбранная модель соответствует марке
        """
        brand = attrs['brand']
        car_model = attrs['car_model']

        if not car_model.brand == brand:
            raise serializers.ValidationError("Неверная комбинация марки и модели автомобиля.")

        return attrs


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ('id', 'image', 'car')
