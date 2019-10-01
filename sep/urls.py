from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from sep import views

login_required(login_required(

urlpatterns = [
    path('applications/create', login_required(login_required(views.EventRequestApplicationCreate.as_view())), name='create_application'),
    path('applications', login_required(login_required(views.EventRequestApplicationList.as_view())), name="list_applications"),
    path('applications/<int:pk>/', login_required(login_required(views.EventRequestApplicationUpdate.as_view())), name="update_application"),

    path('tasks/create', login_required(login_required(views.SubteamTaskCreate.as_view())), name='create_task'),
    path('tasks', login_required(login_required(views.SubteamTaskList.as_view())), name='list_tasks'),
    path('tasks/<int:pk>', login_required(login_required(views.SubteamTaskUpdate.as_view())), name='update_task'),

    path('budget-requests/create', login_required(login_required(views.ExtraBudgetRequestCreate.as_view())), name='create_budget_request'),
    path('budget-requests', login_required(login_required(views.ExtraBudgetRequestList.as_view())), name='list_budget_request'),
    path('budget-requests/<int:pk>', login_required(login_required(views.ExtraBudgetRequestUpdate.as_view())), name='update_budget_request'),
]