from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('info/', views.info, name='info'),
]