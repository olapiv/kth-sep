from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from sep.models import EventRequestApplication, SubteamTask, ExtraBudgetRequest, StaffRequest
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def forbidden_handler(request, exception=None):
    from django.shortcuts import render
    return render(request, 'sep/403.html', status=403)


class RedirectAdminLoginMixin(LoginRequiredMixin):
    login_url = '/admin/login/?next=/admin/'


class HomeView(RedirectAdminLoginMixin, TemplateView):
    template_name = "sep/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


# Application
class EventRequestApplicationFormMixin(object):
    model = EventRequestApplication
    template_name = 'sep/form.html'
    success_url = '/sep/applications'
    fields = '__all__'


class EventRequestApplicationUpdate(RedirectAdminLoginMixin, PermissionRequiredMixin, EventRequestApplicationFormMixin, UpdateView):
    permission_required = 'sep.change_eventrequestapplication'


class EventRequestApplicationCreate(RedirectAdminLoginMixin, PermissionRequiredMixin, EventRequestApplicationFormMixin, CreateView):
    permission_required = 'sep.add_eventrequestapplication'


class EventRequestApplicationList(RedirectAdminLoginMixin, PermissionRequiredMixin, ListView):
    permission_required = 'sep.view_eventrequestapplication'
    model = EventRequestApplication
    template_name = 'sep/list_application.html'


# Subteam tasks
class SubteamTaskFormMixin(object):
    model = SubteamTask
    template_name = 'sep/form.html'
    success_url = '/sep/tasks'
    fields = '__all__'


class SubteamTaskUpdate(RedirectAdminLoginMixin, PermissionRequiredMixin, SubteamTaskFormMixin, UpdateView):
    permission_required = 'sep.change_subteamtask'


class SubteamTaskCreate(RedirectAdminLoginMixin, PermissionRequiredMixin, SubteamTaskFormMixin, CreateView):
    permission_required = 'sep.add_subteamtask'


class SubteamTaskList(RedirectAdminLoginMixin, PermissionRequiredMixin, ListView):
    permission_required = 'sep.view_subteamtask'
    model = SubteamTask
    template_name = 'sep/list_subteam_tasks.html'


# Extra budget request
class ExtraBudgetRequestFormMixin(object):
    model = ExtraBudgetRequest
    template_name = 'sep/form.html'
    success_url = '/sep/budget-requests'
    fields = '__all__'


class ExtraBudgetRequestUpdate(RedirectAdminLoginMixin, PermissionRequiredMixin, ExtraBudgetRequestFormMixin, UpdateView):
    permission_required = 'sep.change_extrabudgetrequest'


class ExtraBudgetRequestCreate(RedirectAdminLoginMixin, PermissionRequiredMixin, ExtraBudgetRequestFormMixin, CreateView):
    permission_required = 'sep.add_extrabudgetrequest'


class ExtraBudgetRequestList(RedirectAdminLoginMixin, PermissionRequiredMixin, ListView):
    permission_required = 'sep.view_extrabudgetrequest'
    model = ExtraBudgetRequest
    template_name = 'sep/list_extra_budget_request.html'


# Staff request
class StaffRequestFormMixin(object):
    model = StaffRequest
    template_name = 'sep/form.html'
    success_url = '/sep/staff-requests'
    fields = '__all__'


class StaffRequestUpdate(RedirectAdminLoginMixin, PermissionRequiredMixin, StaffRequestFormMixin, UpdateView):
    permission_required = 'sep.change_staffrequest'


class StaffRequestCreate(RedirectAdminLoginMixin, PermissionRequiredMixin, StaffRequestFormMixin, CreateView):
    permission_required = 'sep.add_staffrequest'


class StaffRequestList(RedirectAdminLoginMixin, PermissionRequiredMixin, ListView):
    permission_required = 'sep.view_staffrequest'
    model = StaffRequest
    template_name = 'sep/list_staff_request.html'