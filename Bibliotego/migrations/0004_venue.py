# Generated by Django 4.1.4 on 2023-10-25 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bibliotego', '0003_delete_venue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
