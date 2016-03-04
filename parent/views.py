from django.shortcuts import render, render_to_response
from django.template.loader import render_to_string
from SchoolERP.models import *
from django.http.response import HttpResponse,JsonResponse
import logging
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from school.tables import ViewSyllabusTableTeacher,SyllabusTable,ExamAssignTeacherTable,\
    HomeworkTable, AssignmentTable,StudentAttendanceTable, ExamResultTable
logger = logging.getLogger(__name__)

def studentHome(request):
    logger.debug("this is a debug message!")
    default_load_tab = ""
    try:
        default_load_tab = request.GET['default_load_tab']
    except:
        default_load_tab = ""
    return render_to_response("parent/parent.html", {'default_load_tab':default_load_tab})

# Create your views here.
def viewSyllabus(request):
    #studentId = request.GET.get('studentId',None)
    #print studentId
    #student_id = '7'
    #stud_class = Student.objects.filter(student_id=student_id).values('student_id','batch_class_sec')
    #print stud_class
    #grade = BatchClasses.objects.filter(batch_class_id__in=BatchClassSection.objects.filter(batch_class_section_id__in=Student.objects.filter(student_id=student_id).values('batch_class_sec')).values('batch_class')).values('grade')
    #print grade[0]
    #syllabus = Syllabus.objects.filter(class_subject=grade[0])
    logger.debug("start of syllabusList in Teacher Module")
    syllabusList = Syllabus.objects.all()
    syllabus = SyllabusTable(Syllabus.objects.all())
    return render_to_response("parent/studSyllabus.html", {'syllabusList':syllabus,'syllabus':syllabusList})

def getSyllabus(request):
    logger.debug("inside getSyllabusData")
    ExamTypeId = request.GET.get('ExamTypeId')
    classSubjectId = request.GET.get('classSubjectId')
    print 'jjdsjdkjdjkd',ExamTypeId,classSubjectId
    logger.debug(ExamTypeId)
    logger.debug(classSubjectId)
    syllabusInformation = Syllabus.objects.filter(exam_type=ExamTypeId, class_subject__in=ClassSubject.objects.filter(grade='35',subject=classSubjectId).values('class_subject_id'))
    print "syllabusInformation",syllabusInformation
    
    syllabusList = ViewSyllabusTableTeacher(syllabusInformation)
    
    print "tttttttttttt",syllabusList
    html = render_to_string("teacher/viewSyllabusList.html", {'syllabusList':syllabusList})
    return HttpResponse(html)

def viewExamSchedule(request):
    logger.debug("start of ExamSchedule in Parent Module")
    examList = ExamAssign.objects.all()
    exam = SyllabusTable(ExamAssign.objects.all())
    return render_to_response("parent/examSchedule.html", {'examList':exam,'exam':examList})

def getExamSchedule(request):
    logger.debug("inside getExamScheduleInfo")
    examType = request.GET.get('examType')
    print examType
    logger.debug(examType)
    examScheduleInfo = ExamAssign.objects.filter(class_sub_syll__in=ExamTypeSyllabus.objects.filter(syllabus__in=Syllabus.objects.filter(exam_type=examType, class_subject__in=ClassSubject.objects.filter(grade='35').values('class_subject_id')).values('syllabus_id')).values('exmaType_syll_id'))
    
    print "examScheduleInformation ",examScheduleInfo
    examList = ExamAssignTeacherTable(examScheduleInfo)
   
    print "tttttttttttt",examList
    html = render_to_string("parent/viewStudExamSchedule.html", {'examList':examList})
    return HttpResponse(html)

def viewHomework(request):
    logger.debug("start of viewHomework in Parent Module")
    #homeWorkList = Homework.objects.all()
    homeWorkList = HomeworkTable(Homework.objects.all())
    assignmentList = AssignmentTable(Assignment.objects.all())
    return render_to_response("parent/homework.html", {'homeWorkList':homeWorkList,'assignmentList':assignmentList})

def getHomework(request):
    logger.debug("inside getHomework")
    classSubjectId = request.GET.get('classSubjectId')
    print classSubjectId
    logger.debug(classSubjectId)
   
    homework = Homework.objects.filter(syllabus__in=Syllabus.objects.filter(class_subject__in=ClassSubject.objects.filter(grade='35',subject=classSubjectId).values('class_subject_id')).values('syllabus_id'))
    print "homework ",homework
    homeWorkList = HomeworkTable(homework)
    
    assignment = Assignment.objects.filter(syllabus__in=Syllabus.objects.filter(class_subject__in=ClassSubject.objects.filter(grade='35',subject=classSubjectId).values('class_subject_id')).values('syllabus_id'))
    print "assignment ", assignment
    assignmentList = AssignmentTable(assignment)
    print "assignmentList ",assignmentList
    
    print "tttttttttttt",homeWorkList
    html = render_to_string("parent/viewHomework.html", {'homeWorkList':homeWorkList, 'assignmentList':assignmentList})
    return HttpResponse(html)

def viewTimeTable(request):
    logger.debug("start of viewTimeTable in Parent Module") 
    return render_to_response("parent/timetable.html")

def viewAttendance(request):
    logger.debug("start of viewAttendance in Parent Module") 
    attendanceList = StudentAttendanceTable(StudentAttendance.objects.all())
    return render_to_response("parent/attendance.html",{'attendanceList':attendanceList})

def getStudAttendance(request):
    logger.debug("start of getStudAttendance in Parent Module") 
    month = request.GET.get('month')
    endDate = 0
    if month in {'1','3','5','7','8','10','12'}:
        print 'condition 1'
        endDate ='31'
    elif month == '2':
        endDate = '29'
    elif month in {'4','6','9','11'}:
        endDate = '30'
        
    start_date = '2016-'+month+'-1'
    end_date = '2016-'+month+'-'+endDate
    print "start_date ", start_date, " end_date", end_date
    attendance = StudentAttendance.objects.filter(student='74',date__range=(start_date, end_date))
    print attendance
    absentCount = StudentAttendance.objects.filter(student='74',date__range=(start_date, end_date),attendance='A').count()
    print "absentCount ", absentCount
    attendanceList = StudentAttendanceTable(attendance)
    html = render_to_string("parent/viewAttendance.html", {'attendanceList':attendanceList})
    return HttpResponse(html)

def viewResult(request):
    
    logger.debug("start of viewResult in Student Module")
    examResultList = ExamResultTable(ExamResult.objects.all())
    return render_to_response("parent/result.html", {'examResultList':examResultList})

def getStudResult(request):
    logger.debug("start of getStudResult in Student Module")
    ExamTypeId = request.GET.get('ExamTypeId')
    classSubjectId = request.GET.get('classSubjectId')
    print 'jjdsjdkjdjkd',ExamTypeId,classSubjectId
    logger.debug(ExamTypeId)
    logger.debug(classSubjectId)
    examResult = ExamResult.objects.filter(student='74',exam_assign__in=ExamAssign.objects.filter(class_sub_syll__in=ExamTypeSyllabus.objects.filter(syllabus__in=Syllabus.objects.filter(exam_type=ExamTypeId,class_subject__in=ClassSubject.objects.filter(subject=classSubjectId).values('class_subject_id')).values('syllabus_id')).values('exmaType_syll_id')).values('exam_assign_id'))
    print examResult
    examResultList = ExamResultTable(examResult)
    #RequestConfig(request, paginate=False).configure(examResultList)
    html = render_to_string("parent/viewResult.html", {'examResultList':examResultList})
    return HttpResponse(html)

def viewStudProfile(request):
    logger.debug("start of teacher Profile in Teacher Module")
    student = SyllabusTable(Student.objects.all())
    return render_to_response("parent/studProfile.html", {'student':student})

def getStudProfile(request):
    print " In viewStudProfile"
    stud_id = request.GET.get('stud_id')
    print "StudId is -- " , stud_id
    studInformation = Student.objects.filter(student_id=stud_id)
    print "studInformation",studInformation
    student=[]
    for item in studInformation:
        #grade_dict = model_to_dict(item)
        item_dict = model_to_dict(item)
        #item_dict['teacher'] = grade_dict
        student.append(item_dict)
    print "student", student
    logger.debug("going back")
    return  JsonResponse(student, safe=False)

@csrf_exempt
def updateStudDetails(request):
    logger.debug('start of updateStudDetails Method')
    
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        method = request.POST.get('method')
        studID=request.POST.get('studID')
        phnNo=request.POST.get('phnNo')
       
        print "studID is -- " , studID
        print "Phone No is -- " , phnNo
 
        print "Method is -- " , method
        #count = ClassSubject.objects.filter(grade_id=class_name).count()
        #logger.debug(count)
        flag = 0
        if method=='edit':
            logger.debug("In Edit")
            s = Student.objects.get(student_id=studID)
            
            if s.contactNo != phnNo:
                s.contactNo = phnNo
                flag = 1
            
            if flag == 1:
                s.save()
            else:
                print 'No changes detected'
    return HttpResponse(value)