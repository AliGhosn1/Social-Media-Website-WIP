# Generated by Django 4.1.3 on 2022-11-24 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.TextField(blank=True),
        ),
    ]
