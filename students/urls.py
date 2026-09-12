from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('leave/apply/', views.apply_leave, name='apply_leave'),
    path('leave/update/<int:pk>/<str:status>/', views.update_leave_status, name='update_leave_status'),
]