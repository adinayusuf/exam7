from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PollForm, ChoiceForm
from webapp.models import Poll


class ListPollView(ListView):
    model = Poll
    context_object_name = 'polls'
    template_name = 'polls/view.html'
    paginate_by = 5
    ordering = '-created_at'


class DetailPollView(DetailView):
    template_name = 'polls/detail_view.html'
    model = Poll

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['object'] = self.object
            choices = self.object.choices.all()
            context['choices'] = choices
            context['form'] = ChoiceForm()
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        return super().get_context_data(**context)


class CreatePollView(CreateView):
    form_class = PollForm
    template_name = 'polls/create.html'
    model = Poll

    def get_success_url(self):
        return reverse("detail_poll", kwargs={"pk": self.object.pk})


class UpdatePollView(UpdateView):
    form_class = PollForm
    template_name = 'polls/update.html'
    model = Poll

    def get_success_url(self):
        return reverse("detail_poll", kwargs={"pk": self.object.pk})


class PollDeleteView(DeleteView):
    model = Poll
    template_name = 'polls/delete.html'

    def get_success_url(self):
        return reverse("view_poll")
