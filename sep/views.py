from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from sep.models import EventRequestApplication, SubteamTask


# Application
class EventRequestApplicationFormMixin(object):
    model = EventRequestApplication
    template_name = 'sep/form.html'
    success_url = '/sep/applications'
    fields = '__all__'


class EventRequestApplicationUpdate(EventRequestApplicationFormMixin, UpdateView):
    pass


class EventRequestApplicationCreate(EventRequestApplicationFormMixin, CreateView):
    pass


class EventRequestApplicationList(ListView):
    model = EventRequestApplication
    template_name = 'sep/list_application.html'


# Subteam tasks
class SubteamTaskFormMixin(object):
    model = SubteamTask
    template_name = 'sep/form.html'
    success_url = '/sep/tasks'
    fields = '__all__'


class SubteamTaskUpdate(SubteamTaskFormMixin, UpdateView):
    pass


class SubteamTaskCreate(SubteamTaskFormMixin, CreateView):
    pass


class SubteamTaskList(ListView):
    model = SubteamTask
    template_name = 'sep/list_subteam_tasks.html'
