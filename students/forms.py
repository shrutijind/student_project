from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import LeaveRequest, Student
from django.utils import timezone


class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['start_date', 'end_date', 'reason']
        widgets = {
            'start_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control', 'required': True}
            ),
            'end_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control', 'required': True}
            ),
            'reason': forms.Textarea(
                attrs={
                    'rows': 4,
                    'class': 'form-control',
                    'placeholder': 'Reason for leave...',
                    'required': True
                }
            ),
        }

    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        if start_date and start_date < timezone.now().date():
            raise forms.ValidationError(
                "Leave start date cannot be in the past."
            )
        return start_date

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and end_date < start_date:
            raise forms.ValidationError(
                "End date cannot be earlier than start date."
            )
        return cleaned_data


class StudentForm(forms.ModelForm):
    """
    Simplified Student creation form.
    Only requires name, roll_number, and grade_level.
    """
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'grade_level']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'required': True, 'placeholder': 'Full Name'}
            ),
            'roll_number': forms.TextInput(
                attrs={'class': 'form-control', 'required': True, 'placeholder': 'Roll Number'}
            ),
            'grade_level': forms.TextInput(
                attrs={'class': 'form-control', 'required': True, 'placeholder': 'Grade Level'}
            ),
        }


class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    roll_number = forms.CharField(
        max_length=20, 
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Roll Number'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply Bootstrap styling to standard user fields
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            # Automatically create and link the Student profile
            Student.objects.create(
                user=user,
                name=f"{user.first_name} {user.last_name}",
                roll_number=self.cleaned_data['roll_number']
            )
        return user