
from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('innerpage/', views.inner, name='index'),
    path('register/', views.inner, name='register'),
    path('login/', views.inner, name='login'),

]
