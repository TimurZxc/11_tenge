from django.forms import ModelForm
from .models import Teacher, File

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ('__all__')
        labels = {
            'name': 'Құжаттың аты',
            'file': 'Құжаттың өзі',
            'tag': 'Жалпы тег',
            'year': 'Жылы',
            'block': 'Болк',
        }
        

class TeacherForm(ModelForm):
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