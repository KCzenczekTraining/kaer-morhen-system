from django.db import models

class Monster(models.Model):
    CATEGORIES = [
        ('NECROPHAGE', 'Necrophage'),
        ('RELICT', 'Relict'),
        ('HYBRID', 'Hybrid'),
        ('SPECTER', 'Specter'),
        ('CURSED', 'Cursed One'),  # Added for Werewolves/Udalryk quests
        ('DRACONID', 'Draconid'),   # Added for Wyverns/Basilisks
    ]

    # 1. Unique name prevents duplicate data entries
    name = models.CharField(max_length=100, unique=True)
    
    # 2. SlugField makes URL lookups easier for the Quest Service 
    # (e.g., /api/monsters/griffin instead of /api/monsters/1)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    
    category = models.CharField(max_length=20, choices=CATEGORIES)
    description = models.TextField()
    
    # 3. Separating tactical info helps the Quest service give "Witcher Tips"
    weakness_sign = models.CharField(max_length=50, blank=True) # e.g. "Yrden"
    oil_type = models.CharField(max_length=100, blank=True)    # e.g. "Specter Oil"
    
    # Keeping your original logic but adding a validator later
    danger_level = models.IntegerField(default=1) # 1-5 Skulls
    
    # 4. Timestamps for tracking new bestiary entries
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} [{self.category}]"
