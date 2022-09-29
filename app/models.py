from django.db import models
from django.utils import timezone


class Contact(models.Model):
    email = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    colors = models.TextField(blank=True, null=True)
    animal_list = models.TextField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'tbl_contact'