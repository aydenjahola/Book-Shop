# Generated by Django 4.2.3 on 2024-02-05 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0012_alter_author_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=25),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
