from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

staff_manager = Group.objects.get_or_create(name='staff_manager')[0]
# standard_app_users = Group.objects.get_or_create(name='production_manager')[0]
# group_staff_manager = Group.objects.get_or_create(name='service__manager')[0]
senior_customer_service_officer = Group.objects.get_or_create(name='senior_customer_service_officer')[0]
standard_app_users = Group.objects.get_or_create(name='administration_officer')[0]
standard_app_users = Group.objects.get_or_create(name='staff_manager')[0]
standard_app_users = Group.objects.get_or_create(name='staff_manager')[0]
standard_app_users = Group.objects.get_or_create(name='staff_manager')[0]

add_story = Permission.objects.get(codename='add_story')
add_pinpoint = Permission.objects.get(codename='add_pinpoint')
add_image = Permission.objects.get(codename='add_image')
add_audio = Permission.objects.get(codename='add_audio')

standard_app_users.permissions.add(add_story)
standard_app_users.permissions.add(add_pinpoint)
standard_app_users.permissions.add(add_image)
standard_app_users.permissions.add(add_audio)

story_content_typ = ContentType.objects.filter(app_label="storyline_app", model="story").first()
admin_story_permission = Permission(name="Can edit story permission", codename="change_story_object_permission", content_type=story_content_typ)
admin_story_permission.save()

# all_permissions_story = Permission.objects.filter(content_type__app_label='storyline_app', content_type__model='story')
# UserObjectPermission.objects.assign_perm('delete_story', user, obj=story)