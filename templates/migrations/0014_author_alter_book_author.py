# Generated by Django 4.2.3 on 2024-02-05 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0013_alter_book_author_delete_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('bio', models.TextField(blank=True, max_length=250, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='author_photos/')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templates.author'),
        ),
    ]
