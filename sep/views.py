from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from sep.models import EventRequestApplication


class EventRequestApplicationMixin(object):
    model = EventRequestApplication
    template_name = 'sep/application/form.html'
    success_url = '/sep/applications'
    fields = '__all__'


class EventRequestApplicationUpdate(EventRequestApplicationMixin, UpdateView):
    pass


class EventRequestApplicationCreate(EventRequestApplicationMixin, CreateView):
    pass


class EventRequestApplicationList(ListView):
    model = EventRequestApplication
    template_name = 'sep/application/list.html'
