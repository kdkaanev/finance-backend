from django.contrib.auth.views import UserModel
from django.db.models.signals import post_save
from django.dispatch import receiver

from backend.user.models import Profile


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if not created:
        return
    Profile.objects.create(user=instance)
