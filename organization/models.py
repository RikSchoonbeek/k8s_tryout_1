from django.db import models


class OrganizationalUnit(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=255)
    organisational_units = models.ManyToManyField(OrganizationalUnit, related_name='people')

    def __str__(self):
        return self.name
