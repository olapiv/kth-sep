from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from sep import views

urlpatterns = [
    path('applications/create', views.EventRequestApplicationCreate.as_view(), name='create_application'),
    path('applications', views.EventRequestApplicationList.as_view(), name="list_applications"),
    path('applications/<int:pk>/', views.EventRequestApplicationUpdate.as_view(), name="update_application")
]