# Generated by Django 4.1.6 on 2023-08-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_teacher_rename_files_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='diploma',
            field=models.FileField(blank=True, null=True, upload_to='diplomas/'),
        ),
    ]
