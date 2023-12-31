# Generated by Django 4.2.6 on 2023-10-28 17:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('localizacao', models.CharField(max_length=50, verbose_name='Localização')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Stand',
                'verbose_name_plural': 'Stands',
            },
        ),
    ]
