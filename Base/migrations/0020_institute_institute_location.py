# Generated by Django 4.1.7 on 2023-04-10 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0019_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='institute_location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
