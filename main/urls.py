from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name='home'),
    path('userProfile', views.profile, name='user_profile'),
    path('save_job', views.save_job, name='save_job'),
    path('changeName', views.changeName, name='changeName'),
]