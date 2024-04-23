# students/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
   path('login/', views.user_login, name='login'),  # Root URL points to login view
    path('logout/', views.user_logout, name='logout'),
    path('view/', views.student_list, name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('<int:pk>/', views.student_detail, name='student_detail'),
    path('<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('logout/', views.user_logout, name='user_logout'),
]
