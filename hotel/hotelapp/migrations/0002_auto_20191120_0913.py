# Generated by Django 2.2.7 on 2019-11-20 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='c_address',
            new_name='customer_address',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='c_fname',
            new_name='customer_fname',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='c_lname',
            new_name='customer_lname',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='c_pno',
            new_name='customer_pno',
        ),
    ]
