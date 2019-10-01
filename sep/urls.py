from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from sep import views

urlpatterns = [
    path('applications/create', views.EventRequestApplicationCreate.as_view(), name='create_application'),
    path('applications', views.EventRequestApplicationList.as_view(), name="list_applications"),
    path('applications/<int:pk>/', views.EventRequestApplicationUpdate.as_view(), name="update_application"),

    path('tasks/create', views.SubteamTaskCreate.as_view(), name='create_task'),
    path('tasks', views.SubteamTaskList.as_view(), name='list_tasks'),
    path('tasks/<int:pk>', views.SubteamTaskUpdate.as_view(), name='update_task'),

    path('budget-requests/create', views.ExtraBudgetRequestCreate.as_view(), name='create_budget_request'),
    path('budget-requests', views.ExtraBudgetRequestList.as_view(), name='list_budget_request'),
    path('budget-requests/<int:pk>', views.ExtraBudgetRequestUpdate.as_view(), name='update_budget_request'),

    path('staff-requests/create', views.StaffRequestCreate.as_view(), name='create_staff_request'),
    path('staff-requests', views.StaffRequestList.as_view(), name='list_staff_request'),
    path('staff-requests/<int:pk>', views.StaffRequestUpdate.as_view(), name='update_staff_request'),

]