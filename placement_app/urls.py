from django.urls import path
from placement_app import views


urlpatterns = [ 


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


# <----------- Company data | admin Only------------>

path('company_table/',views.company_table,name="company_table"),
path('company_delete/<int:id>/',views.company_delete,name="company_delete"),

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

]
