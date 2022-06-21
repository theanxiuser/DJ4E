from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cat, Breed

# Create your views here.
class MainView(LoginRequiredMixin, View):
    def get(self, request):
        cat_all = Cat.objects.all()
        breed_c = Breed.objects.all().count()

        ctx = {"cat_list": cat_all, "breed_count":breed_c}
        return render(request, "cats/cat_list.html", ctx)

class CreateCats(LoginRequiredMixin, CreateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:main_cats")

class UpdateCats(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:main_cats")

class DeleteCats(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:main_cats")
