# Generated by Django 3.2.5 on 2022-02-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.FileField(blank=True, upload_to='post_image'),
        ),
    ]
