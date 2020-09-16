from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('ContactUs/', views.ContactUs, name='ContactUs'),
    path('quickview/<int:myid>', views.quickview, name='quickview'),
    path('About/', views.Abouts, name='About'),
    path('Error/', views.Error, name='Error'),
    path('CSR/', views.CSR, name='CSR'),
    path('Achievements/', views.Achievements, name='Achievements'),
]