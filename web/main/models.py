from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class ModelApi(models.Model):
    ApprovalDate = models.DateField()
    Term = models.IntegerField()
    NoEmp = models.IntegerField()
    FranchiseCode = models.CharField()
    Naics = models.CharField(null=True, blank=True)
    ApprovalFY = models.IntegerField()
    NewExist = models.CharField()
    LowDoc = models.CharField()
    GrAppv = models.IntegerField()
    CreateJob = models.IntegerField()
    RetainedJob = models.IntegerField()
    UrbanRural = models.CharField()
    RevLineCr = models.CharField()

