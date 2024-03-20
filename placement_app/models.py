# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    a_id = models.AutoField(primary_key=True)
    a_email = models.CharField(max_length=40, blank=True, null=True)
    a_password = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class ApplicationTable(models.Model):
    ap_id = models.AutoField(primary_key=True)
    s = models.ForeignKey('Student', models.DO_NOTHING, blank=True, null=True)
    c = models.ForeignKey('CompanyRegistration', models.DO_NOTHING, blank=True, null=True)
    pd = models.ForeignKey('PlacementDetails', models.DO_NOTHING, blank=True, null=True)
    ap_date = models.DateField(blank=True, null=True)
    ap_status = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_table'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CompanyRegistration(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=100, blank=True, null=True)
    c_industry = models.CharField(max_length=60, blank=True, null=True)
    c_contact_no = models.IntegerField(blank=True, null=True)
    c_email = models.CharField(max_length=50, blank=True, null=True)
    c_url = models.CharField(db_column='c_URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c_location = models.CharField(max_length=450, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_registration'


class Cource(models.Model):
    course_id = models.AutoField(primary_key=True)
    d = models.ForeignKey('Department', models.DO_NOTHING, blank=True, null=True)
    course_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cource'


class Department(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=40)

    def __str__(self):
        return self.d_name

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PlacementDetails(models.Model):
    pd_id = models.AutoField(primary_key=True)
    c = models.ForeignKey(CompanyRegistration, models.DO_NOTHING, blank=True, null=True)
    pd_title = models.CharField(max_length=40, blank=True, null=True)
    pd_date_of_placement = models.DateField(blank=True, null=True)
    pd_eligibility_criteria = models.CharField(max_length=70, blank=True, null=True)
    pd_description = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'placement_details'


class PsReport(models.Model):
    ps_id = models.AutoField(primary_key=True)
    s = models.ForeignKey('Student', models.DO_NOTHING, blank=True, null=True)
    c = models.ForeignKey(CompanyRegistration, models.DO_NOTHING, blank=True, null=True)
    ps_placed_date = models.DateField(blank=True, null=True)
    ps_status = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ps_report'


class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_f_name = models.CharField(max_length=15, blank=True, null=True)
    s_m_name = models.CharField(max_length=15, blank=True, null=True)
    s_l_name = models.CharField(max_length=15, blank=True, null=True)
    s_enrollment_number = models.IntegerField(blank=True, null=True)
    s_phone_number = models.IntegerField(blank=True, null=True)
    s_aadhar_card = models.IntegerField(blank=True, null=True)
    s_guardian_mobile_number = models.IntegerField(blank=True, null=True)
    s_guardian_email = models.CharField(max_length=40, blank=True, null=True)
    s_email = models.CharField(max_length=40, blank=True, null=True)
    s_password = models.CharField(max_length=40, blank=True, null=True)
    d = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    course = models.ForeignKey(Cource, models.DO_NOTHING, blank=True, null=True)
    s_address_permanent = models.CharField(max_length=300, blank=True, null=True)
    s_address_temporary = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class StudentQualification(models.Model):
    sq_id = models.AutoField(primary_key=True)
    s = models.ForeignKey(Student, models.DO_NOTHING, blank=True, null=True)
    sq_ssc_total_marks = models.IntegerField(blank=True, null=True)
    sq_ssc_obtained_marks = models.IntegerField(blank=True, null=True)
    sq_ssc_percentage = models.FloatField(blank=True, null=True)
    sq_hsc_total_marks = models.IntegerField(blank=True, null=True)
    sq_hsc_obtained_marks = models.IntegerField(blank=True, null=True)
    sq_hsc_percentage = models.FloatField(blank=True, null=True)
    sq_bachelor_cgpa = models.FloatField(db_column='sq_bachelor_CGPA', blank=True, null=True)  # Field name made lowercase.
    sq_bachelor_percentage = models.FloatField(blank=True, null=True)
    sq_bachelor_degree = models.CharField(max_length=40, blank=True, null=True)
    sq_bachelor_university = models.CharField(max_length=60, blank=True, null=True)
    sq_master_sem_1 = models.FloatField(blank=True, null=True)
    sq_master_sem_2 = models.FloatField(blank=True, null=True)
    sq_master_sem_3 = models.FloatField()
    sq_master_sem_4 = models.FloatField()
    sq_9th_percentage = models.FloatField()
    sq_11th_percentage = models.FloatField()

    class Meta:
        managed = False
        db_table = 'student_qualification'
