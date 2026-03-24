from django.contrib import admin
from .models import Monster

@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    ## Added 'created_at' and 'slug' to the display
    list_display = ('name', 'category', 'danger_level', 'created_at')

    # Keep your filters
    list_filter = ('category', 'danger_level')

    # Added 'weakness_sign' and 'oil_type' to search since we split the fields
    search_fields = ('name', 'description', 'weakness_sign', 'oil_type')

    list_display_links = ('name',)

    # ⚔️ WITCHER TRICK: This automatically fills the slug as you type the name
    # e.g. Typing "Foglet" automatically fills "foglet" in the slug field
    prepopulated_fields = {'slug': ('name',)}