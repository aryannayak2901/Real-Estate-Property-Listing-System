# Generated by Django 5.0.1 on 2024-03-07 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_web', '0008_alter_property_details_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='property_details',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_image'),
        ),
        migrations.AddField(
            model_name='property_details',
            name='image10',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_image'),
        ),
        migrations.AddField(
            model_name='property_details',
            name='image11',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_image'),
        ),
        migrations.AddField(
            model_name='property_details',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_image'),
        ),
        migrations.AddField(
            model_name='property_details',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_image'),
        ),
        migrations.AddField(
            model_name='property_details',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_image'),
        ),
        migrations.AddField(
            model_name='property_details',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_image'),
        ),
        migrations.AddField(
            model_name='property_details',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_image'),
        ),
        migrations.AddField(
            model_name='property_details',
            name='image7',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_image'),
        ),
        migrations.AddField(
            model_name='property_details',
            name='image8',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_image'),
        ),
        migrations.AddField(
            model_name='property_details',
            name='image9',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_image'),
        ),
    ]
