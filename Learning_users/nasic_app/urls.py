from django.urls import path
from nasic_app import views


app_name = 'nasic_app'



urlpatterns = [
	path('register/', views.register,name='register'),
	path('user_login/',views.user_login,name='user_login'),
	
]