# Generated by Django 5.0.3 on 2024-03-18 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='correct_answer',
        ),
        migrations.AddField(
            model_name='question',
            name='option5',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
