# Generated by Django 4.0.6 on 2022-07-15 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_img',
            field=models.TextField(null=True),
        ),
    ]
