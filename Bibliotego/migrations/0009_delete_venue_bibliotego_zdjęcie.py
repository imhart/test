# Generated by Django 4.1.4 on 2023-10-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bibliotego', '0008_delete_kotki_venue_nazwa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Venue',
        ),
        migrations.AddField(
            model_name='bibliotego',
            name='zdjęcie',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
