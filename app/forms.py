from django.forms import ModelForm
from .models import Teacher, File
from django import forms

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ('name','file','tag','year','block')
        labels = {
            'name': 'Құжаттың аты',
            'file': 'Құжаттың өзі',
            'tag': 'Жалпы тег',
            'year': 'Жылы',
            'block': 'Болк',
        }
       

class TeacherForm(ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), input_formats=['%Y-%m-%d'])    
    class Meta:
        model = Teacher
        fields = ('__all__')
        labels = {
            'first_name': 'Аты',
            'last_name': 'Тегі',
            'middle_name': 'Жөні',
            'birth_date': 'Тұған күні',
            'education': 'Білімі',
            'diploma': 'Дипломы',
            'qualification': 'Дипломы бойынша жоғары біліктілігі',
            'position': 'Лауазымы',
            'overall_experience': 'Педагогикалық еңбек өтілі',
            'experience': 'Осы мекемедегі еңбек өтілі',
            'category': 'Біліктілік санаты',
            'phone_number': 'Телефон нөмірі',
            'image': 'Фото сүреті',
            'block': 'Болк',
        }