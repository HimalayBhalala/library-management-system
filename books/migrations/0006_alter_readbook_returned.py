# Generated by Django 5.0.6 on 2024-06-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_readbook_returned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readbook',
            name='returned',
            field=models.DateField(default='<built-in method utcnow of type object at 0x5f76be6d88a0>'),
        ),
    ]
