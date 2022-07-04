# Generated by Django 3.0 on 2022-06-27 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myproject',
            name='descrip',
        ),
        migrations.RemoveField(
            model_name='myproject',
            name='image',
        ),
        migrations.RemoveField(
            model_name='myproject',
            name='name',
        ),
        migrations.AddField(
            model_name='myproject',
            name='text',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
    ]