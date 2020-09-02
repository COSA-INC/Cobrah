

from django.urls import path
from . import views

app_name="job_messages"
urlpatterns = [
    path('',views.test,name='test'),
]
