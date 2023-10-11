from django.db import models
from phone_field import PhoneField

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    # phone=PhoneField(blank=True, help_text='Contact phone number')
    phone=models.CharField(max_length=250)
    mail=models.EmailField(max_length=254)
    address=models.CharField(max_length=250)
    dep=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    purpose=models.CharField(max_length=100)
    pen=models.CharField(max_length=10,default=False,null=True)
    paper=models.CharField(max_length=10,default=False,null=True)

    def __str__(self):
        return self.name