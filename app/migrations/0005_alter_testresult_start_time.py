# Generated by Django 5.0.3 on 2024-03-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_testresult_displayed_questions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]