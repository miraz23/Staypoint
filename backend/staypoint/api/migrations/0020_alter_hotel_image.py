# Generated by Django 5.1.5 on 2025-03-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_userdetails_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hotel_images/'),
        ),
    ]
