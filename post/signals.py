from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CostumeUser, Profile, UserProfile


@receiver(post_save, sender=CostumeUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CostumeUser)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    instance.profile.save()

