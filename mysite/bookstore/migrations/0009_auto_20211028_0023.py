# Generated by Django 2.2.12 on 2021-10-28 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0008_auto_20211028_0013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'programming book'},
        ),
        migrations.AlterField(
            model_name='book',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='display'),
        ),
    ]
