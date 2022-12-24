from django.urls import path
from . import views


app_name = 'manager'

urlpatterns = [
    path('manager/', views.manage, name='manager')
]