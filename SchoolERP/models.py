from __future__ import unicode_literals

from django.db import models

class Batch(models.Model):
    batch_id = models.AutoField(primary_key=True, max_length=45)
    batch = models.CharField(max_length=45, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True, auto_now=True)
    
    def __str__(self):
        return self.batch

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'batch'


class BatchClassSection(models.Model):
    batch_class_section_id = models.AutoField(primary_key=True, max_length=45)
    batch_class = models.ForeignKey('BatchClasses', models.DO_NOTHING, blank=True, null=True)
    class_sec = models.ForeignKey('Sections',models.DO_NOTHING, db_column="sec_id" ,blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'batch_class_section'
        
   
class BatchClasses(models.Model):
    batch_class_id = models.AutoField(primary_key=True, max_length=45)
    batch = models.ForeignKey('Batch', models.DO_NOTHING,db_column='batch_id' ,blank=True, null=True)
    grade = models.ForeignKey('Class', models.DO_NOTHING,db_column='grade_id' , blank=True, null=True)  # Field renamed because it was a Python reserved word.
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'batch_classes'

class City(models.Model):
    city_id = models.CharField(primary_key=True, max_length=45)
    city = models.CharField(max_length=45, blank=True, null=True)
    state = models.ForeignKey('State', models.DO_NOTHING, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.city  
     
    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'city'


class Class(models.Model):
    class_id = models.AutoField(primary_key=True, max_length=45)
    class_field = models.CharField(db_column='class', max_length=5, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    
    def __str__(self):
        return self.class_field  

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'class'


class ClassSection(models.Model):
    class_sec_id = models.AutoField(primary_key=True, max_length=45)
    class_field = models.ForeignKey(Class, models.DO_NOTHING, db_column='class_id', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    section = models.ForeignKey('Sections', models.DO_NOTHING, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True,auto_now=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'class_section'
        


class ClassSubject(models.Model):
    class_subject_id = models.AutoField(primary_key=True, max_length=45)
    grade = models.ForeignKey('Class', models.DO_NOTHING, blank=True, null=True)
    subject = models.ForeignKey('Subject', models.DO_NOTHING, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True,auto_now=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'class_subject'


class ExamTypeSyllabus(models.Model):
    exmaType_syll_id = models.AutoField(primary_key=True, max_length=45)
    exam_type = models.ForeignKey('ExamType', models.DO_NOTHING, blank=True, null=True)
    syllabus = models.ForeignKey('Syllabus', models.DO_NOTHING, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True,auto_now=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'exam_type_syllabus'

class Period(models.Model):
    period_id = models.AutoField(primary_key=True, max_length=45)
    period = models.CharField(max_length=20, blank=True, null=True)
    from_time = models.TimeField(blank=True, null=True)
    to_time = models.TimeField(blank=True, null=True)
    class Meta:
        managed = False
        app_label = 'period'
        db_table = 'period'
        
    def __str__(self):
        return self.period
    
class ClassTeacher(models.Model):
    class_teacher_id = models.AutoField(primary_key=True, max_length=45)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING, blank=True, null=True)
    batch_class_sec = models.ForeignKey(BatchClassSection, models.DO_NOTHING, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True,auto_now=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'class_teacher'


class ClassTeacherSubject(models.Model):
    class_teacher_sub_id = models.AutoField(primary_key=True, max_length=45)
    class_teacher = models.ForeignKey(ClassTeacher, models.DO_NOTHING, blank=True, null=True)
    class_subject = models.ForeignKey(ClassSubject, models.DO_NOTHING, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    batch_class = models.ForeignKey(BatchClasses, models.DO_NOTHING, db_column='batch_class_id',blank=True, null=True)
    batch_class_sec = models.ForeignKey(BatchClassSection, models.DO_NOTHING,db_column='batch_class_section_id', blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'class_teacher_subject'


class ClassTimetable(models.Model):
    class_timetable_id = models.AutoField(primary_key=True, max_length=45)
    class_subject = models.ForeignKey(ClassSubject, models.DO_NOTHING, blank=True, null=True)
    day = models.CharField(max_length=10, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    class_section = models.ForeignKey(ClassSection,models.DO_NOTHING,blank=True,null=True)
    period = models.ForeignKey(Period, models.DO_NOTHING,blank=True,null=True)
    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'class_timetable'



class ExamAssign(models.Model):
    exam_assign_id = models.AutoField(primary_key=True, max_length=45)
    class_sub_syll = models.ForeignKey(ExamTypeSyllabus, models.DO_NOTHING, blank=True, null=True)
    from_time = models.TimeField(blank=True, null=True)
    to_time = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    day = models.CharField(max_length=10, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True,auto_now=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'exam_assign'


class ExamType(models.Model):
    exam_type_id = models.AutoField(primary_key=True, max_length=45)
    exam_type = models.CharField(max_length=45, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True,auto_now=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'exam_type'
        
    def __str__(self):
        return self.exam_type  


class Parent(models.Model):
    parent_id = models.AutoField(primary_key=True, max_length=45)
    fatherName = models.CharField(max_length=45, blank=True, null=True)
    motherName = models.CharField(max_length=45, blank=True, null=True)
    guardianName = models.CharField(max_length=45, blank=True, null=True)
    fatherContactNo = models.BigIntegerField(blank=True, null=True)
    motherContactNo = models.BigIntegerField(blank=True, null=True)
    guardianContactNo = models.BigIntegerField(blank=True, null=True)
    fatherEmailAddr = models.CharField(max_length=100, blank=True, null=True)
    motherEmailAddr = models.CharField(max_length=100, blank=True, null=True)
    guardianEmailAddr = models.CharField(max_length=100, blank=True, null=True)
    createUser = models.CharField(max_length=20, blank=True, null=True)
    createDate = models.DateTimeField(blank=True, null=True)
    updateUser = models.CharField(max_length=20, blank=True, null=True)
    updateDate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'parent'


class ParentStudent(models.Model):
    parent_student_id = models.AutoField(primary_key=True, max_length=45)
    parent = models.ForeignKey(Parent, models.DO_NOTHING, blank=True, null=True)
    student = models.ForeignKey('Student', models.DO_NOTHING, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'parent_student'


class Principal(models.Model):
    principal_id = models.AutoField(primary_key=True, max_length=45)
    principal_name = models.CharField(max_length=45, blank=True, null=True)
    principal_contact_no = models.CharField(max_length=45, blank=True, null=True)
    principal_email_addr = models.CharField(max_length=100, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'principal'


class School(models.Model):
    school_code = models.AutoField(primary_key=True, max_length=45)
    school_name = models.CharField(max_length=45, blank=True, null=True)
    branch = models.CharField(max_length=45, blank=True, null=True)
    census_code = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    fax_no = models.BigIntegerField(blank=True, null=True)
    telephone_no = models.BigIntegerField(blank=True, null=True)
    email_address = models.CharField(max_length=100, blank=True, null=True)
    website_url = models.CharField(max_length=45, blank=True, null=True)
    principal = models.ForeignKey(Principal, models.DO_NOTHING, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'school'


class Sections(models.Model):
    sectionId = models.AutoField(primary_key=True, max_length=20,db_column='section_id')
    section = models.CharField(max_length=1, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True,auto_now=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'sections'

    def __str__(self):
        return self.section
    

class State(models.Model):
    state_id = models.CharField(primary_key=True, max_length=45)
    state_name = models.CharField(max_length=45, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.state_name

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'state'

class PreviousInstituteDetails(models.Model):
    previous_institute_id = models.AutoField(primary_key=True)
    institute_name = models.CharField(max_length=45, blank=True, null=True)
    last_class_attended = models.CharField(max_length=45, blank=True, null=True)
    duration = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'previous_institute_details'
        

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=45, blank=True, null=True)
    lastName = models.CharField(max_length=45, blank=True, null=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    batch_class_sec = models.ForeignKey(BatchClassSection, models.DO_NOTHING, blank=True, null=True)
    contactNo = models.BigIntegerField(blank=True, null=True)
    aadhaarNo = models.CharField(max_length=40, blank=True, null=True)
    admissionNo = models.CharField(max_length=45, blank=True, null=True)
    dateOfAdmission = models.DateField(blank=True, null=True)
    category = models.CharField(max_length=10, blank=True, null=True)
    motherTongue = models.CharField(max_length=20, blank=True, null=True)
    createUser = models.CharField(max_length=20, blank=True, null=True)
    createDate = models.DateTimeField(blank=True, null=True)
    updateUser = models.CharField(max_length=20, blank=True, null=True)
    updateDate = models.DateTimeField(blank=True, null=True)
    student_pic = models.CharField(blank=True, null=True)
    previous_institute = models.ForeignKey(PreviousInstituteDetails, models.DO_NOTHING, db_column='previous_institute_id', blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'student'
    
    
class StudentAddress(models.Model):
    stud_addr_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    student = models.ForeignKey(Student, models.DO_NOTHING, blank=True, null=True)
    flatNo = models.CharField(max_length=45, blank=True, null=True)
    street1 = models.CharField(max_length=45, blank=True, null=True)
    street2 = models.CharField(max_length=45, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    pincode = models.BigIntegerField(blank=True, null=True)
    state = models.ForeignKey(State, models.DO_NOTHING, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True ,blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'student_address'


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True, max_length=45)
    subject = models.CharField(max_length=45, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True,auto_now=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'subject'


class Syllabus(models.Model):
    syllabus_id = models.AutoField(primary_key=True, max_length=45)
    class_subject = models.ForeignKey(ClassSubject, models.DO_NOTHING, blank=True, null=True)
    syllabus = models.CharField(max_length=45, blank=True, null=True)
    topic = models.CharField(max_length=45, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    exam_type = models.ForeignKey(ExamType, models.DO_NOTHING, db_column='exam_type_id',blank=True, null=True)
    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'syllabus'


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True, max_length=45)
    teacher_first_name = models.CharField(max_length=45, blank=True, null=True)
    teacher_last_name = models.CharField(max_length=45, blank=True, null=True)
    teacher_contact_no = models.BigIntegerField(blank=True, null=True)
    teacher_email_id = models.CharField(max_length=100, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True,auto_now=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'teacher'



    
class TeacherTimetable(models.Model):
    teacher_timetable_id = models.AutoField(primary_key=True, max_length=45)
    class_teacher_sub = models.ForeignKey(ClassTeacherSubject, models.DO_NOTHING, blank=True, null=True)
    day = models.CharField(max_length=10, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    period = models.ForeignKey(Period, models.DO_NOTHING,blank=True,null=True)
    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'teacher_timetable'
        
class Assignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    #batch_class = models.ForeignKey('BatchClasses', models.DO_NOTHING, db_column='batch_class', blank=True, null=True)
    syllabus = models.ForeignKey('Syllabus', models.DO_NOTHING, db_column='syllabus', blank=True, null=True)
    assignment_description = models.CharField(max_length=100, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    create_user = models.CharField(max_length=45, blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'assignment'

class Homework(models.Model):
    homework_id = models.AutoField(primary_key=True)
    batch_class_section = models.ForeignKey(BatchClassSection, models.DO_NOTHING, db_column='batch_class_section', blank=True, null=True)
    syllabus = models.ForeignKey('Syllabus', models.DO_NOTHING, db_column='syllabus', blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    homework_description = models.CharField(max_length=100, blank=True, null=True)
    create_user = models.CharField(max_length=45, blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'homework'

class ExamResult(models.Model):
    exam_result_id = models.AutoField(primary_key=True)
    exam_assign = models.ForeignKey(ExamAssign, models.DO_NOTHING, db_column='exam_assign', blank=True, null=True)
    student = models.ForeignKey(Student, models.DO_NOTHING, db_column='student',blank=True, null=True)
    marks_obtained = models.FloatField(blank=True, null=True)
    total_marks = models.FloatField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'exam_result'
              
    def __str__(self):
        return str(self.exam_result_id) 
    
class Ranking(models.Model):
    ranking_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING,db_column='student_id', blank=True, null=True)
    exam_type = models.ForeignKey(ExamType, models.DO_NOTHING, db_column='exam_type', blank=True, null=True)
    total_marks = models.IntegerField(blank=True, null=True)
    marks_obtained = models.FloatField(blank=True, null=True)
    percentage_marks = models.FloatField(blank=True, null=True)
    ranking = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    
    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'ranking'




class StudentAttendance(models.Model):
    student_attendance_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    attendance = models.CharField(max_length=1, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    
    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'student_attendance'
        
        
class TeacherAttendance(models.Model):
    teacher_attendance_id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    attendance = models.CharField(max_length=1, blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    
    class Meta:
        managed = False
        app_label = 'school'
        db_table = 'teacher_attendance'