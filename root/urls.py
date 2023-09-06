from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views import custom_admin_login, CustomLogoutView

urlpatterns = [
    path('custom-logout/', CustomLogoutView.as_view(), name='custom_logout'),
    path('admin/login/', custom_admin_login, name='custom_admin_login'),
    path('admin/', admin.site.urls),
    path('login/', admin.AdminSite.login), 
    path('', include('app.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'app.views.custom_404'

