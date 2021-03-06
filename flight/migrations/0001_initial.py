# Generated by Django 2.2.4 on 2019-08-26 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Name Of flight')),
                ('origin', models.CharField(blank=True, max_length=200, verbose_name='From')),
                ('destination', models.CharField(blank=True, default='', max_length=200)),
                ('status', models.CharField(choices=[('Booked', 'Reserved'), ('Available', 'Available')], default='Available', max_length=10)),
                ('date', models.DateField(verbose_name='Date of depature')),
                ('time', models.TimeField(verbose_name='Time of depature')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PassportImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=17)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('images', models.CharField(blank=True, max_length=17, verbose_name='passport image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FlightBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('number_of_tickets', models.IntegerField(default=1)),
                ('ticket_type', models.CharField(default='economy', max_length=30)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.Flight')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
