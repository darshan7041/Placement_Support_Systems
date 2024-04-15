from django.urls import path
from placement_app import views
from .views import stu_c_l,stu_r_u_d

urlpatterns = [ 

path('send_email/', views.send_email, name='send_email'),


# <------------------------------ API Only------------------------------->
path('home_app/',stu_c_l.as_view(),name="home_app"),
path('<int:pk>',stu_r_u_d.as_view(),name="home_app"),

path('login_student_app/', views.student_login, name='student_login'),
path('placement_list_app/', views.placement_list_app, name='placement_list'),
path('application_list_app/', views.application_list_app, name='application_list_app'),


# <------------------------------ Admin login Only------------------------------->
path('admin_login/',views.admin_login,name="admin_login"),
path('adminloginsave/',views.adminloginsave,name="adminloginsave"),
path('admin_logout/',views.admin_logout,name="admin_logout"),


path('profile/',views.profile,name="profile"),




# <----------- Login | admin Only------------>

path('main_admin_master/',views.main_admin_master,name="main_admin_master"),
path('admin_home/',views.admin_home,name="admin_home"),

# <----------- Student data | admin Only------------>

path('student_qualification/<int:id>/',views.student_qualification,name="student_qualification"),
path('student_table/',views.student_table,name="student_table"),
path('add_student/',views.add_student,name="add_student"),
path('adding_student/',views.adding_student,name="adding_student"),
path('student_delete/<int:id>/',views.student_delete,name="student_delete"),
path('student_edit/<int:id>/',views.student_edit,name="student_edit"),
path('student_editing/<int:id>/',views.student_editing,name="student_editing"),

path('add_student_ex/',views.add_student_ex,name="add_student_ex"),

# <----------- Company data | admin Only------------>

path('company_table/',views.company_table,name="company_table"),
path('company_delete/<int:id>/',views.company_delete,name="company_delete"),

path('add_company_ex/',views.add_company_ex,name="add_company_ex"),
# <----------- PS report data | admin Only------------>

path('ps_report_table/',views.ps_report_table,name="ps_report_table"),
path('download_ps_report/', views.download_ps_report, name='download_ps_report'),



# <----------- Cource data | admin Only------------>
path('d_c_main/',views.d_c_main,name="d_c_main"),
path('course_list/',views.course_list,name="course_list"),
path('course_add/',views.course_add,name="course_add"),
path('course_adding/',views.course_adding,name="course_adding"),
path('course_edit/<int:id>/',views.course_edit,name="course_edit"),
path('course_editing/<int:id>/',views.course_editing,name="course_editing"),
path('course_delete/<int:id>/',views.course_delete,name="course_delete"),

# <----------- Department data | admin Only------------>
path('department_list/',views.department_list,name="department_list"),
path('department_add/',views.department_add,name="department_add"),
path('department_adding/',views.department_adding,name="department_adding"),
path('department_edit/<int:id>/',views.department_edit,name="department_edit"),
path('department_editing/<int:id>/',views.department_editing,name="department_editing"),
path('department_delete/<int:id>/',views.department_delete,name="department_delete"),


# <----------- application data | admin Only------------>
path('app_search/',views.app_search,name="app_search"),
path('application_list/',views.application_list,name="application_list"),
path('application_add/',views.application_add,name="application_add"),
path('application_adding/',views.application_adding,name="application_adding"),
path('application_edit/<int:id>/',views.application_edit,name="application_edit"),
path('application_editing/<int:id>/',views.application_editing,name="application_editing"),
path('application_delete/<int:id>/',views.application_delete,name="application_delete"),


# <----------- placement data | admin Only------------>
path('place_search/',views.place_search,name="place_search"),
path('placement_list/',views.placement_list,name="placement_list"),
path('placement_add/',views.placement_add,name="placement_add"),
path('placement_adding/',views.placement_adding,name="placement_adding"),
path('placement_edit/<int:id>/',views.placement_edit,name="placement_edit"),
path('placement_editing/<int:id>/',views.placement_editing,name="placement_editing"),
path('placement_delete/<int:id>/',views.placement_delete,name="placement_delete"),

]
