from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subprojects')
    assigned_to = models.ForeignKey("organization.Person", on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_projects')

    def __str__(self):
        return self.name
