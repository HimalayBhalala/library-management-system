# Generated by Django 5.0.6 on 2024-06-04 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_readbook_returned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readbook',
            name='returned',
            field=models.BooleanField(default=False),
        ),
    ]