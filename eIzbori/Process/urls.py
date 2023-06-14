from django.urls import path
from . import views

urlpatterns = [
    path('login/<str:licence>', views.login_user, name='login'),
    path('login/listic/<str:licence>', views.listic, name='listic'),
    path('login/listic/hvala/<str:licence>', views.send_email, name='send_email'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]