from django.urls import path

from . import views
app_name="CRUD"
urlpatterns = [
    path('add/', views.index, name='index'),
    path('', views.home, name='home'),
    path('read/', views.read, name='read'),
    path('search/',views.search,name='search'),
    path('update/',views.update,name='update'),
    path('delete/',views.delete,name='delete'),

]
