from django.urls import path
from .views import EventsView, SignleEvent, EventForm

urlpatterns = [
    path('event', EventsView.as_view(), name='event/event_list'),
    path('event/<int:pk>/', SignleEvent.as_view(), name='event_detail'),
    path('create-event', EventForm.as_view(), name='event_form')
]
