# Generated by Django 5.1.6 on 2025-03-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assignments', '0002_assignment_image_alter_assignment_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='assignment_files/'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='assignments/'),
        ),
    ]
