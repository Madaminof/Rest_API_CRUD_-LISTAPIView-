from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return f"{self.name} {self.id}"


class ProductCinema(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True,null=True)
    video = models.FileField(upload_to='videos/', blank=True)
    audio = models.FileField(upload_to='audio/', blank=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return f"{self.name} {self.id}"

