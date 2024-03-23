from django.db import models

class Company(models.Model):
    id=models.SmallIntegerField(primary_key=True,unique=True)
    title=models.CharField(max_length=32)
    description=models.TextField()
    location=models.CharField(max_length=128)
    logo = models.ImageField(upload_to='images/', blank=True, null=True)
    timetable = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.title} - {self.id}'

class Product(models.Model):
    title=models.CharField(max_length=32)
    description=models.TextField()
    price=models.PositiveIntegerField(default=0)
    stock=models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    company=models.ForeignKey(to=Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

