from django.db import models

# Create your models here.


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    bio = models.TextField(max_length=250, null=True, blank=True)
    born = models.DateField(null=True, blank=True)
    died = models.DateField(null=True, blank=True)
    photo = models.ImageField(
        upload_to='author_photos/', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.IntegerField()
    title = models.CharField(max_length=25)
    synopsis = models.TextField(max_length=250)
    category = models.CharField(max_length=25, default="general")
    cover = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
