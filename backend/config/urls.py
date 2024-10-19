from django.contrib import admin  
from django.urls import path  
from django.conf import settings  
from django.conf.urls.static import static  
from ticket.views import home  # اطمینان حاصل کنید که 'myapp' نام اپلیکیشن شماست و view شما تعریف شده است  

urlpatterns = [  
    path('admin/', admin.site.urls),  # مسیر مدیریت  
    path('', home, name='home'),      # مسیر برای صفحه اصلی  
]  

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)