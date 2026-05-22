from django.urls import path
from . import views

urlpatterns = [

    path('', views.employee_list, name='employee_list'),

    path('add/',
         views.add_employee,
         name='add_employee'),

    path('edit/<int:id>/',
         views.edit_employee,
         name='edit_employee'),

    path('delete/<int:id>/',
         views.delete_employee,
         name='delete_employee'),

    path('login/',
     views.login_user,
     name='login'),

    path('logout/',
     views.logout_user,
     name='logout'),

path('attendance/',
     views.attendance_list,
     name='attendance_list'),

path('attendance/add/',
     views.add_attendance,
     name='add_attendance'),

path('leave/',
     views.leave_list,
     name='leave_list'),

path('leave/add/',
     views.add_leave,
     name='add_leave'),

path('leave/approve/<int:id>/',
     views.approve_leave,
     name='approve_leave'),

path('leave/reject/<int:id>/',
     views.reject_leave,
     name='reject_leave'),


path('dashboard/',
     views.dashboard,
     name='dashboard'),
]
