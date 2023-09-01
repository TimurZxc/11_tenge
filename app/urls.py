from django.urls import path
from django.views.generic import TemplateView
from .views import *
from . import views
urlpatterns = [
    path('', FilesList.as_view(), name='files'),
    path('form/', uploadForm, name='form'),
    path('upload/', uploadFile, name='upload'),
    path('about/', AboutUs.as_view(), name='about'),
    path('teachers/', Staff.as_view(), name='teachers'),
    path('year_plan/', YearPlan.as_view(), name='year_plan'),
    path('gpp/', GPP.as_view(), name='gpp'),
    path('group_cyclogram/', GroupCyclogram.as_view(), name='group_cyclogram'),
    path('monitoring/', Monitoring.as_view(), name='monitoring'),
    path('personal_development_map/', PersonalDevelopmentMap.as_view(), name='personal_development_map'),
    path('methodist_monitoring/', MethodistMonitoring.as_view(), name='methodist_monitoring'),
    path('m_a_d/', MAD.as_view(), name='m_a_d'),
    path('methodist_cyclogram/', MethodistCyclogram.as_view(), name='methodist_cyclogram'),
    path('course/', Course.as_view(), name='course'),
    path('schedule/', Schedule.as_view(), name='schedule'),
    path('rate/', TemplateView.as_view(template_name='test.html'), name='rate'),
    path('all_files/', AllFiles.as_view(template_name='all_files.html'), name='all_files'),
    path('search/', views.search, name='search'),
] 
