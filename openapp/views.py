from django.views.generic import ListView,DetailView
from .models import Events
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import EventForm
from django.utils import timezone
# Create your views here.

class EventsView(ListView):
    model = Events
    template_name = "openapp/events.html"
    context_object_name = "events"
class SignleEvent(DetailView):
    template_name = "openapp/single_event.html"
    model = Events
    context_object_name = "event"
class EventForm(CreateView):
    model = Events
    form_class = EventForm
    template_name = "openapp/event_form.html"
    success_url = "/"
