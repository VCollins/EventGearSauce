# Generated by Django 4.2.3 on 2023-07-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=50)),
                ('model_name', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=13)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]