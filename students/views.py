from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import LeaveRequest, Student
from .forms import LeaveRequestForm, StudentForm, StudentRegistrationForm
from django.views.decorators.http import require_POST



def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'students/login.html', {'form': form})


def student_logout(request):
    auth_logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, f"Account created successfully! Welcome, {user.username}.")
            return redirect('dashboard')
    else:
        form = StudentRegistrationForm()
    return render(request, 'students/register.html', {'form': form})


@login_required
def dashboard(request):
    if request.user.is_staff:
        students = Student.objects.all()
        leave_requests = LeaveRequest.objects.all().order_by('-start_date')
        return render(request, 'students/admin_dashboard.html', {
            'students': students,
            'my_requests': leave_requests
        })
    
    student = get_object_or_404(Student, user=request.user)
    my_requests = LeaveRequest.objects.filter(student=student).order_by('-start_date')
    return render(request, 'students/parent_dashboard.html', {
        'student': student,
        'my_requests': my_requests
    })


@login_required
def apply_leave(request):
    student = get_object_or_404(Student, user=request.user)
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.student = student
            leave.save()
            messages.success(request, "Leave request submitted successfully.")
            return redirect('dashboard')
    else:
        form = LeaveRequestForm()
    return render(request, 'students/apply_leave.html', {'form': form})


@login_required
def edit_leave(request, leave_id):
    leave_request = get_object_or_404(LeaveRequest, id=leave_id)
    if not request.user.is_staff and leave_request.student.user != request.user:
        messages.error(request, "You are not authorized to edit this request.")
        return redirect('dashboard')
        
    if leave_request.status != 'Pending':
        messages.warning(request, "You cannot edit a request that has already been processed.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = LeaveRequestForm(request.POST, instance=leave_request)
        if form.is_valid():
            form.save()
            messages.success(request, "Your leave request has been updated successfully!")
            return redirect('dashboard')
    else:
        form = LeaveRequestForm(instance=leave_request)

    return render(request, 'students/edit_leave.html', {'form': form, 'leave_request': leave_request})


@login_required
def cancel_leave(request, leave_id):
    leave_request = get_object_or_404(LeaveRequest, id=leave_id)
    if leave_request.student.user == request.user and leave_request.status == 'Pending':
        leave_request.delete()
        messages.success(request, "Leave application canceled successfully.")
    else:
        messages.error(request, "Unable to cancel this leave application.")
    return redirect('dashboard')


@login_required
def update_leave_status(request, leave_id, status):
    if not request.user.is_staff:
        messages.error(request, "Unauthorized access.")
        return redirect('dashboard')
    leave_request = get_object_or_404(LeaveRequest, id=leave_id)
    if status in ['Approved', 'Rejected']:
        leave_request.status = status
        leave_request.save()
        messages.success(request, f"Leave request status updated to {status}.")
    return redirect('dashboard')

@login_required
@require_POST 
 # Ensures state changes only happen via POST requests
def toggle_attendance(request, student_id):
    if not request.user.is_staff:
        messages.error(request, "Unauthorized access.")
        return redirect('dashboard')
        
    student = get_object_or_404(Student, id=student_id)
    student.attendance_status = 'Absent' if student.attendance_status == 'Present' else 'Present'
    student.save()
    
    messages.success(request, f"Attendance status for {student.name} updated.")
    return redirect('dashboard')


@login_required
def add_student(request):
    if not request.user.is_staff:
        messages.error(request, "Unauthorized access.")
        return redirect('dashboard')
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New student added successfully.")
            return redirect('dashboard')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})


@login_required
def delete_student(request, student_id):
    if not request.user.is_staff:
        messages.error(request, "Unauthorized access.")
        return redirect('dashboard')
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    messages.success(request, "Student profile deleted successfully.")
    return redirect('dashboard')


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student

@login_required
def toggle_attendance(request, student_id):
    if not request.user.is_staff:
        messages.error(request, "Unauthorized access.")
        return redirect('dashboard')
        
    student = get_object_or_404(Student, id=student_id)
    # Flip status between Present and Absent
    student.attendance_status = 'Absent' if student.attendance_status == 'Present' else 'Present'
    student.save()
    
    messages.success(request, f"Attendance status for {student.name} updated to {student.attendance_status}.")
    return redirect('dashboard')

