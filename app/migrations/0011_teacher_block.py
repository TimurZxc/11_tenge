# Generated by Django 4.1.6 on 2023-08-31 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_file_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='block',
            field=models.CharField(choices=[('1', '1 блок'), ('2', '2 блок')], default='1 блок', max_length=10),
            preserve_default=False,
        ),
    ]
