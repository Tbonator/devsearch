from django.urls import  path
from . import views



#import views into this file 

urlpatterns = [
    path('',views.projects,name="projects"),
    path('project/<str:pk>',views.project,name="project"),
    path('create-projects', views.createProject, name="createProject"),
    

]
