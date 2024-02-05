from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    author = models.CharField(max_length=25)
    price = models.IntegerField()
    title = models.CharField(max_length=25)
    synopsis = models.TextField(max_length=250)
    category = models.CharField(max_length=25, default="general")
    cover = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    def __str__(self):
        return self.title
