# Generated by Django 3.2.4 on 2021-06-27 11:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_subject_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Post')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
