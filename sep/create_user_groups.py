from django.contrib.auth.models import Group, Permission, User
from django.contrib.auth import authenticate


# Step 1
customer_service_officer_group = Group.objects.get_or_create(name='customer_service_officer')[0]
senior_customer_service_officer_group = Group.objects.get_or_create(name='senior_customer_service_officer')[0]
financial_manager_group = Group.objects.get_or_create(name='financial_manager')[0]
administration_manager_group = Group.objects.get_or_create(name='administration_manager')[0]
hr_manager_group = Group.objects.get_or_create(name='hr_manager')[0]
staff_manager_group = Group.objects.get_or_create(name='staff_manager')[0]

# Step 2

try:
    customer_service_officer_1 = User.objects.create_user(
        username='customer_service_officer_1',
        password='abc123',
        is_staff=True
    )
except:
    customer_service_officer_1 = User.objects.get_or_create(
        username='customer_service_officer_1',
    )[0]

customer_service_officer_1.groups.add(customer_service_officer_group)
# customer_service_officer_group.user_set.add(customer_service_officer_1)

try:
    senior_customer_service_officer_1 = User.objects.create_user(
        username='senior_customer_service_officer_1',
        password='abc123',
        is_staff=True
    )
except:
    senior_customer_service_officer_1 = User.objects.get_or_create(
        username='senior_customer_service_officer_1',
    )[0]

senior_customer_service_officer_1.groups.add(senior_customer_service_officer_group)
# senior_customer_service_officer_group.user_set.add(senior_customer_service_officer_1)

try:
    financial_manager_1 = User.objects.create_user(
        username='financial_manager_1',
        password='abc123',
        is_staff=True
    )
except:
    financial_manager_1 = User.objects.get_or_create(
        username='financial_manager_1',
    )[0]

financial_manager_1.groups.add(financial_manager_group)
# financial_manager_group.user_set.add(financial_manager_1)

try:
    administration_manager_1 = User.objects.create_user(
        username='administration_manager_1',
        password='abc123',
        is_staff=True
    )
except:
    administration_manager_1 = User.objects.get_or_create(
        username='administration_manager_1',
    )[0]

administration_manager_1.groups.add(administration_manager_group)
# administration_manager_group.user_set.add(administration_manager_1)

try:
    hr_manager_1 = User.objects.create_user(
        username='hr_manager_1',
        password='abc123',
        is_staff=True
    )
except:
    hr_manager_1 = User.objects.get_or_create(
        username='hr_manager_1',
    )[0]

hr_manager_1.groups.add(hr_manager_group)
# hr_manager_group.user_set.add(hr_manager_1)

# user = authenticate(username=customer_service_officer_1, password="abc123")

# Step 3

add_event_request_application = Permission.objects.get_or_create(codename='add_eventrequestapplication')[0]
view_eventrequestapplication = Permission.objects.get_or_create(codename='view_eventrequestapplication')[0]
change_eventrequestapplication = Permission.objects.get_or_create(codename='change_eventrequestapplication')[0]

add_subteamtask = Permission.objects.get_or_create(codename='add_subteamtask')[0]
change_subteamtask = Permission.objects.get_or_create(codename='change_subteamtask')[0]
view_subteamtask = Permission.objects.get_or_create(codename='view_subteamtask')[0]

add_extrabudgetrequest = Permission.objects.get_or_create(codename='add_extrabudgetrequest')[0]
change_extrabudgetrequest = Permission.objects.get_or_create(codename='change_extrabudgetrequest')[0]
view_extrabudgetrequest = Permission.objects.get_or_create(codename='view_extrabudgetrequest')[0]

add_staffrequest = Permission.objects.get_or_create(codename='add_staffrequest')[0]
change_staffrequest = Permission.objects.get_or_create(codename='change_staffrequest')[0]
view_staffrequest = Permission.objects.get_or_create(codename='view_staffrequest')[0]

# ------

customer_service_officer_group.permissions.add(add_event_request_application)
customer_service_officer_group.permissions.add(view_eventrequestapplication)
customer_service_officer_group.permissions.add(change_eventrequestapplication)

senior_customer_service_officer_group.permissions.add(add_event_request_application)
senior_customer_service_officer_group.permissions.add(view_eventrequestapplication)
senior_customer_service_officer_group.permissions.add(change_eventrequestapplication)

financial_manager_group.permissions.add(view_eventrequestapplication)
financial_manager_group.permissions.add(change_eventrequestapplication)
financial_manager_group.permissions.add(view_extrabudgetrequest)
financial_manager_group.permissions.add(change_extrabudgetrequest)

administration_manager_group.permissions.add(view_eventrequestapplication)
administration_manager_group.permissions.add(change_eventrequestapplication)

hr_manager_group.permissions.add(change_staffrequest)
hr_manager_group.permissions.add(view_staffrequest)

staff_manager_group.permissions.add(add_staffrequest)
staff_manager_group.permissions.add(change_staffrequest)
staff_manager_group.permissions.add(view_staffrequest)

staff_manager_group.permissions.add(view_eventrequestapplication)
staff_manager_group.permissions.add(change_eventrequestapplication)

staff_manager_group.permissions.add(add_extrabudgetrequest)
staff_manager_group.permissions.add(change_extrabudgetrequest)
staff_manager_group.permissions.add(view_extrabudgetrequest)

staff_manager_group.permissions.add(add_subteamtask)
staff_manager_group.permissions.add(change_subteamtask)
staff_manager_group.permissions.add(view_subteamtask)


