from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import logout as logout
import openpyxl 
from django.http import HttpResponse

# Create your views here.


# <----------------------------- Admin login Only------------------------------>
def admin_login(request):
        return render(request,'admin/admin_logins.html')
def profile(request):
        return render(request,'admin/profile.html')

def admin_logout(request):
        logout(request)
        print("not login")
        messages.error(request,"You have successfully logout")
        return redirect('/admin_login/')


def adminloginsave(request):
    if request.method == 'POST': 
        ademail=request.POST.get('email')
        adpass=request.POST.get('password')
        admin1=Admin.objects.filter(a_email=ademail,a_password=adpass)
        if admin1:
            request.session['a_email']=ademail
        #     messages.success(request,"you are successfully login")
            return redirect('/admin_home/')
        else:
            messages.error(request,"You have Invalid Email or Password")
            return redirect('/admin_login/')
    else:
        return render(request,'admin/admin_logins.html')
    


# <------------------------ Admin Only------------------------->

def main_admin_master(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        

        admin_id_to_show = request.session.get('a_email')
        # admins = AdminCollege.objects.get(a_email = admin_id_to_show)
        return render(request,'admin/main_admin.html',{'adminss':admin_id_to_show})

def admin_home(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        return render(request,'admin/admin_home.html')




# <-------------- Student data | admin Only--------------->

def student_qualification(request, id):
    session_data = request.session.get('a_email')
    if session_data:
        print("welcome", session_data)
    else:
        print("not login")
        return redirect('/admin_login/')
    
    try:
        sq_list = StudentQualification.objects.get(s=id)
    except StudentQualification.DoesNotExist:
        # Handle the case when the object does not exist
        return HttpResponse("Student qualification with the given ID does not exist.")
    
    return render(request, 'admin/student/student_qualification.html', {'sq': sq_list})


def student_table(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        
        st_list=Student.objects.all()
        return render(request,'admin/student/student_table.html',{'student_list':st_list})


def add_student(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        return render(request,'admin/student/add_student.html')

def adding_student(request):
        
        f_n=request.POST.get('f_name')
        m_n=request.POST.get('m_name')
        l_n=request.POST.get('l_name')
        enroll_num=request.POST.get('enrollment_num')
        mobile=request.POST.get('phone_number')
        email=request.POST.get('email')




        
        # aadhar_card=request.POST.get('aadhar_card')
        # g_mobile_num=request.POST.get('g_mobile_num')
        # g_email=request.POST.get('g_email')
        # password=request.POST.get('password')
        # depart=request.POST.get('department')
        # cource=request.POST.get('cource')
        # address_per=request.POST.get('address_per')
        # address_temp=request.POST.get('address_temp')

        studetn_add=Student(s_f_name=f_n,
                               s_m_name=m_n,
                               s_l_name=l_n,
                               s_enrollment_number=enroll_num,
                               s_phone_number=mobile,
                               s_email=email)
                        #        s_aadhar_card=aadhar_card,
                        #        s_guardian_mobile_number=g_mobile_num,
                        #        s_guardian_email=g_email,
                        #        s_password=password,
                        #        d=depart,
                        #        cource=cource,
                        #        s_address_permanent=address_per,
                        #        s_address_temporary=address_temp
        studetn_add.save()
        messages.success(request,"Data is Added.")
        return redirect('/add_student/')
       

def student_delete(request,id):
        s_delete=Student.objects.get(s_id=id)
        s_delete.delete()
        return redirect('/student_table/')




# <-------------- Company data | admin Only--------------->

def company_table(request): 
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        c_list=CompanyRegistration.objects.all()
        return render(request,'admin/company/company_table.html',{'company_list':c_list})

def company_delete(request,id):
        c_delete=CompanyRegistration.objects.get(c_id=id)
        c_delete.delete()
        return redirect('/company_table/')




# <-------------- PS report data | admin Only--------------->


def ps_report_table(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        
        ps_list=PsReport.objects.all()
        return render(request,'admin/ps_report_table.html',{'PS_report_list':ps_list})


def download_ps_report(request):
    # Fetching data from database
    ps_reports = PsReport.objects.all()

    # Creating new xl
    wb = openpyxl.Workbook()
    ws = wb.active

    # Write header row
    headers = ['PS_id', 'Student Name', 'Company Name', 'PS Date', 'Performance', 'Status']
    ws.append(headers)

    # Write data rows
    for ps_report in ps_reports:
        ws.append([
            ps_report.ps_id,
            ps_report.s.s_f_name if ps_report.s else '',  # Assuming 'name' is a field in the Student model
            ps_report.c.c_name if ps_report.c else '',  # Assuming 'name' is a field in the Company model
            ps_report.ps_date.strftime('%Y-%m-%d') if ps_report.ps_date else '',
            ps_report.ps_performance,
            ps_report.ps_status
        ])

    # Save the workbook
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=ps_reports.xlsx'
    wb.save(response)

    return response



# <-------------- Cource | admin Only--------------->


def d_c_main(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        return render(request,'admin/Extra/d_c_main.html')

def course_list(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        c_list = Cource.objects.all()
        return render(request,'admin/Extra/cource_list.html',{'c_lists':c_list})


def course_add(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        dept=Department.objects.all()
        return render(request,'admin/Extra/add_cource.html',{'dept':dept})

def course_adding(request):
        name=request.POST.get('name')
        cat2=request.POST.get('cat12')
        cat1=Department.objects.get(d_id=cat2)

        studetn_add=Cource(course_name=name,d=cat1)
        studetn_add.save()
        return redirect('/course_list/')


def course_edit(request,id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        
        c_show=Cource.objects.get(course_id=id)  
        d_show=Department.objects.all()
        return render(request,'admin/Extra/edit_cource.html',{'show_d':c_show,'d_show1':d_show})

def course_editing(request,id):
        name=request.POST.get('name')
        cat2=request.POST.get('cat12')
        cat1=Department.objects.get(d_id=cat2)

        studetn_add=Cource(course_id=id,course_name=name,d=cat1)
        studetn_add.save()
        return redirect('/course_list/')



def course_delete(request,id):
        ddelete=Cource.objects.get(course_id=id)
        ddelete.delete()
        return redirect('/course_list/')


# <-------------- Department | admin Only--------------->


def department_list(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        d_list = Department.objects.all()
        return render(request,'admin/Extra/department/department_list.html',{'d_lists':d_list})


def department_add(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        return render(request,'admin/Extra/department/add_department.html')

def department_adding(request):
        name=request.POST.get('name')
        studetn_add=Department(d_name=name)
        studetn_add.save()
        return redirect('/department_list/')


def department_edit(request,id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        
        d_show=Department.objects.get(d_id=id)  
        return render(request,'admin/Extra/department/edit_department.html',{'show_d':d_show})

def department_editing(request,id):
        name=request.POST.get('name')
        studetn_add=Department(d_id=id,d_name=name)
        studetn_add.save()
        return redirect('/department_list/')



def department_delete(request,id):
        ddelete=Department.objects.get(d_id=id)
        ddelete.delete()
        return redirect('/department_list/')







# <------------------------ Student Only------------------------->

# <------------------------ Company Only------------------------->