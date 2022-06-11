from django.urls import path
from . import views

# defining url path for polls app
urlpatterns = [
    path("", views.index, name="index"),
]