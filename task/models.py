from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    project = models.OneToOneField("project.Project", on_delete=models.CASCADE, related_name='task')
    assigned_to = models.ForeignKey("organization.Person", on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')

    def __str__(self):
        return self.name