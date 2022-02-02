# Generated by Django 4.0 on 2021-12-20 23:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(default='anonymous', max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'myapp_image',
                'ordering': ['-created_on'],
            },
        ),
    ]
