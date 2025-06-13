from django.db import models
from django.utils import timezone
# bydefault django has user model
from django.contrib.auth.models import User
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
    
    # this is called a dander method
    def __str__(self): 
        return self.name
    # what does the above line do?
    # it returns the name of the chai when we print the object
    
    
#one to many relationship
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField(default="")
    data_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} reviws for {self.chai.name}'
    
    
    # Many to many relationship
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    chai_varities = models.ManyToManyField(ChaiVarity, related_name='stores') # store ke naam se relation
    
    def __str__(self):
        return self.name
    
#  One to one relationship
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=50, unique=True)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()
    
    def __str__(self):
        return f'Certificate for {self.chai.name}'