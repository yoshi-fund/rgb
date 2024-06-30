from django.urls import path
from . import views

app_name = 'medical'

urlpatterns = [
    path('', views.List.as_view(), name='list'),
    path('create/', views.Create.as_view(), name='create')
]