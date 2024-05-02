from django.urls import path
from . import views

#URL configuration
urlpatterns = [
    path('', views.landingPage),
    path('signIn/', views.signIn, name='signIn'),
    path('signUp/', views.signUp, name='signUp'),
    path('homePage/', views.homePage, name='homePage'),
    path('homeUser/',views.homeUser,name='homeUser'),
    path('Api_connection/',views.Api_Conection,name='Api_Conection'),
    path('Settings/',views.Settings,name='Settings'),
    path('stats/',views.stats,name='stats'),
    path('Api_connection/',views.Api_Conection,name='Api_Connection'),
    path('price/',views.Price,name='Prce')
]
