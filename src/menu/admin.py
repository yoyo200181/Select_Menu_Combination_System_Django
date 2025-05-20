from django.contrib import admin
from .models import Menu

# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'kcal', 'protein', 'fat', 'carbs', 'fiber', 'salt', 'image_url', 'price', 'type', 'is_active')
    #search_fields = ('name',)
    list_filter = ('type', 'is_active')
