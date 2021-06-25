from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title=models.CharField(default='',max_length=50)
    image=models.ImageField(upload_to='images/',default='')

    def __str__(self):
        return self.title