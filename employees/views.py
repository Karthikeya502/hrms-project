from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from .models import Attendance
from .forms import AttendanceForm
from .models import Leave
from .forms import LeaveForm
from datetime import date
from django.http import HttpResponse

def is_hr(user):

    return user.groups.filter(
        name='HR'
    ).exists()
@login_required
def employee_list(request):

    employees = Employee.objects.all()

    search = request.GET.get('search')

    department = request.GET.get('department')

    if search:

        employees = employees.filter(
            name__icontains=search
        )

    if department:

        employees = employees.filter(
            department=department
        )

    context = {

        'employees': employees
    }

    return render(
        request,
        'employees/employee_list.html',
        context
    )
@login_required
def add_employee(request):

    if request.method == 'POST':

        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('employee_list')

    else:
        form = EmployeeForm()

    return render(request,
                  'employees/add_employee.html',
                  {'form': form})

@login_required
def edit_employee(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == 'POST':

        form = EmployeeForm(request.POST,
                            instance=employee)

        if form.is_valid():
            form.save()

            return redirect('employee_list')

    else:
        form = EmployeeForm(instance=employee)

    return render(request,
                  'employees/edit_employee.html',
                  {'form': form})
@login_required
def delete_employee(id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('employee_list')

def login_user(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/employees/dashboard/')

        else:

            return render(
                request,
                'employees/login.html',
                {
                    'error': 'Invalid username or password'
                }
            )

    return render(
        request,
        'employees/login.html'
    )
def logout_user(request):

    logout(request)

    return redirect('login')

@login_required
def attendance_list(request):

    attendance = Attendance.objects.all()

    return render(request,
                  'employees/attendance_list.html',
                  {'attendance': attendance})

@login_required
def add_attendance(request):

    if request.method == 'POST':

        form = AttendanceForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('attendance_list')

    else:

        form = AttendanceForm()

    return render(request,
                  'employees/add_attendance.html',
                  {'form': form})

@login_required
def leave_list(request):

    leaves = Leave.objects.all()

    return render(request,
                  'employees/leave_list.html',
                  {'leaves': leaves})

@login_required
def add_leave(request):

    if request.method == 'POST':

        form = LeaveForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('leave_list')

    else:

        form = LeaveForm()

    return render(request,
                  'employees/add_leave.html',
                  {'form': form})

@login_required
def approve_leave(request, id):

    if not is_hr(request.user):

        return HttpResponse(
            "Access Denied"
        )

    leave = Leave.objects.get(id=id)

    leave.status = 'Approved'

    leave.save()

    return redirect('leave_list')


@login_required
def reject_leave(request, id):

    if not is_hr(request.user):

        return HttpResponse(
            "Access Denied"
        )

    leave = Leave.objects.get(id=id)

    leave.status = 'Rejected'

    leave.save()

    return redirect('leave_list')

@login_required
def dashboard(request):

    total_employees = Employee.objects.count()

    present_today = Attendance.objects.filter(
        date=date.today(),
        status='Present'
    ).count()

    absent_today = Attendance.objects.filter(
        date=date.today(),
        status='Absent'
    ).count()

    pending_leaves = Leave.objects.filter(
        status='Pending'
    ).count()

    context = {

        'total_employees': total_employees,
        'present_today': present_today,
        'absent_today': absent_today,
        'pending_leaves': pending_leaves,
    }

    return render(request,
                  'employees/dashboard.html',
                  context)

@login_required
def delete_employee(request, id):

    if not is_hr(request.user):

        return HttpResponse(
            "Access Denied"
        )

    employee = Employee.objects.get(id=id)

    employee.delete()

    return redirect('employee_list')

@login_required
def dashboard(request):

    total_employees = Employee.objects.count()

    total_attendance = Attendance.objects.count()

    pending_leaves = Leave.objects.filter(
        status='Pending'
    ).count()

    approved_leaves = Leave.objects.filter(
        status='Approved'
    ).count()

    context = {

        'total_employees': total_employees,

        'total_attendance': total_attendance,

        'pending_leaves': pending_leaves,

        'approved_leaves': approved_leaves,
    }

    return render(
        request,
        'employees/dashboard.html',
        context
    )

@login_required
def employee_attendance(request):

    employee = Employee.objects.get(
        user=request.user
    )

    attendance_records = Attendance.objects.filter(
        employee=employee
    )

    context = {

        'attendance_records': attendance_records
    }

    return render(
        request,
        'employees/employee_attendance.html',
        context
    )

@login_required
def employee_leave_list(request):

    employee = Employee.objects.get(
        user=request.user
    )

    leaves = Leave.objects.filter(
        employee=employee
    )

    context = {

        'leaves': leaves
    }

    return render(
        request,
        'employees/employee_leave_list.html',
        context
    )

@login_required
def employee_profile(request):

    employee = Employee.objects.get(
        user=request.user
    )

    return render(
        request,
        'employees/employee_profile.html',
        {'employee': employee}
    )
@login_required
def employee_dashboard(request):

    return render(
        request,
        'employees/employee_dashboard.html'
    )