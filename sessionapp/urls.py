from django.conf.urls import url
from django.urls import path
from . import views
app_name='sessionapp'
urlpatterns=[
  path('input',views.input),
  path('add',views.add),
  path('display',views.display),
]