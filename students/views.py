from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import LeaveRequest, Student
from .forms import LeaveRequestForm, StudentRegistrationForm


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after successful registration
            messages.success(request, f"Account created successfully! Welcome, {user.username}.")
            return redirect('dashboard')
    else:
        form = StudentRegistrationForm()

    return render(request, 'students/register.html', {'form': form})


@login_required
def dashboard(request):
    # Staff / Admin view
    if request.user.is_staff:
        my_requests = LeaveRequest.objects.all().order_by('-start_date')
        return render(request, 'students/admin_dashboard.html', {'my_requests': my_requests})
    
    # Student view
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
    
    # Access Control Check
    if not request.user.is_staff and leave_request.student.user != request.user:
        messages.error(request, "You are not authorized to edit this request.")
        return redirect('dashboard')
        
    # Prevent editing non-pending requests
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