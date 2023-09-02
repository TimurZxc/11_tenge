from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from app.forms import FileForm, TeacherForm
from .models import File, Teacher
from django.views import generic

def uploadForm(request):
    return render(request, 'upload.html')
    
class UploadFile(generic.CreateView):
    form_class = FileForm
    template_name = 'upload.html'
    success_url = reverse_lazy('all_files')
    
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched_files = File.objects.filter(name__contains = searched)
        return render(request, 'searched_page.html', {'searched': searched, 'searched_files': searched_files})
    else:
        return render(request, 'searched_page.html')
        
class FilesList(generic.ListView):
    model = File
    template_name = 'list.html'
    context_object_name = 'files'
    paginate_by = 4

    def get_queryset(self):
        return File.objects.order_by('-id')
    
class Teachers(generic.ListView):
    model = File
    template_name = 'teachers.html'
    context_object_name = 'files'
    paginate_by = 4

    def get_queryset(self):
        queryset = File.objects.filter(tag='teacher')
        block = self.request.GET.get('block')
        if block:
            queryset = queryset.filter(block=str(block))
        else:
            queryset = queryset.filter(block='1')
        return queryset
    

class AboutUs(generic.ListView):
    model = File
    template_name = 'about.html'
    paginate_by = 10
    context_object_name = 'files'

    def get_queryset(self):
        queryset = File.objects.filter(tag='about')
        block = self.request.GET.get('block')
        if block:
            queryset = queryset.filter(block=str(block))
        else:
            queryset = queryset.filter(block='1')
        return queryset



class Staff(generic.ListView):
    model = Teacher
    template_name = 'teacher.html'
    context_object_name = 'teachers'
    paginate_by = 10

    def get_queryset(self):
        queryset = Teacher.objects.all()
        block = self.request.GET.get('block')
        if block:
            queryset = queryset.filter(block=str(block))
        else:
            queryset = queryset.filter(block='1')
        return queryset
    
class YearPlan(generic.ListView):
    model = File
    template_name = 'year_plan.html'
    context_object_name = 'files'
    paginate_by = 10

    def get_queryset(self):
        block = self.request.GET.get('block')
        queryset = File.objects.filter(tag='year_plan')
        if block:
            queryset = queryset.filter(block=str(block))
        else:
            queryset = queryset.filter(block='1')
        return queryset
    

class GPP(generic.ListView):
    model = File
    template_name = 'gpp.html'
    context_object_name = 'files'
    paginate_by = 10


    def get_queryset(self):
        queryset = File.objects.filter(tag='gpp')
        block = self.request.GET.get('block')
        if block:
            queryset = queryset.filter(block=str(block))
        else:
            queryset = queryset.filter(block='1')
        return queryset

    
class GroupCyclogram(generic.ListView):
    model = File
    template_name = 'group_cyclogram.html'
    context_object_name = 'files'
    paginate_by = 10
    

    def get_queryset(self):
        queryset = File.objects.filter(tag='group_cyclogram')
        block = self.request.GET.get('block')
        if block:
            queryset = queryset.filter(block=str(block))
        else:
            queryset = queryset.filter(block='1')
        return queryset


class Monitoring(generic.ListView):
    model = File
    template_name = 'monitoring.html'
    context_object_name = 'files'
    paginate_by = 10


    def get_queryset(self):
        queryset = File.objects.filter(tag='monitoring')
        block = self.request.GET.get('block')
        if block:
            queryset = queryset.filter(block=str(block))
        else:
            queryset = queryset.filter(block='1')
        return queryset

    

class PersonalDevelopmentMap(generic.ListView):
    model = File
    template_name = 'personal_development_map.html'
    context_object_name = 'files'
    paginate_by = 10


    def get_queryset(self):
        queryset = File.objects.filter(tag='personal_development_map')
        block = self.request.GET.get('block')
        if block:
            queryset = queryset.filter(block=str(block))
        else:
            queryset = queryset.filter(block='1')
        return queryset
    
class MethodistMonitoring(generic.ListView):
    model = File
    template_name = 'methodist_monitoring.html'
    context_object_name = 'files'
    paginate_by = 10

    def get_queryset(self):
        queryset = File.objects.filter(tag='methodist_monitoring')
        block = self.request.GET.get('block')
        if block:
            queryset = queryset.filter(block=str(block))
        else:
            queryset = queryset.filter(block='1')
        return queryset



class MAD(generic.ListView):
    model = File
    template_name = 'm_a_d.html'
    context_object_name = 'files'
    paginate_by = 10

    def get_queryset(self):
        queryset = File.objects.filter(tag='mad')
        block = self.request.GET.get('block')
        if block:
            queryset = queryset.filter(block=str(block))
        else:
            queryset = queryset.filter(block='1')
        return queryset
    
class MethodistCyclogram(generic.ListView):
    model = File
    template_name = 'methodist_cyclogram.html'
    context_object_name = 'files'
    paginate_by = 10

    
    def get_queryset(self):
        queryset = File.objects.filter(tag='methodist_cyclogram')
        block = self.request.GET.get('block')
        if block:
            queryset = queryset.filter(block=str(block))
        else:
            queryset = queryset.filter(block='1')
        return queryset
    
class Course(generic.ListView):
    model = File
    template_name = 'course.html'
    context_object_name = 'files'
    paginate_by = 10

    def get_queryset(self):
        queryset = File.objects.filter(tag='course')
        block = self.request.GET.get('block')
        if block:
            queryset = queryset.filter(block=str(block))
        else:
            queryset = queryset.filter(block='1')
        return queryset
    

class Schedule(generic.ListView):
    model = File
    template_name = 'schedule.html'
    context_object_name = 'files'
    paginate_by = 10

    def get_queryset(self):
        block = self.request.GET.get('block')
        queryset = File.objects.filter(tag='schedule')
        if block:
            queryset = queryset.filter(block=str(block))
        else:
            queryset = queryset.filter(block='1')
        return queryset
    

class AllFiles(generic.ListView):
    model = File
    template_name = 'all_files.html'
    context_object_name = 'files'
    paginate_by = 15

    def get_queryset(self):
        queryset = File.objects.filter(tag='common')
        block = self.request.GET.get('block')
        if block:
            queryset = queryset.filter(block=str(block))
        else:
            queryset = queryset.filter(block='1')
        return queryset

class CreateTeacher(generic.CreateView):
    form_class = TeacherForm
    template_name = 'create_teacher.html'
    success_url = reverse_lazy('teachers')

class DeleteTeacher(generic.DeleteView):
    model = Teacher
    template_name='delete_teacher.html'
    success_url = reverse_lazy('teachers')