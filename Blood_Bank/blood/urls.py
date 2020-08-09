from django.urls import path

from .views import index

app_name = 'blood'
urlpatterns = [
    path('', index, name='index')
]
