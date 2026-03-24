from django.contrib import admin
from .models import Monster

@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    # 'category' matches your model field
    # We removed 'created_at' because it's not in your model
    list_display = ('name', 'category', 'danger_level')

    # This adds the filter sidebar using the CATEGORIES choices
    list_filter = ('category', 'danger_level')

    # This allows you to search by name or weakness
    search_fields = ('name', 'description', 'weakness')

    list_display_links = ('name',)
