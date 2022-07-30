from django.urls import path

from webapp.views.answers import AnswerListView, AnswerCreateView
from webapp.views.choices import CreateChoiceView, ChoiceDeleteView, ChoiceUpdateView
from webapp.views.polls import ListPollView, CreatePollView, DetailPollView, UpdatePollView, PollDeleteView

urlpatterns = [
    path('', ListPollView.as_view(), name='view_poll'),
    path('poll/create/', CreatePollView.as_view(), name='create_poll'),
    path('poll/detail/<int:pk>/', DetailPollView.as_view(), name='detail_poll'),
    path('poll/update/<int:pk>/', UpdatePollView.as_view(), name='update_poll'),
    path('poll/delete/<int:pk>/', PollDeleteView.as_view(), name='delete_poll'),

    path('poll/<int:pk>/choice_create/', CreateChoiceView.as_view(), name='choice_create'),
    path('poll/<int:pk>/choice/update/', ChoiceUpdateView.as_view(), name='choice_update'),
    path('poll/<int:pk>/choice/delete', ChoiceDeleteView.as_view(), name='choice_delete'),

    path('answer/list/', AnswerListView.as_view(), name='answer_list'),
    path('poll/<int:pk>/answer/', AnswerCreateView.as_view(), name='answer')
]
