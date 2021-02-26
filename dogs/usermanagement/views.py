from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from usermanagement.models import Dogs
from .forms import DogModelForm
from django.shortcuts import get_object_or_404


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
        print("the id",id_)
        obj = Dogs.objects.get(id=id_)
        print(obj.name)
        return obj