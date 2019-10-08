from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from sep.models import EventRequestApplication, SubteamTask, ExtraBudgetRequest, StaffRequest
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.base import RedirectView
from django.contrib.auth import logout
from django.forms import ModelForm
from django.urls import reverse_lazy


def forbidden_handler(request, exception=None):
    from django.shortcuts import render
    return render(request, 'sep/403.html', status=403)


class RedirectAdminLoginMixin(LoginRequiredMixin):
    # login_url = reverse_lazy('login')
    login_url = '/admin/login/?next=/admin/'


class HomeView(RedirectAdminLoginMixin, TemplateView):
    template_name = "sep/home.html"
    

#######################
##### Application #####
#######################

class EventRequestApplicationForm(ModelForm):
    class Meta:
        model = EventRequestApplication
        exclude = ('user',)


class EventRequestApplicationCSOForm(ModelForm):
    class Meta:
        model = EventRequestApplication
        # exclude = ('user',)
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['approved_by_senior_customer_service_officer'].disabled = True
        self.fields['approved_by_financial_manager'].disabled = True
        self.fields['approved_by_admin_manager'].disabled = True
        self.fields['user'].disabled = True


class EventRequestApplicationSCSOForm(ModelForm):
    class Meta:
        model = EventRequestApplication
        # exclude = ('user',)
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['approved_by_financial_manager'].disabled = True
        self.fields['approved_by_admin_manager'].disabled = True
        self.fields['user'].disabled = True


class EventRequestApplicationAMForm(ModelForm):
    class Meta:
        model = EventRequestApplication
        # exclude = ('user',)
        exclude = ()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['approved_by_senior_customer_service_officer'].disabled = True
        self.fields['approved_by_financial_manager'].disabled = True
        self.fields['user'].disabled = True


class EventRequestApplicationFMForm(ModelForm):
    class Meta:
        model = EventRequestApplication
        # exclude = ('user',)
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['approved_by_senior_customer_service_officer'].disabled = True
        self.fields['approved_by_admin_manager'].disabled = True
        self.fields['user'].disabled = True


class EventRequestApplicationFormMixin(object):
    model = EventRequestApplication
    template_name = 'sep/form.html'
    success_url = '/sep/applications'

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser:
            return EventRequestApplicationForm
        elif user.groups.filter(name = "customer_service_officer").exists() or user.groups.filter(name = "staff_manager").exists():
            return EventRequestApplicationCSOForm
        elif user.groups.filter(name = "senior_customer_service_officer").exists():
            return EventRequestApplicationSCSOForm
        elif user.groups.filter(name = "administration_manager").exists():
            return EventRequestApplicationAMForm
        elif user.groups.filter(name = "financial_manager").exists():
            return EventRequestApplicationFMForm


class EventRequestApplicationUpdate(RedirectAdminLoginMixin, PermissionRequiredMixin, EventRequestApplicationFormMixin, UpdateView):
    permission_required = 'sep.change_eventrequestapplication'


class EventRequestApplicationCreate(RedirectAdminLoginMixin, PermissionRequiredMixin, EventRequestApplicationFormMixin, CreateView):
    permission_required = 'sep.add_eventrequestapplication'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Just for testing:
class EventRequestApplicationDetail(RedirectAdminLoginMixin, PermissionRequiredMixin, DetailView):
    model = EventRequestApplication
    permission_required = 'sep.view_eventrequestapplication'


class EventRequestApplicationList(RedirectAdminLoginMixin, PermissionRequiredMixin, ListView):
    permission_required = 'sep.view_eventrequestapplication'
    model = EventRequestApplication
    template_name = 'sep/list_application.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.groups.filter(name = "senior_customer_service_officer").exists() or user.groups.filter(name = "staff_manager").exists():
            return EventRequestApplication.objects.all()
        elif user.groups.filter(name = "customer_service_officer").exists():
            return EventRequestApplication.objects.filter(user=user).all()
        elif user.groups.filter(name = "administration_manager").exists():
            return EventRequestApplication.objects.filter(approved_by_senior_customer_service_officer=True).all()
        elif user.groups.filter(name = "financial_manager").exists():
            return EventRequestApplication.objects.filter(approved_by_senior_customer_service_officer=True, approved_by_admin_manager=True).all()


#######################
#### Subteam tasks ####
#######################

class SubteamTaskForm(ModelForm):
    class Meta:
        model = SubteamTask
        exclude = ('user',)


class SubteamTaskFormMixin(object):
    model = SubteamTask
    template_name = 'sep/form.html'
    success_url = '/sep/tasks'


class SubteamTaskUpdate(RedirectAdminLoginMixin, PermissionRequiredMixin, SubteamTaskFormMixin, UpdateView):
    permission_required = 'sep.change_subteamtask'
    form_class = SubteamTaskForm


class SubteamTaskCreate(RedirectAdminLoginMixin, PermissionRequiredMixin, SubteamTaskFormMixin, CreateView):
    permission_required = 'sep.add_subteamtask'
    form_class = SubteamTaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SubteamTaskList(RedirectAdminLoginMixin, PermissionRequiredMixin, ListView):
    permission_required = 'sep.view_subteamtask'
    model = SubteamTask
    template_name = 'sep/list_subteam_tasks.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return SubteamTask.objects.all()
        else:
            return SubteamTask.objects.filter(user=user).all()


##############################
#### Extra budget request ####
##############################

class ExtraBudgetRequestForm(ModelForm):
    class Meta:
        model = ExtraBudgetRequest
        exclude = ('user',)


class ExtraBudgetRequestFormMixin(object):
    model = ExtraBudgetRequest
    template_name = 'sep/form.html'
    success_url = '/sep/budget-requests'


class ExtraBudgetRequestUpdate(RedirectAdminLoginMixin, PermissionRequiredMixin, ExtraBudgetRequestFormMixin, UpdateView):
    permission_required = 'sep.change_extrabudgetrequest'
    form_class = ExtraBudgetRequestForm


class ExtraBudgetRequestCreate(RedirectAdminLoginMixin, PermissionRequiredMixin, ExtraBudgetRequestFormMixin, CreateView):
    permission_required = 'sep.add_extrabudgetrequest'
    form_class = ExtraBudgetRequestForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExtraBudgetRequestList(RedirectAdminLoginMixin, PermissionRequiredMixin, ListView):
    permission_required = 'sep.view_extrabudgetrequest'
    template_name = 'sep/list_extra_budget_request.html'

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name = "financial_manager").exists() or user.is_superuser:
            return ExtraBudgetRequest.objects.all()
        else:
            return ExtraBudgetRequest.objects.filter(user=user).all()


#########################
##### Staff request #####
#########################


class StaffRequestForm(ModelForm):
    class Meta:
        model = StaffRequest
        exclude = ('user',)


class StaffRequestFormMixin(object):
    model = StaffRequest
    template_name = 'sep/form.html'
    success_url = '/sep/staff-requests'


class StaffRequestUpdate(RedirectAdminLoginMixin, PermissionRequiredMixin, StaffRequestFormMixin, UpdateView):
    permission_required = 'sep.change_staffrequest'
    form_class = StaffRequestForm


class StaffRequestCreate(RedirectAdminLoginMixin, PermissionRequiredMixin, StaffRequestFormMixin, CreateView):
    permission_required = 'sep.add_staffrequest'
    form_class = StaffRequestForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class StaffRequestList(RedirectAdminLoginMixin, PermissionRequiredMixin, ListView):
    permission_required = 'sep.view_staffrequest'
    template_name = 'sep/list_staff_request.html'

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name = "hr_manager").exists() or user.is_superuser:
            return StaffRequest.objects.all()
        else:
            return StaffRequest.objects.filter(user=user).all()
