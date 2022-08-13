from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save 
from django.dispatch import receiver


class Profile(models.Model):
    jango_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    skill = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.jango_user)


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(jango_user=instance)
        print('profile created !')

# here receiver is create_profile   and  sender is User---------------
post_save.connect(create_profile, sender=User)


def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('updated')

post_save.connect(update_profile, sender=User)


# -------------------  OR ---------------------- both are correct.....


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('updated')



