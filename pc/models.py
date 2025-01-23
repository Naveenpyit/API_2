from django.db import models

class product(models.Model):
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=30)
    price=models.IntegerField()
    quantity=models.IntegerField()

    class Meta:
        db_table='products'


    
