from django.urls import include, path
from . import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup',views.signup,name='signup'),
    path('insert', views.insert, name='insert'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('demo', views.demo, name='demo'),

]