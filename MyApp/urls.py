from django.conf.urls import url
from MyApp import views

app_name = 'MyApp'

urlpatterns =[
    url(r'^register/', views.register_user,name="register"),
    url(r'^user_login/', views.user_login,name="user_login")
]
