from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

class Contact(models.Model):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.phone

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Compensation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.SmallIntegerField(null=True)
    created = models.DateTimeField(default=timezone.now)
    work_experience = models.SmallIntegerField(default=0)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None)
    compensations = models.ManyToManyField(Compensation)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

from main_app.models import Product, Category
from django.db.models import Count, Max
from datetime import date
result = Product.objects.aggregate(gt_stock=Max('stock'))