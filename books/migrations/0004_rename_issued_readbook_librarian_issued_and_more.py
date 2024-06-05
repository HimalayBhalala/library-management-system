# Generated by Django 5.0.6 on 2024-06-05 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_readbook_issued_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='readbook',
            old_name='issued',
            new_name='librarian_issued',
        ),
        migrations.RemoveField(
            model_name='readbook',
            name='issued_at',
        ),
        migrations.AddField(
            model_name='readbook',
            name='librarian_issued_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='readbook',
            name='student_issued',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='readbook',
            name='student_issued_at',
            field=models.DateField(auto_now=True),
        ),
    ]
