from operator import mod
from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.

class FromFactry(models.Model):
    item = models.CharField('item', max_length=100)
    qty = models.IntegerField('qty')
    cost_price= MoneyField(max_digits=10,decimal_places=2,default_currency='USD')
    in_date = models.DateField()
    
    
    
    def __str__(self):
        return self.item
    
    
class Sales(models.Model):
    date = models.DateField()
    tiem = models.ForeignKey(FromFactry, on_delete=models.CASCADE)  
    qty =  models.ImageField('qty')
    price = MoneyField(max_digits=10,decimal_places=2,default_currency='USD')
  
    
    
    def __str__(self):
        return self.date
    
    
class StoreIn(models.Model):
    item = models.ForeignKey(FromFactry,on_delete=models.CASCADE)
    qty = models.IntegerField()
    total= models.IntegerField()
    
    def __str__(self):
        return self.total      
    
    
    