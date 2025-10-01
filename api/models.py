from django.db import models

# Create your models here.
class Alert(models.Model):
    tourist_id = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)
    alert_type = models.CharField(max_length=50, default="EmergencyButton")


    def __str__(self):
        return self.name

# models.py
class Tourist(models.Model):
    tourist_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    user_type = models.CharField(max_length=20, default="tourist")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name or 'Anonymous'} ({self.tourist_id})"
