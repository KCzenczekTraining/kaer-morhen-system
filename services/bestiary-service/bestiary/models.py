from django.db import models

class Monster(models.Model):
    CATEGORIES = [
        ('NECROPHAGE', 'Necrophage'),
        ('RELICT', 'Relict'),
        ('HYBRID', 'Hybrid'),
        ('SPECTER', 'Specter'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    description = models.TextField()
    weakness = models.CharField(max_length=255)
    danger_level = models.IntegerField(default=1) # 1-5 Skulls

    def __str__(self):
        return self.name
