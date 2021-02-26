from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from usermanagement.models import Dogs
from .forms import DogModelForm
from django.urls import reverse

class HomeView(ListView):
    template_name = "home.html"
    queryset = Dogs.objects.all()


class AddDog(CreateView):
    form_class = DogModelForm
    template_name = "addDog.html"
    queryset = Dogs.objects.all()


class UpdateDog(UpdateView):
    form_class = DogModelForm
    template_name = "addDog.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        obj = Dogs.objects.get(id=id_)
        print(obj.name)
        return obj


class DeleteDog(DeleteView):
    template_name = "deleteDog.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        obj = Dogs.objects.get(id=id_)
        return obj

    def get_success_url(self):
        return reverse("home-view")