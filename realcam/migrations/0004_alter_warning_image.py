# Generated by Django 4.2 on 2023-06-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realcam', '0003_warning_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warning',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
