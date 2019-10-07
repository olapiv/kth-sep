from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from sep import views


urlpatterns = [
    path('applications/create', staff_member_required(login_required(views.EventRequestApplicationCreate.as_view())), name='create_application'),
    path('applications', staff_member_required(login_required(views.EventRequestApplicationList.as_view())), name="list_applications"),
    path('applications/<int:pk>/', staff_member_required(login_required(views.EventRequestApplicationUpdate.as_view())), name="update_application"),

    path('tasks/create', staff_member_required(login_required(views.SubteamTaskCreate.as_view())), name='create_task'),
    path('tasks', staff_member_required(login_required(views.SubteamTaskList.as_view())), name='list_tasks'),
    path('tasks/<int:pk>', staff_member_required(login_required(views.SubteamTaskUpdate.as_view())), name='update_task'),

    path('budget-requests/create', staff_member_required(login_required(views.ExtraBudgetRequestCreate.as_view())), name='create_budget_request'),
    path('budget-requests', staff_member_required(login_required(views.ExtraBudgetRequestList.as_view())), name='list_budget_request'),
    path('budget-requests/<int:pk>', staff_member_required(login_required(views.ExtraBudgetRequestUpdate.as_view())), name='update_budget_request'),
    
    path('staff-requests/create', staff_member_required(login_required(views.StaffRequestCreate.as_view())), name='create_staff_request'),
    path('staff-requests', staff_member_required(login_required(views.StaffRequestList.as_view())), name='list_staff_request'),
    path('staff-requests/<int:pk>', staff_member_required(login_required(views.StaffRequestUpdate.as_view())), name='update_staff_request'),
]