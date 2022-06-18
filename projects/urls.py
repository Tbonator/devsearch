from django.urls import  path
from . import views



#import views into this file 

urlpatterns = [
    path('',views.projects,name="projects"),
    path('project/<str:pk>',views.project,name="project"),
    path('create-projects', views.createProject, name="createProject"),
    path('update-projects/<str:pk>/', views.updateProject, name="updateProject"),
    path('delete-projects/<str:pk>/', views.deleteProject, name="deleteProject"),
    

]
