# Generated by Django 5.0.6 on 2024-06-05 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_info_readbook_fine_readbook_issued_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readbook',
            name='issued_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]