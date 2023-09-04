from typing import Any, Dict, Optional
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from app.forms import *
from .models import File, Teacher
from django.views import generic
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.urls import reverse
import os
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.admin.sites import AdminSite
from django.http import HttpResponseRedirect
from django.contrib.auth.views import RedirectURLMixin



class CustomAdminLogin(AdminSite):
    def login(self, request, extra_context=None):
        """
        Display the login form for the given HttpRequest.
        """
        if request.method == "GET" and self.has_permission(request):
            # Already logged-in, redirect to admin index
            index_path = reverse("/", current_app=self.name)
            return HttpResponseRedirect(index_path)

        # Since this module gets imported in the application's root package,
        # it cannot import models from other applications at the module level,
        # and django.contrib.admin.forms eventually imports User.
        from django.contrib.admin.forms import AdminAuthenticationForm
        from django.contrib.auth.views import LoginView

        context = {
            **self.each_context(request),
            "title": _("Log in"),
            "subtitle": None,
            "app_path": request.get_full_path(),
            "username": request.user.get_username(),
        }
        if (
            REDIRECT_FIELD_NAME not in request.GET
            and REDIRECT_FIELD_NAME not in request.POST
        ):
            context[REDIRECT_FIELD_NAME] = reverse("/", current_app=self.name)
        context.update(extra_context or {})

        defaults = {
            "extra_context": context,
            "authentication_form": self.login_form or AdminAuthenticationForm,
            "template_name": self.login_template or "admin/login.html",
        }
        request.current_app = self.name
        return LoginView.as_view(**defaults)(request)

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetch image filenames from the directory
        if settings.DEBUG:
            image_directory = os.path.join(settings.STATICFILES_DIRS[0], 'images')
        else:
            image_directory = os.path.join(settings.STATIC_ROOT, 'images')
        image_filenames = [filename for filename in os.listdir(image_directory) if not filename.endswith(".svg")]
        
        context['image_filenames'] = image_filenames
        return context
    
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
    paginate_by = 10

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

class DeleteFile(generic.DeleteView):
    model = File
    template_name='delete_file.html'
    success_url = reverse_lazy('all_files')

class FileUpdateView(generic.UpdateView):
    form_class = FileForm
    template_name = 'file_update.html' 
    success_url = reverse_lazy('all_files')  

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.update(**form.cleaned_data)  
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return get_object_or_404(File, id=self.kwargs['pk'])
    
class TeacherUpdateView(generic.UpdateView):
    template_name = 'teacher_update.html'  

    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        form = TeacherForm(instance=teacher)
        return render(request, self.template_name, {'form': form, 'teacher': teacher})

    def post(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers')
        return render(request, self.template_name, {'form': form, 'teacher': teacher})

def custom_404(request, exception):
    return render(request, '404.html', status=404)

