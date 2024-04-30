from rest_framework.routers import DefaultRouter
from src.car.views import *

router = DefaultRouter()

router.register(r'brand', BrandViewSet)
router.register(r'drive', DriveViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'transmission', TransmissionViewSet)
router.register(r'car-model', CarModelViewSet)
router.register(r'car', CarViewSet)
router.register(r'car-image', CarImageViewSet)

urlpatterns = router.urls
