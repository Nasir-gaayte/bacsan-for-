# Generated by Django 4.1 on 2022-08-14 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bac_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='tiem',
        ),
        migrations.RemoveField(
            model_name='storein',
            name='item',
        ),
        migrations.DeleteModel(
            name='FromFactry',
        ),
        migrations.DeleteModel(
            name='Sales',
        ),
        migrations.DeleteModel(
            name='StoreIn',
        ),
    ]