from django import forms
from .models import LeaveRequest, Student

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['start_date', 'end_date', 'reason']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'required': True}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'required': True}),
            'reason': forms.Textarea(attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Reason for leave...', 'required': True}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and end_date < start_date:
            raise forms.ValidationError("End date cannot be earlier than start date.")
        return cleaned_data

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'name', 'roll_number', 'grade_level', 'attendance_status']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Full Name'}),
            'roll_number': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Roll Number'}),
            'grade_level': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Grade Level'}),
            'attendance_status': forms.Select(attrs={'class': 'form-select'}),
        }