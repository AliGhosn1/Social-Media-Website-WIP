# Generated by Django 4.1.3 on 2022-11-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_siteusers_email_remove_siteusers_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteusers',
            name='picture',
            field=models.URLField(default='https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg', max_length=255),
            preserve_default=False,
        ),
    ]
