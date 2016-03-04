'''
Created on 10-Feb-2016

@author: Administrator
'''
from SchoolERP.models import *
from table import Table

from table.columns import Column

 
class examScheduleTable(Table):
    exam_assign_id = Column(field='exam_assign_id', header='ID')
    exam_type = Column(field='class_sub_syll.exam_type.exam_type', header='EXAM TYPE')
    grade = Column(field='class_sub_syll.syllabus.class_subject.grade.class_field', header='CLASS')
    subject = Column(field='class_sub_syll.syllabus.class_subject.subject.subject', header='SUBJECT')
    date = Column(field='date', header='DATE')
    day = Column(field='day', header='DAY')
    
class RankingTable(Table):
    student_id =Column(field='student', header='StudentId')
    firstName = Column(field='student.firstName', header='FirstName')
    lastName = Column(field='student.lastName', header='LastName')
    total_marks = Column(field='total_marks', header='Total_Marks')
    marks_obtained = Column(field='marks_obtained', header='marks Obtained')
    percentage_marks = Column(field='percentage_marks', header='Percentage')
    ranking = Column(field='ranking', header='Ranking')
    