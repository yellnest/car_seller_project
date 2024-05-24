from rest_framework.routers import DefaultRouter
from src.car.views import *

router = DefaultRouter()

router.register(r'brand', BrandViewSet)
router.register(r'drive', DriveViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'transmission', TransmissionViewSet)
router.register(r'model-car', CarModelViewSet)
router.register(r'cars', CarViewSet)
router.register(r'image-car', CarImageViewSet)

urlpatterns = router.urls
