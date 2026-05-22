from django.db import models

class Employee(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.name
class Attendance(models.Model):

    objects = None
    STATUS_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    def __str__(self):
        return f"{self.employee.name} - {self.date}"

class Leave(models.Model):

    objects = None
    LEAVE_TYPES = (
        ('Sick Leave', 'Sick Leave'),
        ('Casual Leave', 'Casual Leave'),
    )

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    leave_type = models.CharField(
        max_length=20,
        choices=LEAVE_TYPES
    )

    start_date = models.DateField()

    end_date = models.DateField()

    reason = models.TextField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return f"{self.employee.name} - {self.leave_type}"