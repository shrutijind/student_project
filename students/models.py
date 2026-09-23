from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    grade_level = models.CharField(max_length=20)
    attendance_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Present')

    def __str__(self):
        return f"{self.roll_number} - {self.name}"

    def delete(self, *args, **kwargs):
        user = self.user
        super().delete(*args, **kwargs)  # Delete the Student record first
        if user:
            user.delete()  # Automatically delete the linked User account


class LeaveRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='leave_requests')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(max_length=250)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.status}"