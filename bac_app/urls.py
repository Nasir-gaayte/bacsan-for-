from django.urls import path
from . import views

app_name = 'bac_app'



urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login_requeset,name='login'),
    path('logout/',views.logout_request,name='logout'),
]
