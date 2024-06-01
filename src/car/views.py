from rest_framework import viewsets

from src.car.models import *
from src.car.serializers import BrandSerializer, DriveSerializer, CategorySerializer, TransmissionSerializer, \
    CarSerializer, CarImageSerializer, CarModelSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'slug'


class DriveViewSet(viewsets.ModelViewSet):
    queryset = Drive.objects.all()
    serializer_class = DriveSerializer
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class TransmissionViewSet(viewsets.ModelViewSet):
    queryset = Transmission.objects.all()
    lookup_field = 'slug'
    serializer_class = TransmissionSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.filter(published=True)
    serializer_class = CarSerializer
    lookup_field = 'slug'


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    lookup_field = 'slug'


class CarImageViewSet(viewsets.ModelViewSet):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
    lookup_field = 'id'
