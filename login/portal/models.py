from django.db import models

class Usuario(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    Name = models.CharField(max_length=255)

# Create your models here.
