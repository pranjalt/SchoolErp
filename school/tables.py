'''
Created on 12-Jan-2016

@author: VKCSL0010
'''
from SchoolERP.models import *
from table import Table

from table.columns import Column

class SectionTable(Table):
    section_id = Column(field='sectionId',header='SNO')
    sectionName = Column(field='section',header='SECTION NAME')
    creatUser = Column(field='create_user',header='CREATE USER')
    createDate = Column(field='create_date',header='CREATE DATE')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit','title':'Edit'},sortable=False)
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view','title':'View'},sortable=False)
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal','title':'Delete'},sortable=False)
    
class TeacherTable(Table):
    teacher_id = Column(field='teacher_id',header='TEACHER ID')
    teacher_first_name = Column(field='teacher_first_name',header='FIRST NAME')
    teacher_last_name = Column(field='teacher_last_name',header='LAST NAME')
    teacher_email_id = Column(field='teacher_email_id',header='EMAIL ID')
    teacher_contact_no = Column(field='teacher_contact_no',header='CONTACT NUMBER')
    create_user = Column(field='create_user',header='CREATE USER')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit','title':'Edit'},sortable=False)
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view','title':'View'},sortable=False)
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#delTeacherModal','title':'Delete'},sortable=False) 

class SyllabusTable(Table):
    syllabus_id = Column(field='syllabus_id',header='SYLLABUS ID')
    syllabus = Column(field='syllabus',header='SYLLABUS NAME')
    creatUser = Column(field='create_user',header='CREATE USER')
    createDate = Column(field='create_date',header='CREATE DATE')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit','title':'Edit'},sortable=False)
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view','title':'View'},sortable=False)
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal','title':'Delete'},sortable=False)
    
class BatchTable(Table):
    batch_id = Column(field='batch_id',header='BATCH ID')
    batch_name = Column(field='batch',header='BATCH NAME')
    creatUser = Column(field='create_user',header='CREATE USER')
    createDate = Column(field='create_date',header='CREATE DATE')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'},sortable=False)
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'},sortable=False)
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal'},sortable=False)
    class meta:
        Batch
        
class SubjectTable(Table):
    subject_id = Column(field='subject_id',header='SUBJECT ID')
    subject_name = Column(field='subject',header='SUBJECT NAME')
    creatUser = Column(field='create_user',header='CREATE USER')
    createDate = Column(field='create_date',header='CREATE DATE')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'},sortable=False)
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'},sortable=False)
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal'},sortable=False)
    class meta:
        Subject
        
class ClassTable(Table):
    class_id = Column(field='class_id',header='CLASS ID')
    class_field = Column(field='class_field',header='CLASS NAME')
    creatUser = Column(field='create_user',header='CREATE USER')
    createDate = Column(field='create_date',header='CREATE DATE')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'},sortable=False)
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'},sortable=False)
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal'},sortable=False)
    class meta:
        Class
        
class ExamTable(Table):
    exam_type_id = Column(field='exam_type_id',header='EXAM ID')
    exam_type = Column(field='exam_type',header='EXAM NAME')
    creatUser = Column(field='create_user',header='CREATE USER')
    createDate = Column(field='create_date',header='CREATE DATE')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'},sortable=False)
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'},sortable=False)
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal'},sortable=False)
    class meta:
        model = Batch
        
class SchoolTable(Table):
    school_code = Column(field='school_code',header='SCHOOL CODE')
    school_name = Column(field='school_name',header='SCHOOL NAME')
    branch = Column(field='branch',header='BRANCH NAME')
    census_code = Column(field='census_code',header='CENSUS CODE')
    telephone_no = Column(field='telephone_no',header='TELEPHONE NO')
    email_address = Column(field='email_address',header='EMAIL ADDRESS')
    website_url = Column(field='website_url',header='WEBSITE')
    principal = Column(field='principal.principal_name', header='PRINCIPAL')
  
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'})
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'})
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal'})
    
    class meta:
        model = School
        
class BatchClassTable(Table):
    batch_class_id = Column(field='batch_class_id',header='ID')
    batch = Column(field='batch.batch',header='BATCH')
    grade = Column(field='grade.class_field',header='CLASS')
    createUser = Column(field='create_user',header='CREATE USER')
    createDate = Column(field='create_date',header='CREATE DATE')
  
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'})
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'})
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal'})
    
    
class BatchClassSectionTable(Table):
    batch_class_section_id = Column(field='batch_class_section_id',header='ID')
    batch = Column(field='batch_class.batch.batch',header='BATCH')
    grade = Column(field='batch_class.grade.class_field',header='CLASS')
    class_sec = Column(field='class_sec.section', header='SECTION')
    createUser = Column(field='create_user',header='CREATE USER')
    createDate = Column(field='create_date',header='CREATE DATE')
  
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'})
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'})
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal'})
    
class ExamAssignTable(Table):
    exam_assign_id = Column(field='exam_assign_id', header='ID')
    exam_type = Column(field='class_sub_syll.exam_type.exam_type', header='EXAM TYPE')
    grade = Column(field='class_sub_syll.syllabus.class_subject.grade.class_field', header='CLASS')
    subject = Column(field='class_sub_syll.syllabus.class_subject.subject.subject', header='SUBJECT')
    date = Column(field='date', header='DATE')
    day = Column(field='day', header='DAY')
    #from_time = Column(field='from_time', header='START TIME')
    #to_time = Column(field='to_time', header='END TIME')
    
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'})
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'})
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal'})
    
class ClassTimetableTable(Table):
    class_timetable_id =  Column(field='class_timetable_id', header="CLASS TIMETABLE CODE ")
    class_name = Column(field='class_subject.grade.class_field',visible=True,header='CLASS NAME')
    subject = Column(field='class_subject.subject.subject', visible=True,header='SUBJECT')
    section = Column(field='class_section.section.section',header="SECTION")
    period = Column (field='period.period',header='PERIOD')
    day = Column(field='day',header='DAY')
#    from_time = Column(field='from_time',header='FROM TIME')
#    to_time = Column(field='to_time',header='TO TIME')
#    day = Column(field='day',header='DAY')
    #creatUser = Column(field='create_user',header='CREATE USER')
    #createDate = Column(field='create_date',header='CREATE DATE')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'},sortable=False)
#    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'},sortable=False)
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal'},sortable=False)
    

class TeacherTimetableTable(Table):
    teacher_timetable_id =  Column(field='teacher_timetable_id', header="TEACHER TIMETABLE CODE ")
    teacher_name = Column(field='class_teacher_sub.class_teacher.teacher.teacher_first_name', header="TEACHER NAME")
    subject = Column(field='class_teacher_sub.class_subject.subject.subject', visible=True,header='SUBJECT')
    period = Column (field='period.period',header='PERIOD')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'},sortable=False)
    #view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'},sortable=False)
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal'},sortable=False)
    
class ClassSectionTable(Table):
    
    class_sec_code = Column(field='class_sec_id', header="CLASS SECTION CODE")
    class_name = Column(field='class_field.class_field', header="CLASS NAME")
    section = Column(field='section.section', header="SECTION")
    creatUser = Column(field='create_user',header='CREATE USER')
    createDate = Column(field='create_date',header='CREATE DATE')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'},sortable=False)
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'},sortable=False)
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                            'data-toggle':'modal','data-target':'#deleteModal'},sortable=False)
                           
class ClassSubjectTable(Table):
    class_subject_id = Column(field='class_subject_id',header='ID')
    grade = Column(field='grade.class_field',header='CLASS NAME')
    subject = Column(field='subject.subject',header='SUBJECT NAME')
    creatUser = Column(field='create_user',header='CREATE USER')
    createDate = Column(field='create_date',header='CREATE DATE')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'},sortable=False)
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'},sortable=False)
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal'},sortable=False)
    class meta:
        Class
        
class ExamSyllabusTable(Table):
    exmaType_syll_id = Column(field='exmaType_syll_id',header='ID')
    exam_type = Column(field='exam_type.exam_type',header='EXAM NAME')
    syllabus = Column(field='syllabus.syllabus',header='SYLLABUS NAME')
    topic = Column(field='syllabus.topic',header='TOPIC')
    className = Column(field='syllabus.class_subject.grade.class_field',header='CLASS NAME')
    subject = Column(field='syllabus.class_subject.subject.subject',header='SUBJECT NAME')
    creatUser = Column(field='create_user',header='CREATE USER')
    createDate = Column(field='create_date',header='CREATE DATE')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'},sortable=False)
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'},sortable=False)
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal'},sortable=False)
    class meta:
        ExamTypeSyllabus
        
class ClassTeacherTable(Table):
    class_teacher_id = Column(field='class_teacher_id',header='ID')
    batch = Column(field='batch_class_sec.batch_class.batch.batch',header='BATCH')
    class_field = Column(field='batch_class_sec.batch_class.grade.class_field',header='CLASS') 
    section = Column(field='batch_class_sec.class_sec.section',header='SECTION')
    teacher_name = Column(field='teacher.teacher_first_name',header='TEACHER NAME')
    #creatUser = Column(field='create_user',header='CREATE USER')
    #createDate = Column(field='create_date',header='CREATE DATE')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'},sortable=False)
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'},sortable=False)
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal'},sortable=False)
    




class ClassTeacherSubjectTable(Table):
    class_teacher_sub_id = Column(field='class_teacher_sub_id',header='ID')
    class_teacher = Column(field='class_teacher.teacher.teacher_first_name',header='TEACHER NAME')
    class_subject = Column(field='class_subject.subject.subject',header='SUBJECT NAME')
    class_subjects = Column(field='class_subject.grade.class_field',header='CLASS NAME')
    batch_name = Column(field='batch_class.batch.batch',header='BATCH NAME')
    section_name  = Column(field='batch_class_sec.class_sec.section',header='SECTION NAME')
    create_user = Column(field='create_user',header='CREATE USER')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'},sortable=False)
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'},sortable=False)
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal'},sortable=False)
    class meta:
        ClassTeacherSubject
        
        
        
class StudentAttendanceTable(Table):
    #student_attendance_id = Column(field='student_attendance_id',header='ID')
    #student = Column(field='student.firstName',header='STUDENT NAME')
    date = Column(field='date',header='DATE')
    attendance = Column(field='attendance',header='ATTENDANCE')
    #create_user = Column(field='create_user',header='CREATE USER')
    
    class meta:
        StudentAttendance
        ajax = True
        
class TeacherAttendanceTable(Table):
    teacher_attendance_id = Column(field='teacher_attendance_id',header='ID')
    teacher = Column(field='teacher.teacher_first_name',header='TEACHER NAME')
    date = Column(field='date',header='DATE')
    attendance = Column(field='attendance',header='ATTENDANCE')
    create_user = Column(field='create_user',header='CREATE USER')
    
    class meta:
        TeacherAttendance
        ajax = True
        
        
class ViewSyllabusTableTeacher(Table):
    #syllabus_id = Column(field='syllabus_id',header='SYLLABUS ID')
    syllabus = Column(field='syllabus',header='SYLLABUS NAME')
    topic = Column(field='topic',header='TOPIC')
    #className = Column(field='class_subject.grade.class_field',header='CLASS NAME')
    #SubjectName = Column(field='class_subject.subject.subject',header='SUBJECT NAME')
    #examName = Column(field='exam_type.exam_type',header='EXAM NAME')
    
    class meta:
        Syllabus
        ajax = True
        
        
class ExamAssignTeacherTable(Table):
    exam_assign_id = Column(field='exam_assign_id', header='ID')
    exam_type = Column(field='class_sub_syll.exam_type.exam_type', header='EXAM TYPE')
    grade = Column(field='class_sub_syll.syllabus.class_subject.grade.class_field', header='CLASS')
    subject = Column(field='class_sub_syll.syllabus.class_subject.subject.subject', header='SUBJECT')
    date = Column(field='date', header='DATE')
    day = Column(field='day', header='DAY')
    #from_time = Column(field='from_time', header='START TIME')
    #to_time = Column(field='to_time', header='END TIME')
    
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'})
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'})
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteModal'})
    
    
    
class resultTable(Table):
    ranking_id = Column(field='ranking_id',header='RANKING ID')
    studentFirstName = Column(field='student.firstName',header='FIRST NAME')
    studentlastName = Column(field='student.lastName',header='LAST NAME')
    examType = Column(field='exam_type.exam_type',header='EXAM')
    totalmarks = Column(field='total_marks',header='TOTAL MARKS')
    marksobtained = Column(field='marks_obtained',header='MARKS OBTAINED')
    percentagemarks = Column(field='percentage_marks',header='PERCENTAGE')
    ranking = Column(field='ranking',header='RANK')
    class meta:
        model = Batch
		
class HomeworkTable(Table):
    syllabus = Column(field='syllabus.syllabus', header='CHAPTER')
    homework_description = Column(field='homework_description', header='DESCRIPTION')
    from_date = Column(field='from_date', header='START DATE')
    to_date = Column(field='to_date', header='END DATE')
    class meta:
        model = Homework
        
class AssignmentTable(Table):
    syllabus = Column(field='syllabus.syllabus', header='CHAPTER')
    assignment_description = Column(field='assignment_description', header='DESCRIPTION')
    from_date = Column(field='from_date', header='START DATE')
    to_date = Column(field='to_date', header='END DATE')
    class meta:
        model = Assignment
        
class ExamResultTable(Table):
    marks_obtained  =Column(field='marks_obtained', header='MARKS OBTAINED')
    total_marks  =Column(field='total_marks', header='TOTAL MARKS')
    status  =Column(field='status', header='RESULT')
    class meta:
        model = ExamResult