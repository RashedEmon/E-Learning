# Generated by Django 3.2.4 on 2021-06-26 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_topic_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
