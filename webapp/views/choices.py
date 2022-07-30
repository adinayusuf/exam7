from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import UpdateView, DeleteView, CreateView

from webapp.forms import ChoiceForm
from webapp.models import Choice, Poll


class CreateChoiceView(CreateView):
    model = Choice
    template_name = 'polls/detail_view.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get("pk"))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        return redirect("detail_poll", pk=poll.pk)


class ChoiceUpdateView(UpdateView):
    form_class = ChoiceForm
    template_name = 'choices/update_choices.html'
    model = Choice

    def get_success_url(self):
        return reverse("detail_poll", kwargs={"pk": self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choices/delete_choices.html'

    def get_success_url(self):
        return reverse("detail_poll", kwargs={"pk": self.object.poll.pk})