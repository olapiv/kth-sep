from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from sep.models import EventRequestApplication, SubteamTask, ExtraBudgetRequest, StaffRequest


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


# Extra budget request
class ExtraBudgetRequestFormMixin(object):
    model = ExtraBudgetRequest
    template_name = 'sep/form.html'
    success_url = '/sep/budget-requests'
    fields = '__all__'


class ExtraBudgetRequestUpdate(ExtraBudgetRequestFormMixin, UpdateView):
    pass


class ExtraBudgetRequestCreate(ExtraBudgetRequestFormMixin, CreateView):
    pass


class ExtraBudgetRequestList(ListView):
    model = ExtraBudgetRequest
    template_name = 'sep/list_extra_budget_request.html'


# Staff request
class StaffRequestFormMixin(object):
    model = StaffRequest
    template_name = 'sep/form.html'
    success_url = '/sep/staff-requests'
    fields = '__all__'


class StaffRequestUpdate(StaffRequestFormMixin, UpdateView):
    pass


class StaffRequestCreate(StaffRequestFormMixin, CreateView):
    pass


class StaffRequestList(ListView):
    model = StaffRequest
    template_name = 'sep/list_staff_request.html'