from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from sep import views

urlpatterns = [
    path('applications/create', staff_member_required(login_required(views.EventRequestApplicationCreate.as_view())), name='create_application'),
    path('applications', staff_member_required(login_required(views.EventRequestApplicationList.as_view())), name="list_applications"),
    path('applications/<int:pk>/', staff_member_required(login_required(views.EventRequestApplicationUpdate.as_view())), name="update_application")
]