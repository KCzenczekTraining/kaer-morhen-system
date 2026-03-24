from django.db import models

class Quest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    reward_gold = models.PositiveIntegerField(default=100)
    
    # This is the "Service Discovery" link. 
    # We store the ID of the monster from the Bestiary service.
    monster_id = models.IntegerField() 
    
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
