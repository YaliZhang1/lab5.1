from django.conf.urls import url
from django.contrib.auth.signals import user_logged_in
from appTwo import views

app_name='appTwo'

urlpatterns = [  
    url(r'^register/$', views.register,name='register'),
    url(r'^user_login/$',views.user_logged_in, name='user_login')
]