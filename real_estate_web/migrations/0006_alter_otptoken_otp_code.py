# Generated by Django 5.0.1 on 2024-03-07 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_web', '0005_alter_otptoken_otp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default=964414, max_length=6),
        ),
    ]
