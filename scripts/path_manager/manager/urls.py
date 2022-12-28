from django.urls import path
from . import views


app_name = 'manager'

urlpatterns = [
    path('manager/', views.manage, name='manager'),
    path('reader/<int:pk>/', views.pdf_reader, name="pdfReader"),
    path('readers-list/', views.Readers_list.as_view(), name='readers-list')
]