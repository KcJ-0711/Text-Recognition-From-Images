# Generated by Django 4.1 on 2023-12-03 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr_project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]