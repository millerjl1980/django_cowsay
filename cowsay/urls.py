from django.urls import path
from cowsay import views

urlpatterns = [
    path('', views.index, name='home'),
    path('old_cows', views.old_cows, name='oldcows')
]