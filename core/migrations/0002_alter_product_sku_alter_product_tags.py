# Generated by Django 5.1.2 on 2024-11-18 07:43

import django.db.models.deletion
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=8, max_length=20, prefix='sku', unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.tags'),
        ),
    ]
