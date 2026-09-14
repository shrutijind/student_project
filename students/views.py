from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import LeaveRequest, Student
from .forms import LeaveRequestForm, StudentForm

def student_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        
    return render(request, 'students/login.html', {'form': form})

def student_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    if request.user.is_staff:
        pending_requests = LeaveRequest.objects.filter(status='Pending')
        students = Student.objects.all()
        return render(request, 'students/admin_dashboard.html', {
            'pending_requests': pending_requests,
            'students': students
        })
    else:
        student = get_object_or_404(Student, user=request.user)
        my_requests = LeaveRequest.objects.filter(student=student)
        return render(request, 'students/parent_dashboard.html', {
            'my_requests': my_requests,
            'student': student
        })

@login_required
def apply_leave(request):
    student = get_object_or_404(Student, user=request.user)
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.student = student
            leave_request.status = 'Pending'
            leave_request.save()
            messages.success(request, "Leave request submitted successfully.")
            return redirect('dashboard')
    else:
        form = LeaveRequestForm()
    return render(request, 'students/apply_leave.html', {'form': form})

@login_required
def cancel_leave(request, leave_id):
    student = get_object_or_404(Student, user=request.user)
    leave_request = get_object_or_404(LeaveRequest, id=leave_id, student=student, status='Pending')
    leave_request.delete()
    messages.info(request, "Leave request cancelled.")
    return redirect('dashboard')

@login_required
def update_leave_status(request, leave_id, status):
    if not request.user.is_staff:
        return redirect('dashboard')
    leave_request = get_object_or_404(LeaveRequest, id=leave_id)
    if status in ['Approved', 'Rejected']:
        leave_request.status = status
        leave_request.save()
        if status == 'Approved':
            student = leave_request.student
            student.attendance_status = 'Absent'
            student.save()
        messages.success(request, f"Leave request marked as {status}.")
    return redirect('dashboard')

@login_required
def toggle_attendance(request, student_id):
    if not request.user.is_staff:
        return redirect('dashboard')
    student = get_object_or_404(Student, id=student_id)
    student.attendance_status = 'Absent' if student.attendance_status == 'Present' else 'Present'
    student.save()
    messages.success(request, f"Updated attendance for {student.user.get_full_name() or student.user.username}.")
    return redirect('dashboard')

@login_required
def add_student(request):
    if not request.user.is_staff:
        return redirect('dashboard')
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student profile created successfully.")
            return redirect('dashboard')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

@login_required
def delete_student(request, student_id):
    if not request.user.is_staff:
        return redirect('dashboard')
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    messages.warning(request, "Student record deleted.")
    return redirect('dashboard')