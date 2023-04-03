from django.db import models
class responseForm(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField(max_length=50)
    # docs=models.FileField(null=True, upload_to="docs/", max_length=250,default=None)
    desc=models.TextField()

# Create your models here.
