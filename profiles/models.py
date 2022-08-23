from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    display_name = models.CharField(max_length=40, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(
        blank_label='Country',
        null=True, blank=True,
        default='GB')
    email_address = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_display_name(self):
        return self.display_name

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
