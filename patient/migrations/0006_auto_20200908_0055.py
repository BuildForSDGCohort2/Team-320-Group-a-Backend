# Generated by Django 3.0.6 on 2020-09-08 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_auto_20200908_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.Patient'),
        ),
    ]
