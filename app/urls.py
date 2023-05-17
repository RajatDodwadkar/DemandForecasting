from django.urls import path
from app import views

urlpatterns = [
	path('', views.index, name='index'),
    path('tools/', views.tools, name='tools'),
	path('aboutus/', views.about_us, name='aboutus'),
    path('shop/', views.shop, name="shop"),
    
	# Authentication
	path('login/', views.log_in, name='log_in'),
    path('signup/', views.sign_up, name='sign_up'),
    path('logout/', views.log_out, name="log_out")
]