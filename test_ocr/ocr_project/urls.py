from django.urls import path
from . import views

urlpatterns = [
    path("", views.uploaded_image, name="image_request"),
]