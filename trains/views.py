from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, DeleteView, UpdateView, CreateView)
from trains.models import Train
from trains.forms import TrainForm


__all__ = (
    'home',
    'TrainListView',
    'TrainDetailView',
    'TrainCreateView',
    'TrainUpdateView',
    'TrainDeleteView'
)


def home(request, pk=None):
    qs = Train.objects.all()
    context = {"qs":qs}
    return render(request, "trains/home.html", context)


class TrainListView(ListView):
    paginate_by = 5
    model = Train
    template_name = "trains/home.html"

class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'

class TrainCreateView(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Поезд успешно создан"


class TrainUpdateView(SuccessMessageMixin,LoginRequiredMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Поезд успешно отредактирован"


class TrainDeleteView(LoginRequiredMixin, DeleteView):
    model = Train
    success_url = reverse_lazy('trains:home')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.delete(request, *args, **kwargs)

