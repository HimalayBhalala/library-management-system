# Generated by Django 5.0.6 on 2024-06-04 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_remove_readbook_returned_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='readbook',
            name='returned_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]