# Generated by Django 2.2.4 on 2019-08-25 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passportimage',
            old_name='image',
            new_name='image_url',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='images',
            field=models.CharField(blank=True, max_length=17, verbose_name='passport image'),
        ),
    ]
