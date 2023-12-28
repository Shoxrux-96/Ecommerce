from django.db import models

# Create your models here.
class Persons(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='media/profile')
    phoneNumber = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.first_name

class Products(models.Model):

    class Status(models.TextChoices):
        Active = 'AC','Active',
        Noactive = 'NA', 'Noactive',

    id = models.AutoField(primary_key=True)  # Add primary_key=True
    user = models.ForeignKey(Persons, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='media/products')
    price = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Noactive)

    def __str__(self):
        return self.name
