# Generated by Django 4.1.4 on 2023-10-13 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autorzy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=60)),
                ('opis', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autorzy',
            },
        ),
        migrations.CreateModel(
            name='Gatunki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Gatunek',
                'verbose_name_plural': 'Gatunki',
            },
        ),
        migrations.CreateModel(
            name='Bibliotego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('opis', models.TextField(blank=True)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Autorzy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Bibliotego.autorzy')),
                ('Gatunki', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Bibliotego.gatunki')),
            ],
        ),
    ]
