from django.urls import path
from main import views
urlpatterns = [
    path('projects/',views.project,name='project'),
    path('languages',views.languages,name="languages"),
    
    path('',views.index,name="index")
]
