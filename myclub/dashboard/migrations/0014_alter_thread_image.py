# Generated by Django 3.2.4 on 2021-06-25 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_alter_thread_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
