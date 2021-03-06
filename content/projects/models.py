from django.db import models
from content.staff.models import StaffMember

class Project(models.Model):
    title = models.CharField(max_length=127)
    summary = models.TextField()
    details = models.TextField()
    website = models.CharField(max_length=255, blank=True)
    staff = models.ManyToManyField(StaffMember, blank=True)
    image = models.ImageField(upload_to='project_pics', blank=True)

    def __str__(self):
        return self.title
