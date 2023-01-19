# Generated by Django 4.1.3 on 2023-01-16 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0031_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='userWhoPosted',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile1', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]