from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, User

# Create your models here.
class Pledge(models.Model):
    reg_number = models.CharField(max_length=100, blank=True)
    auth_token = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(blank=False)
    dob = models.DateField(blank=False)
    resident = models.CharField(max_length=150, blank=False)
    heart = models.BooleanField(default=False, null=True)
    lungs = models.BooleanField(default=False, null=True)
    kidneys = models.BooleanField(default=False, null=True)
    liver = models.BooleanField(default=False, null=True)
    pancreas = models.BooleanField(default=False, null=True)
    any_other_organ = models.CharField(max_length=100, blank=True)
    all_organs = models.BooleanField(default=False, null=True)
    blood_group = models.CharField(max_length=5, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    corneas_or_eye_balls = models.BooleanField(default=False, null=True)
    skin = models.BooleanField(default=False, null=True)
    bones = models.BooleanField(default=False, null=True)
    heart_valves = models.BooleanField(default=False, null=True)
    blood_vessels = models.BooleanField(default=False, null=True)
    any_other_tissue = models.CharField(max_length=100, blank=True)
    all_tissues = models.BooleanField(default=False, null=True)
    sign = models.ImageField(upload_to="pledger", blank=False)
    address = models.TextField(max_length=150, blank=False)
    tel_no = models.CharField(max_length=15, blank=False)
    email = models.EmailField(max_length=25, blank=False)
    date = models.DateField(blank=False)
    witness1_sign = models.ImageField(upload_to="pledger", blank=False)
    witness1_name = models.CharField(max_length=100, blank=False)
    witness1_age = models.IntegerField(blank=False)
    witness1_dob = models.DateField(blank=False)
    witness1_resident = models.CharField(max_length=150, blank=False)
    witness1_tel_no = models.CharField(max_length=15, blank=False)
    witness1_email = models.EmailField(max_length=100, blank=False)
    witness1_relation = models.CharField(max_length=100, blank=False)
    witness2_sign = models.ImageField(upload_to="pledger", blank=False)
    witness2_name = models.CharField(max_length=100, blank=False)
    witness2_age = models.IntegerField(blank=False)
    witness2_dob = models.DateField(blank=False)
    witness2_resident = models.CharField(max_length=150, blank=False)
    witness2_tel_no = models.CharField(max_length=15, blank=False)
    witness2_email = models.EmailField(max_length=100, blank=False)
    witness2_relation = models.CharField(max_length=100, blank=False)
    witness_dated = models.DateField(blank=False)
    witness_place = models.CharField(max_length=100, blank=False)
    is_verified = models.BooleanField(default=False)

    date_filled = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Donar_card(models.Model):
    name = models.ForeignKey(Pledge, on_delete=models.CASCADE, null=True)
    unique_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.unique_id
