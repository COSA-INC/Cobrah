

from django.urls import path
from . import views
app_name="status"

urlpatterns = [
    path('',views.status,name='test'),
    
]
