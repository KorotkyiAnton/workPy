from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key_1c = models.CharField(max_length=500, blank=True)
    department_key = models.CharField(max_length=255, blank=True)
    position_key = models.CharField(max_length=255, blank=True)
    direction_key = models.CharField(max_length=255, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
