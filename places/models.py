from django.db import models

class Place(models.Model):
    CATEGORY_CHOICES = [
        ('RELIGIOUS', 'Religious'),
        ('NATURE', 'Nature'),
        ('HERITAGE', 'Heritage'),
        ('CULTURAL', 'Cultural'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    opening_time = models.CharField(max_length=100) 
    distance = models.DecimalField(max_digits=5, decimal_places=1) 
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(upload_to='places/', blank=True, null=True)
    travel_tips = models.TextField(blank=True, null=True, help_text="e.g., Bring cash, best time to visit, etc.")

    def __str__(self):
        return self.name


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='places/gallery/')
    caption = models.CharField(max_length=150, blank=True, help_text="Optional short caption for this photo")

    def __str__(self):
        return f"Photo for {self.place.name}"