# Generated by Django 4.2.3 on 2024-02-05 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0014_author_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='born',
            field=models.DateField(blank=True, null=True),
        ),
    ]