# Generated by Django 3.2.4 on 2021-06-14 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
