from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from cities.forms import CityForm
from cities.models import City


__all__ = (
    "home",
    "CityDetailView",
    "CityCreateView",
    "CityUpdateView",
    "CityDeleteView",
    "CityListView",
)


def home(request, pk=None):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

    # if pk:
    #     # city = City.objects.get(id=pk)
    #     # city = get_object_or_404(City, id=pk)
    #     city = City.objects.filter(id=pk).first()
    #     context = {"object":city}
    #     return render(request, "cities/detail.html", context)

    form = CityForm()
    qs = City.objects.all()
    context = {"qs":qs, "form":form}
    return render(request, "cities/home.html", context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = "cities/detail.html"


class CityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно создан"


class CityUpdateView(SuccessMessageMixin,LoginRequiredMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно отредактирован"


class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    success_url = reverse_lazy('cities:home')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # messages.success(request, 'Город успешно удален')
        return self.delete(request, *args, **kwargs)


class CityListView(ListView):
    paginate_by = 2
    model = City
    template_name = "cities/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context['form'] = form
        return context

