# Generated by Django 4.1.7 on 2023-04-03 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(default='category.jpg', upload_to='Category'),
        ),
    ]
