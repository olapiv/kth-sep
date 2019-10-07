from django.test import TestCase
from django.contrib.auth.models import Group, Permission, User


# Create your tests here.

class PermissionsTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        import sep.create_user_groups

    def test_customer_service_officer(self):
        group = Group.objects.get(name='customer_service_officer')
        self.assertEqual(group.permissions.count(), 2)
        self.assertTrue(group.permissions.filter(codename="add_eventrequestapplication").exists())
        self.assertTrue(group.permissions.filter(codename="view_eventrequestapplication").exists())

    def test_senior_customer_service_officer(self):
        group = Group.objects.get(name='senior_customer_service_officer')
        self.assertEqual(group.permissions.count(), 3)
        self.assertTrue(group.permissions.filter(codename="add_eventrequestapplication").exists())
        self.assertTrue(group.permissions.filter(codename="view_eventrequestapplication").exists())
        self.assertTrue(group.permissions.filter(codename="change_eventrequestapplication").exists())

    def test_financial_manager(self):
        group = Group.objects.get(name='financial_manager')
        self.assertEqual(group.permissions.count(), 4)
        self.assertTrue(group.permissions.filter(codename="view_eventrequestapplication").exists())
        self.assertTrue(group.permissions.filter(codename="change_eventrequestapplication").exists())
        self.assertTrue(group.permissions.filter(codename="change_extrabudgetrequest").exists())
        self.assertTrue(group.permissions.filter(codename="view_extrabudgetrequest").exists())

    def test_hr_manager(self):
        group = Group.objects.get(name='hr_manager')
        self.assertEqual(group.permissions.count(), 2)
        self.assertTrue(group.permissions.filter(codename="change_staffrequest").exists())
        self.assertTrue(group.permissions.filter(codename="view_staffrequest").exists())

    def test_staff_manager(self):
        group = Group.objects.get(name='staff_manager')
        self.assertEqual(group.permissions.count(), 11)
        self.assertTrue(group.permissions.filter(codename="add_staffrequest").exists())
        self.assertTrue(group.permissions.filter(codename="change_staffrequest").exists())
        self.assertTrue(group.permissions.filter(codename="view_eventrequestapplication").exists())
        self.assertTrue(group.permissions.filter(codename="change_eventrequestapplication").exists())
        self.assertTrue(group.permissions.filter(codename="add_extrabudgetrequest").exists())
        self.assertTrue(group.permissions.filter(codename="change_extrabudgetrequest").exists())
        self.assertTrue(group.permissions.filter(codename="view_extrabudgetrequest").exists())
        self.assertTrue(group.permissions.filter(codename="add_subteamtask").exists())
        self.assertTrue(group.permissions.filter(codename="change_subteamtask").exists())
        self.assertTrue(group.permissions.filter(codename="view_extrabudgetrequest").exists())




