# Generated by Django 4.1.6 on 2023-08-31 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_teacher_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
