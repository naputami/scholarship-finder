from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

from core.models import BaseModel

class Scholarship(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    degree = ArrayField(models.CharField(max_length=100))
    deadline = models.DateField(blank=True, null=True)
    registration_start_date = models.DateField(blank=True, null=True)
    country = ArrayField(models.CharField(max_length=100))
    type = models.CharField(max_length=100)
    benefits = ArrayField(models.CharField(max_length=255))
    requirements = ArrayField(models.CharField(max_length=255))
    official_url = models.URLField(blank=True, null=True)
    source_url = models.URLField(unique=True, blank=True, null=True)
    must_relocate = models.BooleanField(default=False)
    study_format = models.CharField(max_length=100, blank=True, null=True)
    
    
class ScholarshipRecommendation(BaseModel):
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
