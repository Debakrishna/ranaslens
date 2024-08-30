# Generated by Django 5.0.7 on 2024-07-21 07:43

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
                ('title', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='my_image')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
