# Generated by Django 5.0.3 on 2024-03-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_testresult_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]