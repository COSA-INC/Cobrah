

from django.urls import path
from . import views
app_name="suggestions"

urlpatterns = [
    path('',views.test,name='test'),
]
