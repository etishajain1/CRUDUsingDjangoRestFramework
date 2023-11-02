from django.db import models

class Studdb(models.Model):
    sid=models.PositiveIntegerField(max_length=10,primary_key=True)
    name=models.CharField(max_length=100,)
    phone=models.IntegerField()
    email=models.EmailField(max_length=100)
    passing_year=models.IntegerField(max_length=4)
    finishing_date=models.DateField()
    age=models.IntegerField(max_length=3)
    address=models.CharField(max_length=100)
