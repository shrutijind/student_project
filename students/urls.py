from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.student_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('leave/apply/', views.apply_leave, name='apply_leave'),
    path('leave/edit/<int:leave_id>/', views.edit_leave, name='edit_leave'),
    path(
        'leave/cancel/<int:leave_id>/',
        views.cancel_leave,
        name='cancel_leave',
    ),
    path(
        'leave/update/<int:leave_id>/<str:status>/',
        views.update_leave_status,
        name='update_leave_status',
    ),
    path(
        'attendance/toggle/<int:student_id>/',
        views.toggle_attendance,
        name='toggle_attendance',
    ),
    path('student/add/', views.add_student, name='add_student'),
    path(
        'student/delete/<int:student_id>/',
        views.delete_student,
        name='delete_student',
    ),
]
