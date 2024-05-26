from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [ 
    path('', views.index),
    path('home/', views.home),
    path('contact/', views.contact),
    path('register/', views.register, name='register'),
    path('signup',views.signup),
    # path('search/', views.search, name='search'),
    path('login/',views.Login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]



