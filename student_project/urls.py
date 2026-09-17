from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('leave/apply/', views.apply_leave, name='apply_leave'),
    path('leave/edit/<int:leave_id>/', views.edit_leave, name='edit_leave'),
    path('leave/cancel/<int:leave_id>/', views.cancel_leave, name='cancel_leave'),
]