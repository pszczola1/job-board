from django.urls import path
from . import views

urlpatterns = [
    path("create-listing/", views.create_listing, name="create listing"),
    path("listing/<str:id>", views.listing)
]
