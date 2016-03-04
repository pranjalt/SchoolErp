'''
Created on 14-Jan-2016

@author: Administrator
'''
from SchoolERP.models import Student,ExamResult
from table import Table
from table.columns import Column



class StudentTable(Table):
    studentId = Column(field='student_id',header=' StudentId')
    first_name = Column(field='firstName',header='FIRST NAME')
    last_name = Column(field='lastName',header='LAST NAME')
    addmission_Num=Column(field='admissionNo',header='Addmission No')
    contactNo=Column(field="contactNo",header=' ConatactNo')
    DOB = Column(field='dateOfBirth',header='DOB')
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'})
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view',})
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteStudModal'})
    
    class Meta:
        model = Student
        
class StudentResultTable(Table):
    student= Column(field='student.student_id',header='StudentId')
    first_name = Column(field='student.firstName',header='First Name')
    last_name = Column(field='student.lastName',header='Last Name')
    batch = Column(field=' student.batch_class_sec.batch_class.batch.batch',header='BATCH')
    classvalue = Column(field='student.batch_class_sec.batch_class.grade.class_field',header='class')
    section = Column(field='student.batch_class_sec.class_sec.section',header='section')
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view'})
    
class studReportCardTab(Table):
    marks_obtained =Column(field='marks_obtained',header='marksObtained')
    total_marks = Column(field='total_marks',header='out of')
    status =Column(field='marks_obtained',header='status')    
 
class assignmentTable(Table):
    assignmentId=Column(field='assignment_id',header="Assignment_id",)
    classVal=Column(field='syllabus.class_subject.grade.class_field',header="class")
    subject =Column(field = 'syllabus.class_subject.subject.subject',header="subject")
    syllabus= Column(field='syllabus.syllabus',header="syllabus")
    view = Column(field='view',header='',attrs = {'class':'fa fa-file-text','id':'view',})
    edit = Column(field='edit',header='',attrs = {'class':'fa fa-edit','id':'edit'})
    trash = Column(field='trash',header='',attrs= {'class':'fa fa-trash-o','id':'trash',
                                                   'data-toggle':'modal','data-target':'#deleteAssignmentModal'})
    
class StudentRankingTable(Table):
    student_id = Column(field="student.student_id" , header="student_id")
    first_name = Column(field="student.first_name" , header="first_name")
    last_name = Column(field="student.last_name" , header="last_name")
    total_marks = Column(field="total_marks" , header="total_marks")
    marks_obtained = Column(field="marks_obtained" , header="marks_obtained")
    percentage_marks = Column(field="percentage_marks" , header="percentage_marks")
    ranking = Column(field="ranking" , header="ranking")
    grade = Column(field="grade" , header="grade")
    