# Generated by Django 3.2.4 on 2022-06-23 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='../static/images/profile-pics/user-default.png', null=True, upload_to='profile-pics/'),
        ),
    ]
