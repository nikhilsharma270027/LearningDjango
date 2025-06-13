from django.db import models
from django.utils import timezone
# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'Masala Chai'),
        ('GR', 'Ginger Chai'),
        ('CD', 'Cardamom Chai'),
        ('LM', 'Lemon Chai'),
        ('MK', 'Milk Chai'),
        ('BK', 'Black Chai'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default="")
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.name
    