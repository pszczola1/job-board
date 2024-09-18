from django.urls import path
from . import views

urlpatterns = [
    path("create-listing/", views.create_listing, name="create listing"),
    path("listings/", views.listings, name="listings"),
    path("listing/<str:pk>", views.listing)
]
