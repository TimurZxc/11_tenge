from django.db import models
from django.conf import settings
import os

block_choices = [('1', '1 блок'),
                 ('2', '2 блок')]


class File(models.Model):
    year_choices = [('2020-2021', '2020-2021'),
                    ('2021-2022', '2021-2022'),
                    ('2022-2023', '2022-2023')]

    tag_choices = [('schedule', 'Кесте'),
                   ('course', 'Курс'),
                   ('methodist_cyclogram', 'Әдіскер циклограмасы'),
                   ('mad', 'МАД'),
                   ('methodist_monitoring', 'Әдіскер мониторинг'),
                   ('personal_development_map', 'Жеке даму картасы'),
                   ('monitoring', 'Мониторинг'),
                   ('group_cyclogram', 'Топтың циклограммасы'),
                   ('year_plan', 'Жалдық жоспар'),
                   ('gpp', 'Топтардың перспективалық жоспарлары'),
                   ('about', 'Біз туралы')]

    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdf/', max_length=255)
    tag = models.CharField(
        max_length=100, default='common', choices=tag_choices)
    year = models.CharField(max_length=10, choices=year_choices)
    block = models.CharField(max_length=10, choices=block_choices)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        file_path = os.path.join(settings.MEDIA_ROOT, self.file.name)
        super().delete(*args, **kwargs)
        os.remove(file_path)


class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField()
    education = models.CharField(max_length=1000)
    diploma = models.FileField(upload_to='diplomas/', null=True, blank=True)
    qualification = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    overall_experience = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    block = models.CharField(max_length=10, choices=block_choices)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def delete(self, *args, **kwargs):
        diploma_path = os.path.join(settings.MEDIA_ROOT, self.diploma.name)
        avatar_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
        super().delete(*args, **kwargs)
        os.remove(diploma_path)
        os.remove(avatar_path)
