

from django.urls import path
from . import views

app_name ="job"
urlpatterns = [
    path('',views.index,name='index'),
    path('aboutjob/<int:job_id>',views.aboutJob,name="aboutjob")
]
