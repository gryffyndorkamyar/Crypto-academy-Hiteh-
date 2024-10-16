import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from django.contrib.auth.models import User
from post.models import Profile

for user in User.objects.all():
    Profile.objects.get_or_create(user=user)