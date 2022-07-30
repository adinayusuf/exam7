from django.urls import path

from webapp.views.polls import ListPollView, CreatePollView, DetailPollView, UpdatePollView, PollDeleteView

urlpatterns = [
    path('', ListPollView.as_view(), name='view_poll'),
    path('poll/create/', CreatePollView.as_view(), name='create_poll'),
    path('poll/detail/<int:pk>/', DetailPollView.as_view(), name='detail_poll'),
    path('poll/update/<int:pk>/', UpdatePollView.as_view(), name='update_poll'),
    path('poll/delete/<int:pk>/', PollDeleteView.as_view(), name='delete_poll'),

]
