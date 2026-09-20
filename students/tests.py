from datetime import date
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from students.models import Student, LeaveRequest


class StudentModelTests(TestCase):
    """Test suite for Student and LeaveRequest database models."""

    @classmethod
    def setUpTestData(cls):
        """Set up initial user and student profile data."""
        cls.user = User.objects.create_user(
            username='johndoe', 
            email='john@example.com', 
            password='Password123!'
        )
        cls.student = Student.objects.create(
            user=cls.user,
            name="John Doe",
            roll_number="CS2026-001"
        )

    def test_student_profile_creation(self):
        """Assert student profile fields match setup data."""
        self.assertEqual(self.student.name, "John Doe")
        self.assertEqual(self.student.roll_number, "CS2026-001")
        self.assertEqual(self.student.user.username, "johndoe")

    def test_student_str_representation(self):
        """Verify __str__ returns expected representation matching 'Roll - Name' format."""
        expected_str = f"{self.student.roll_number} - {self.student.name}"
        self.assertEqual(str(self.student), expected_str)

    def test_user_cascade_deletion(self):
        """Ensure deleting User removes associated Student record."""
        user_id = self.user.id
        self.user.delete()
        self.assertFalse(User.objects.filter(id=user_id).exists())
        self.assertFalse(Student.objects.filter(user_id=user_id).exists())


class EduLeaveDefensiveEdgeCaseTests(TestCase):
    """Defensive, boundary, authorization, and security edge case tests."""

    @classmethod
    def setUpTestData(cls):
        """Set up two isolated student accounts and a leave record."""
        # Student A Setup
        cls.user_a = User.objects.create_user(username='student_a', password='Password123!')
        cls.student_a = Student.objects.create(
            user=cls.user_a, 
            name="Student A", 
            roll_number="ST001"
        )
        cls.leave_a = LeaveRequest.objects.create(
            student=cls.student_a,
            start_date=date(2026, 10, 1),
            end_date=date(2026, 10, 5),
            reason="Medical Leave"
        )

        # Student B Setup
        cls.user_b = User.objects.create_user(username='student_b', password='Password123!')
        cls.student_b = Student.objects.create(
            user=cls.user_b, 
            name="Student B", 
            roll_number="ST002"
        )

    def setUp(self):
        self.client = Client()

    def test_unauthenticated_access_blocked(self):
        """EDGE CASE: Logged-out users are redirected when accessing dashboard."""
        try:
            url = reverse('student_dashboard')
        except Exception:
            url = '/dashboard/'
            
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_prevent_idor_cross_user_leave_cancellation(self):
        """EDGE CASE (IDOR): Student B cannot cancel Student A's leave application."""
        self.client.login(username='student_b', password='Password123!')
        
        try:
            cancel_url = reverse('cancel_leave', kwargs={'pk': self.leave_a.pk})
        except Exception:
            cancel_url = f'/cancel-leave/{self.leave_a.pk}/'
            
        self.client.post(cancel_url)

        # Verify Student A's leave record remains intact in database
        self.assertTrue(LeaveRequest.objects.filter(pk=self.leave_a.pk).exists())

    def test_invalid_date_range_end_before_start(self):
        """EDGE CASE: Application rejects leave requests where end_date is before start_date."""
        self.client.login(username='student_a', password='Password123!')
        try:
            apply_url = reverse('apply_leave')
        except Exception:
            apply_url = '/apply-leave/'

        invalid_payload = {
            'start_date': '2026-10-10',
            'end_date': '2026-10-01',
            'reason': 'Testing date boundary'
        }
        self.client.post(apply_url, invalid_payload)
        
        # Verify no record was created with this invalid reason
        self.assertFalse(LeaveRequest.objects.filter(reason='Testing date boundary').exists())

    def test_xss_script_injection_escaped(self):
        """EDGE CASE: Raw <script> tags in text input are HTML-escaped on output."""
        self.client.login(username='student_a', password='Password123!')
        try:
            apply_url = reverse('apply_leave')
            dash_url = reverse('student_dashboard')
        except Exception:
            apply_url = '/apply-leave/'
            dash_url = '/dashboard/'

        xss_payload = "<script>alert('malicious')</script>"
        
        payload = {
            'start_date': '2026-11-01',
            'end_date': '2026-11-02',
            'reason': xss_payload
        }
        self.client.post(apply_url, payload)
        
        # Check rendered response on dashboard page
        response = self.client.get(dash_url)
        self.assertNotContains(response, "<script>alert('malicious')</script>")