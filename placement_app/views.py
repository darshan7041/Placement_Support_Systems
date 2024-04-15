from django.db import IntegrityError
from django.shortcuts import render,redirect
from placement_app.serialization import *
from .models import *
from django.contrib import messages
from django.contrib.auth import logout as logout
import openpyxl 
import csv
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework import generics
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# <----------------------------- API Only------------------------------>

class stu_c_l(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class stu_r_u_d(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


def student_login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            student = Student.objects.get(email=email, password=password)
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"error": "Invalid request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def placement_list_app(request):
    place = PlacementDetails.objects.all()
    serializer = PlacementDetailsSerializer(place, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def application_list_app(request):
    place = ApplicationTable.objects.all()
    serializer = applicationDetailsSerializer(place, many=True)
    return Response(serializer.data)



# views.py or wherever you want to send the email

# <----------------------------- Email Only------------------------------>

def send_email(request):
    subject = 'Subject of your email'
    message = 'Message of your email'
    sender = 'ds704198@gmail.com'  # Replace with your Gmail address
    recipient = 'darshansolanki0502.com'  # Replace with recipient's email address
    
    # Render the email template with dynamic content
    email_html = render_to_string('admin/email.html', {'subject': subject, 'message': message, 'sender': sender, 'greeting': 'Hello!'})
    
    # Send the email using Gmail SMTP with App Password
    send_mail(
        subject,
        message,
        sender,
        [recipient],
        html_message=email_html,
        fail_silently=False,
        auth_user='ds704198@gmail.com',  # Replace with your Gmail address
        auth_password='darshan14789'  # Replace with your App Password
    )



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
    session_data = request.session.get('a_email')
    if session_data:
        admin = Admin.objects.get(a_email=session_data)
        admin_name = admin.a_name  # Extract admin's name
        print("Admin Name:", admin_name)  # Print admin's name to verify
        return render(request, 'admin/main_admin.html', {'admin_name': admin_name})
    else:
        print("Not logged in")
        return redirect('/admin_login/')

def admin_home(request):
        session_data = request.session.get('a_email')
        if session_data:
                admin = Admin.objects.get(a_email=session_data)
                admin_name = admin.a_name  # Extract admin's name
                print("Admin Name:", admin_name)  # Print admin's name to verify
                return render(request, 'admin/admin_home.html', {'admin_name': admin_name})
        else:
                print("Not logged in")
                return redirect('/admin_login/')




# <-------------- Student data | admin Only--------------->

def student_qualification(request, id):
        session_data = request.session.get('a_email')
        if session_data:
                admin = Admin.objects.get(a_email=session_data)
                admin_name = admin.a_name  
                print("Admin Name:", admin_name)  

                try:
                        sq_list = StudentQualification.objects.get(s=id)
                except StudentQualification.DoesNotExist:
                        # Handle the case when the object does not exist
                        messages.error (request,"Data is not Added.")
                        return redirect('/student_table/')
                return render(request, 'admin/student/student_qualification.html', {'sq': sq_list})

        else:
                print("Not logged in")
                return redirect('/admin_login/')
        


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
        email=request.POST.get('email')
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
       

def student_delete(request, id):
    try:
        s_delete = Student.objects.get(s_id=id)
        s_delete.delete()
    except Student.DoesNotExist:
        messages.error(request, 'Student does not exist.')
    except IntegrityError:
        messages.error(request, 'Cannot delete this student because it is referenced in other tables.')

    return redirect('/student_table/')
 

def add_student_ex(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        
        errors = []
        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            header = next(reader)

            column_mapping = {
                'First_name': 's_f_name',
                'Middle_name': 's_m_name',
                'Last_name': 's_l_name',
                'Enrollment_number': 's_enrollment_number',
                'Phone_number': 's_phone_number',
                'Aadhar_card': 's_aadhar_card',
                'Guardian_mobile_number': 's_guardian_mobile_number',
                'Guardian_email': 's_guardian_email',
                'Email': 's_email',
                'Password': 's_password',
                'Department_id': 'd_id',
                'Course_id': 'course_id',
                'Home_no': 'home_no',
                'Block_no': 'block_no',
                'Flat_society_name': 'flat_society_name',
                'Area': 'area',
                'City': 'city',
            }

            for row in reader:
                mapped_row = {column_mapping.get(header[i], header[i]): row[i] for i in range(len(row))}
                
                print("Mapped Row:", mapped_row) 

                enrollment_number = mapped_row.get('s_enrollment_number')
                if not enrollment_number.isdigit():
                    errors.append(f"Enrollment number '{enrollment_number}' is not a valid integer.")
                    continue 

                try:
                    student = Student.objects.create(**mapped_row)
                except Exception as e:
                    errors.append(f"Error creating student: {e}")

            if not errors:
                messages.success(request, 'CSV file uploaded successfully.')
            else:
                messages.error(request, 'Errors occurred while processing the CSV file: {}'.format(', '.join(errors)))
        except Exception as e:
            messages.error(request, f"An error occurred while processing the CSV file: {e}")
        
        return redirect('student_table')

    return render(request, 'admin/student/add_student.html') 


def student_edit(request,id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        
        d_show=Student.objects.get(s_id=id)  
        return render(request,'admin/student/edit.html',{'show_d':d_show})

def student_editing(request,id):
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

        studetn_add=Student(s_id=id,s_f_name=f_n,
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

def add_company_ex(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        
        errors = []

        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)

            header = next(reader)

            column_mapping = {
                'Company_name': 'c_name',
                'Industry_company': 'c_industry',
                'Email': 'c_email',
                'Contact_number': 'c_contact_no',
                'URL': 'c_url',
                'Company_no': 'company_no',
                'Company_area': 'area',
                'Company_city': 'city',
            }

            for row in reader:
                
                mapped_row = {column_mapping.get(header[i], header[i]): row[i] for i in range(len(row))}
                
                print("Mapped Row:", mapped_row) 

                try:
                    company = CompanyRegistration.objects.create(**mapped_row)
                except Exception as e:
                    errors.append(str(e))
        except Exception as e:
            errors.append(str(e))
        
        if errors:
            messages.error(request, 'Errors occurred while processing the CSV file: {}'.format(', '.join(errors)))
        else:
            messages.success(request, 'CSV file uploaded successfully.')
        
        return redirect('company_table')

    return render(request, 'add_company.html')


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
    
    ps_reports = PsReport.objects.all()


    wb = openpyxl.Workbook()
    ws = wb.active


    headers = ['PS_id', 'Student Name', 'Company Name', 'PS Date', 'Performance', 'Status']
    ws.append(headers)


    for ps_report in ps_reports:
        ws.append([
            ps_report.ps_id,
            ps_report.s.s_f_name if ps_report.s else '',  # Assuming 'name' is a field in the Student model
            ps_report.c.c_name if ps_report.c else '',  # Assuming 'name' is a field in the Company model
            ps_report.ps_date.strftime('%Y-%m-%d') if ps_report.ps_date else '',
            ps_report.ps_performance,
            ps_report.ps_status
        ])


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




# <-------------- Application | admin Only--------------->


def app_search(request):
    session_data = request.session.get('a_email')
    if not session_data:
        print("Not logged in")
        return redirect('/admin_login/')

    if request.method == 'POST':
        search_term = request.POST.get('search')
        d_list = ApplicationTable.objects.filter(c__c_name=search_term) | ApplicationTable.objects.filter(s__s_f_name=search_term) | ApplicationTable.objects.filter(ap_status=search_term) | ApplicationTable.objects.filter(pd__pd_title=search_term)

    else:
        d_list = ApplicationTable.objects.all()

    return render(request, 'admin/application/application_list.html', {'d_lists': d_list})




def application_list(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        d_list = ApplicationTable.objects.all()
        return render(request,'admin/application/application_list.html',{'d_lists':d_list})


def application_add(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        
        return render(request,'admin/application/add_application.html')

def application_adding(request):
        name=request.POST.get('name')
        studetn_add=ApplicationTable(d_name=name)
        studetn_add.save()
        return redirect('/application_list/')


def application_edit(request,id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        
        d_show=ApplicationTable.objects.get(ap_id=id) 
        studentList = Student.objects.all()
        comp = CompanyRegistration.objects.all()
        pd = PlacementDetails.objects.all()
        return render(request,'admin/application/edit_application.html',
                {'show_d':d_show,'studentList':studentList,'comp':comp,'pd':pd})

def application_editing(request,id):
        stud=request.POST.get('student')
        st=Student.objects.get(s_f_name=stud)

        com=request.POST.get('company')
        co=CompanyRegistration.objects.get(c_name=com)

        place=request.POST.get('placement')
        pl=PlacementDetails.objects.get(pd_title=place)
        
        date=request.POST.get('date')
        status=request.POST.get('status')

        app_add=ApplicationTable(ap_id=id,s=st,c=co,pd=pl,ap_date=date,ap_status=status)
        app_add.save()
        return redirect('/application_list/')




def application_delete(request,id):
        ddelete=ApplicationTable.objects.get(ap_id=id)
        ddelete.delete()
        return redirect('/application_list/')


# <-------------- Placement Details | admin Only--------------->

def place_search(request):
        session_data = request.session.get('a_email')
        if not session_data:
                print("Not logged in")
                return redirect('/admin_login/')

        if request.method == 'POST':
                search_term = request.POST.get('search')
                place = PlacementDetails.objects.filter(c__c_name=search_term) | PlacementDetails.objects.filter(pd_title=search_term)

        else:
                place = PlacementDetails.objects.all()

        return render(request,'admin/placement_details/placement_list.html',{'pla':place})


def placement_list(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        place = PlacementDetails.objects.all()
        return render(request,'admin/placement_details/placement_list.html',{'pla':place})


def placement_add(request):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        return render(request,'admin/placement_details/add_placement.html')

def placement_adding(request):
        name=request.POST.get('name')
        studetn_add=PlacementDetails(d_name=name)
        studetn_add.save()
        return redirect('/placement_list/')


def placement_edit(request,id):
        session_data=request.session.get('a_email')
        if session_data:
                print("welcome",session_data)
        else:
                print("not login")
                return redirect('/admin_login/')
        
        d_show=PlacementDetails.objects.get(ap_id=id)  
        return render(request,'admin/placement_details/edit_placement.html',{'show_d':d_show})

def placement_editing(request,id):
        name=request.POST.get('name')
        studetn_add=PlacementDetails(ap_id=id,d_name=name)
        studetn_add.save()
        return redirect('/placement_list/')



def placement_delete(request,id):
        ddelete=PlacementDetails.objects.get(pd_id=id)
        ddelete.delete()
        return redirect('/placement_list/')







# <------------------------ Student Only------------------------->

# <------------------------ Company Only------------------------->

