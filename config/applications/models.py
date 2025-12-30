from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from jobs.models import Job

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.TextField()
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='pending')

    class Meta:
        unique_together = ['job', 'applicant']

    def __str__(self):
        return f"Application for {self.job.title}"