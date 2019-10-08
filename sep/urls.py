from django.urls import path
from sep import views


urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    # path('/logout', views.logout_view, name='logout'),

    path('applications/view/<int:pk>/', views.EventRequestApplicationDetail.as_view(), name='view_application'),
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