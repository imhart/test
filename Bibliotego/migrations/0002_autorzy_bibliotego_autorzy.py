# Generated by Django 4.1.4 on 2023-01-13 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bibliotego', '0001_initial'),
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
        migrations.AddField(
            model_name='bibliotego',
            name='Autorzy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Bibliotego.autorzy'),
        ),
    ]
