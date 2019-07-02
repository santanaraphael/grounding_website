from django.db import models

# Create your models here.
class GroundingMeshProject(models.Model):
    fault_current = models.FloatField()
    trip_time = models.FloatField()
    grid_depth = models.FloatField()
    grid_height = models.FloatField()
    grid_width = models.FloatField()
    ground_resistivity = models.FloatField()
    gravel_depth = models.FloatField()
    gravel_resistivity = models.FloatField()
    room_temperature = models.FloatField()
    maximum_temperature = models.FloatField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)