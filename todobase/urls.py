from django import views
from django.urls import path
from .  import views

urlpatterns=[
    path('',views.home,name="home"),
    path('update_list/<str:rp>/',views.updateList,name="update_list"),
    path('delete/<str:rp>/',views.deleteList,name="delete"),
]

