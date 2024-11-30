
from django.db import models

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('Telescopes', 'Telescopes'),
        ('Eyepieces', 'Eyepieces'),
        ('Miscellaneous', 'Miscellaneous'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='shop/items/', blank=False, null=False)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='Miscellaneous')
    stock = models.PositiveIntegerField(default=0) # Add category
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
