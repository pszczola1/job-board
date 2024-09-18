from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'listings', views.ListingsViewset, basename="listings-api")
router.register(r'listing', views.ListingsViewset, basename="listing-api")

urlpatterns = [
    path(r'api/v1/', include(router.urls))
]
