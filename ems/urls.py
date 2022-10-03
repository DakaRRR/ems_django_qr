from django.conf.urls import handler404, handler500,  handler403, handler400
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls,name="admin-site"),
    path('', include('employee_information.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

handler404 = 'employee_information.views.error_404'

handler500 = 'employee_information.views.error_500'

handler403 = 'employee_information.views.error_403'

handler400 = 'employee_information.views.error_400'