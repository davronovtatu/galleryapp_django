from django.urls import path
from .views import home,addedphotoview


urlpatterns=[
    path("",home,name='main'),
    path("added/",addedphotoview,name='add'),
]