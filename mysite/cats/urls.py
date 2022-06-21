from django.urls import path
from . views import MainView, CreateCats, UpdateCats, DeleteCats

app_name = "cats"
urlpatterns = [
    path("", MainView.as_view(), name="main_cats"),
    path("main/create/", CreateCats.as_view(), name="create_cats"),
    path("main/<int:pk>/update/", UpdateCats.as_view(), name="update_cats"),
    path("main/<int:pk>/delete/", DeleteCats.as_view(), name="delete_cats"),
]
