from django.contrib.auth.models import Group, Permission, User
from django.contrib.auth import authenticate


# Step 1
customer_service_officer_group = Group.objects.get_or_create(name='customer_service_officer')[0]
senior_customer_service_officer_group = Group.objects.get_or_create(name='senior_customer_service_officer')[0]
financial_manager_group = Group.objects.get_or_create(name='financial_manager')[0]
administration_manager_group = Group.objects.get_or_create(name='administration_manager')[0]
hr_manager_group = Group.objects.get_or_create(name='hr_manager')[0]

add_event_request_application = Permission.objects.get_or_create(codename='add_eventrequestapplication')[0]
customer_service_officer_group.permissions.add(add_event_request_application)

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
customer_service_officer_group.user_set.add(customer_service_officer_1)

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
    
senior_customer_service_officer_group.user_set.add(senior_customer_service_officer_1)

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

financial_manager_group.user_set.add(financial_manager_1)

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

administration_manager_group.user_set.add(administration_manager_1)

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

hr_manager_group.user_set.add(hr_manager_1)

# user = authenticate(username=customer_service_officer_1, password="abc123")

# Step 3

