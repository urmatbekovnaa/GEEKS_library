from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from main_page import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_me/', views.page_about_me, name='page_about_me'),
    path('image_link/', views.about_my_pets, name='about_my_pets'),
    path('time/', views.system_time, name='system_time'),
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)