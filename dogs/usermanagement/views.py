from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from usermanagement.models import Dogs
from .forms import DogModelForm


class HomeView(ListView):
    template_name = "home.html"
    queryset = Dogs.objects.all()



class AddDog(CreateView):
    form_class = DogModelForm
    template_name = "addDog.html"
    queryset = Dogs.objects.all()

