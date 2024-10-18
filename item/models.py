from django.contrib.auth.models import User
from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=255)

#     class Meta:
#         ordering = ('name',)
#         verbose_name_plural = 'Categories'
    
#     def __str__(self):
#         return self.name

CATEGORY_CHOICES = (
    ('books', 'Books'),
    ('stationary', 'Stationary'),
    ('tech_stuff', 'Tech Stuff'),
    ('gate_material', 'Gate Material'),
    ('others', 'Others'),
)

class Item(models.Model):
    category = models.CharField(max_length=20, choices = CATEGORY_CHOICES )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name