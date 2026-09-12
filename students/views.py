

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student, LeaveRequest

@login_required
def dashboard(request):
    if request.user.is_staff:
        students = Student.objects.all()
        leave_requests = LeaveRequest.objects.all().order_by('-submitted_at')
        return render(request, 'students/admin_dashboard.html', {
            'students': students,
            'leave_requests': leave_requests
        })
    else:
        student = get_object_or_404(Student, user=request.user)
        leave_requests = LeaveRequest.objects.filter(student=student).order_by('-submitted_at')
        return render(request, 'students/student_dashboard.html', {
            'student': student,
            'leave_requests': leave_requests
        })

@login_required
def apply_leave(request):
    student = get_object_or_404(Student, user=request.user)
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reason = request.POST.get('reason')
        
        LeaveRequest.objects.create(
            student=student,
            start_date=start_date,
            end_date=end_date,
            reason=reason
        )
        return redirect('dashboard')
        
    return render(request, 'students/apply_leave.html')

@login_required
def update_leave_status(request, pk, status):
    if request.user.is_staff:
        leave_request = get_object_or_404(LeaveRequest, pk=pk)
        if status in ['Approved', 'Rejected']:
            leave_request.status = status
            leave_request.save()
    return redirect('dashboard')