from django.contrib import admin
from .models import Place, PlaceImage

# This creates a form inside the Place page to upload multiple images at once
class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 3 # Shows 3 empty upload slots by default

class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]

admin.site.register(Place, PlaceAdmin)
