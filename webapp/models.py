from django.db import models

# Create your models here.
class EngineeringExam(models.Model):
    name = models.CharField(max_length=100)
    purpose = models.TextField(max_length=150)
    eligibility = models.TextField(max_length=250)
    application_mode = models.CharField(max_length=20)
    source = models.CharField(max_length=150)
    minimum_percentage = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class MedicalExam(models.Model):
    name = models.CharField(max_length=100)
    purpose = models.TextField(max_length=150)
    eligibility = models.TextField(max_length=250)
    application_mode = models.CharField(max_length=20)
    source = models.CharField(max_length=150)
    minimum_percentage = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class DefNavArm(models.Model):
    name = models.CharField(max_length=100)
    purpose = models.TextField(max_length=150)
    eligibility = models.TextField(max_length=250)
    application_mode = models.CharField(max_length=20)
    source = models.CharField(max_length=150)
    minimum_percentage = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class AllExam(models.Model):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name