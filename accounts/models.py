from django.db import models


from django.contrib.auth.models import User
from .constants import ACC_TYPE,GENDER


# Create your models here.

class UserAccount(models.Model):
    user=models.OneToOneField(User,related_name="account",on_delete=models.CASCADE)
    account_type=models.CharField(max_length=10,choices=ACC_TYPE)
    account_no=models.IntegerField(unique=True)
    gender=models.CharField(max_length=10,choices=GENDER)
    birth_date=models.DateField(null=True,blank=True)
    initial_deposit_date=models.DateField(auto_now_add=True)
    balance=models.DecimalField(default=0,max_digits=12,decimal_places=2)
    
    def __str__(self):
        return f'{self.user.username} : {self.account_no}'
        # return str(self.account_no)
    
    
    
class UserAddress(models.Model):
    user=models.OneToOneField(User,related_name="address",on_delete=models.CASCADE)
    street_address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    postal_code=models.IntegerField()
    country=models.CharField(max_length=100)
    
    
    def __str__(self):
        return f'{self.user.username} : {self.city}'