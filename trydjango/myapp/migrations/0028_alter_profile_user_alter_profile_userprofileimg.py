# Generated by Django 4.1.3 on 2023-01-16 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0027_alter_profile_userprofileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='userProfileImg',
            field=models.ImageField(blank=True, default='/blankpfp.jpg', null=True, upload_to=''),
        ),
    ]