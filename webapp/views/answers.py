from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import ListView, TemplateView

from webapp.models import Answer, Poll


class AnswerListView(ListView):
    model = Answer
    context_object_name = 'answers'
    template_name = 'answers/answers_list.html'


class AnswerCreateView(TemplateView):

    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        return render(request, "answers/answer.html", {"poll": poll})

    def post(self, request, *args, **kwargs):
        choice_id = request.POST.get("answer")
        poll_id = self.kwargs.get('pk')
        Answer.objects.create(poll_id=poll_id, choice_id=choice_id)
        return redirect("answer_list")
