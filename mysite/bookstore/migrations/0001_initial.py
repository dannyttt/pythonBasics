# Generated by Django 2.2.12 on 2021-10-27 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='title')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='price')),
            ],
        ),
    ]
