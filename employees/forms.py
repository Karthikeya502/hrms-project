from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):


    class Meta:
        model = Employee

        fields = [
            'name',
            'department',
            'designation',
            'salary'
        ]

from .models import Attendance

class AttendanceForm(forms.ModelForm):

    class Meta:

        model = Attendance

        fields = [
            'employee',
            'date',
            'status'
        ]

from .models import Leave

class LeaveForm(forms.ModelForm):

    class Meta:

        model = Leave

        fields = [
            'employee',
            'leave_type',
            'start_date',
            'end_date',
            'reason'
        ]