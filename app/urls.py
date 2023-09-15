from django.urls import path
from django.views.generic import TemplateView
from .views import *
from . import views
urlpatterns = [
    path('', FilesList.as_view(), name='files'),
    path('form/', uploadForm, name='form'),
    path('upload/', UploadFile.as_view(), name='upload'),
    path('about/', AboutUs.as_view(), name='about'),
    path('teachers/', Staff.as_view(), name='teachers'),
    path('create_teacher/', CreateTeacher.as_view(), name='сreate_teacher'),
    path('delete_teacher/<int:pk>/', DeleteTeacher.as_view(), name='delete_teacher'),
    path('delete_file/<int:pk>/', DeleteFile.as_view(), name='delete_file'),
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
    path('file/<int:pk>/update/', FileUpdateView.as_view(), name='update_file'),
    path('teacher/<int:pk>/update/', TeacherUpdateView.as_view(), name='update_teacher'),

    path('docs/', Docs.as_view(), name='docs'),
    path('docs/2020-2021/', Docs.as_view(template_name = '2020-2021.html', tag='2020-2021 ж'), name='2020-2021'),
    path('docs/2020-2021/tech-cards/', Docs.as_view(template_name = '2020-2021 ж жеке даму картасы.html', tag='2020-2021 ж жеке даму картасы'), name='2020-2021_tech_cards'),
    path('docs/2020-2021/indicators/', Docs.as_view(template_name = '2020-2021 ж Индикаторлар.html', tag='2020-2021 ж Индикаторлар'), name='2020-2021_indicators'),
    path('docs/2020-2021/indicators/1_bal_tob/', Docs.as_view(template_name = '№1 Балбөбек тобы.html', tag='№1 Балбөбек тобы'), name='Y2020_2021_indicators_1_bal_tob'),
    path('docs/2020-2021/indicators/2_erk_tob/', Docs.as_view(template_name = '№2 Еркелер тобы.html', tag='№2 Еркелер тобы'), name='Y2020_2021_indicators_2_erk_tob'),
    path('docs/2020-2021/indicators/3_bot_tob/', Docs.as_view(template_name = '№3 Ботақан тобы.html', tag='№3 Ботақан тобы'), name='Y2020_2021_indicators_3_bot_tob'),
    path('docs/2020-2021/indicators/4_qul_tob/', Docs.as_view(template_name = '№4 Құлыншақ тобы.html', tag='№4 Құлыншақ тобы'), name='Y2020_2021_indicators_4_qul_tob'),
    path('docs/2020-2021/indicators/5_bal_tob/', Docs.as_view(template_name = '№5 Балапан тобы.html', tag='№5 Балапан тобы'), name='Y2020_2021_indicators_5_bal_tob'),
] 
