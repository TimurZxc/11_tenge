from django.db import models
from django.conf import settings
import os


block_choices = [('1', '1'), ('2', '2')]

tag_choices = [
    ('schedule','schedule'),
    ('course','course'),
    ('methodist_cyclogram','methodist_cyclogram'),
    ('mad','mad'),
    ('methodist_monitoring','methodist_monitoring'),
    ('personal_development_map','personal_development_map'),
    ('monitoring','monitoring'),
    ('group_cyclogram','group_cyclogram'),
    ('year_plan','year_plan'),
    ('gpp','gpp'),
    ('about','about'),
]


class File(models.Model):
    year_choices = [('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), 
                ('2022-2023', '2022-2023')]
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdf/')
    tag = models.CharField(max_length=100, default='common', choices=tag_choices)
    year = models.CharField(max_length=10, choices=year_choices)
    block = models.CharField(max_length=10, choices=block_choices)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        file_path = os.path.join(settings.MEDIA_ROOT, self.file)
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
    block = models.CharField(max_length=10,choices=block_choices)


    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
    
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        diploma_path = os.path.join(settings.MEDIA_ROOT, self.diploma)
        avatar_path = os.path.join(settings.MEDIA_ROOT, self.image)
        os.remove(diploma_path)
        os.remove(avatar_path)