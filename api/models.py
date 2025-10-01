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