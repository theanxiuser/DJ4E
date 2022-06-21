from django.urls import path
from . views import MainView, CreateCats, UpdateCats, DeleteCats, ShowBreed, CreateBreed, UpdateBreed, DeleteBreed

app_name = "cats"
urlpatterns = [
    path("", MainView.as_view(), name="main_cats"),
    path("main/create/", CreateCats.as_view(), name="create_cats"),
    path("main/<int:pk>/update/", UpdateCats.as_view(), name="update_cats"),
    path("main/<int:pk>/delete/", DeleteCats.as_view(), name="delete_cats"),
    path("breed/", ShowBreed.as_view(), name="breed_list"),
    path("breed/create/", CreateBreed.as_view(), name="create_breed"),
    path("breed/<int:pk>/update/", UpdateBreed.as_view(), name="update_breed"),
    path("breed/<int:pk>/delete/", DeleteBreed.as_view(), name="delete_breed"),
]
