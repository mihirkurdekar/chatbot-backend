from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload_file, name='file'),
    path('train', views.train, name='train'),
    path('execute', views.execute, name='answer')
]