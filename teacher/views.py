from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
from django.template.response import TemplateResponse
from SchoolERP.models import *
from school.tables import *
from django.shortcuts import render_to_response,render
from django.template.loader import render_to_string
from django.shortcuts import RequestContext
import json as json
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import JsonResponse
import logging
from django.http.response import HttpResponse, JsonResponse
logger = logging.getLogger(__name__)
from django.http import HttpResponseRedirect


def teacherHomePage(request):
    
    logger.debug("this is a debug message!")
    return render_to_response("baseTeacher.html")

def viewSyllabusTeacherModule(request):
    logger.debug("start of syllabusList in Teacher Module")
    syllabusList = Syllabus.objects.all()
    syllabus = SyllabusTable(Syllabus.objects.all())
    return render_to_response("teacher/viewSyllabus.html", {'syllabusList':syllabus,'syllabus':syllabusList})
    
def viewResultTeacherModule(request):
    logger.debug("start of ResultList in Teacher Module")
    resultList = ExamResult.objects.all()
    result = SyllabusTable(ExamResult.objects.all())
    return render_to_response("teacher/viewResult.html", {'resultList':result,'result':resultList})
    
def viewExamScheduleTeacherModule(request):
    logger.debug("start of ExamSchedule in Teacher Module")
    examList = ExamAssign.objects.all()
    exam = SyllabusTable(ExamAssign.objects.all())
    return render_to_response("teacher/viewExamSchedule.html", {'examList':exam,'exam':examList})
    
def viewProfileTeacherModule(request):
    logger.debug("start of teacher Profile in Teacher Module")
    teacherinformation = Teacher.objects.all()
    teacher = SyllabusTable(Teacher.objects.all())
    return render_to_response("teacher/viewTeacherProfile.html", {'teacherinformation':teacher,'teacher':teacherinformation})
    

def viewAttendanceTeacherModule(request):
    logger.debug("start of Class Attendance in Teacher Module")
    classAttndInfo = Student.objects.all()
    attndInfo = SyllabusTable(Student.objects.all())
    return render_to_response("teacher/viewClassAttendance.html", {'classAttndInfo':attndInfo,'attndInfo':classAttndInfo})
    
def viewTimeTableTeacherModule(request):
    logger.debug("start of timetable in Teacher Module")
    classAttndInfo = Student.objects.all()
    attndInfo = SyllabusTable(Student.objects.all())
    return render_to_response("teacher/viewTeacherTimetable.html", {'classAttndInfo':attndInfo,'attndInfo':classAttndInfo})
    
def getSyllabusData(request):
    logger.debug("inside getSyllabusData")
    ExamTypeId = request.GET.get('ExamTypeId')
    classSubjectId = request.GET.get('classSubjectId')
    logger.debug(ExamTypeId)
    logger.debug(classSubjectId)
    syllabusInformation = Syllabus.objects.filter(exam_type=ExamTypeId, class_subject=classSubjectId)
    print "syllabusInformation",syllabusInformation
    students=[]
    syllabusList = ViewSyllabusTableTeacher(syllabusInformation)
    """"for item in attendanceInformation:
        #grade_dict = model_to_dict(item.student)
        item_dict = model_to_dict(item)
        #item_dict['student'] = grade_dict
        #students.append(item_dict)
        stable = StudentAttendanceTable(item_dict)"""
    print "tttttttttttt",syllabusList
    html = render_to_string("teacher/viewSyllabusList.html", {'syllabusList':syllabusList})
    return HttpResponse(html)
    
def getBatchClassSecIdbyTeacher(request):
    logger.debug("inside getBatchClassSecIdbyTeacher")
    teacher_id = request.GET.get('teacher_id')
    logger.debug(teacher_id)
    batchClassSecInfo = ClassTeacher.objects.filter(teacher=teacher_id)
    print "batchClassSecInfo",batchClassSecInfo
    students=[]
    for item in batchClassSecInfo:
        grade_dict = model_to_dict(item.batch_class_sec)
        item_dict = model_to_dict(item)
        item_dict['batch_class_sec'] = grade_dict
        students.append(item_dict)    
    logger.debug(students)
    print 'batchClassSecInfo  --', students
    logger.debug("going back")
    return  JsonResponse(students, safe=False)
    
def getClassbyBacthClassId(request):
    logger.debug("inside getClassbyBacthClassId")
    bacthClass = request.GET.getlist('bacthClass[]')
    logger.debug(bacthClass)
    classInfo = BatchClasses.objects.filter(batch_class_id__in=bacthClass)
    print "classInfo",classInfo
    classes=[]
    for item in classInfo:
        grade_dict = model_to_dict(item.grade)
        item_dict = model_to_dict(item)
        item_dict['grade'] = grade_dict
        classes.append(item_dict)    
    logger.debug(classes)
    print 'classInfo  --', classes
    logger.debug("going back")
    return  JsonResponse(classes, safe=False)
    
    
def getSyllabusId(request):
    logger.debug("inside getSyllabusId")
    classSubjectId = request.GET.get('classSubjectId')
    examtypeId = request.GET.get('examtypeId')
    logger.debug(classSubjectId)
    logger.debug(examtypeId)
    syllabusInfo = Syllabus.objects.filter(class_subject=classSubjectId, exam_type=examtypeId)
    print "syllabusInfo",syllabusInfo
    syllabuses=[]
    for item in syllabusInfo:
        grade_dict = model_to_dict(item.exam_type)
        item_dict = model_to_dict(item)
        item_dict['grade'] = grade_dict
        syllabuses.append(item_dict)    
    logger.debug(syllabuses)
    print 'syllabusInfo  --', syllabuses
    logger.debug("going back")
    return  JsonResponse(syllabuses, safe=False)
    
    
def getExamTypeSyllabusId(request):
    print "inside getExamTypeSyllabusId"
    syllabusInfo = request.GET.getlist('syllabusInfo[]')
    examID = request.GET.get('examID')
    print "Syllabus Info -- " , syllabusInfo
    print "examID Info -- " , examID
    examTypeSyllabusId = ExamTypeSyllabus.objects.filter(syllabus__in=syllabusInfo, exam_type=examID)
    print "examTypeSyllabusId",examTypeSyllabusId
    syllabuses=[]
    for item in examTypeSyllabusId:
        grade_dict = model_to_dict(item.syllabus)
        item_dict = model_to_dict(item)
        item_dict['syllabus'] = grade_dict
        syllabuses.append(item_dict)    
    logger.debug(syllabuses)
    print 'examTypeSyllabusId  --', syllabuses
    logger.debug("going back")
    return  JsonResponse(syllabuses, safe=False)
    
    
def getExamScheduleInfo(request):
    logger.debug("inside getExamScheduleInfo")
    class_sub_syll_id = request.GET.getlist('class_sub_syll_id[]')
    logger.debug(class_sub_syll_id)
    examScheduleInformation = ExamAssign.objects.filter(class_sub_syll__in=class_sub_syll_id)
    print "examScheduleInformation",examScheduleInformation
    students=[]
    examList = ExamAssignTeacherTable(examScheduleInformation)
    """"for item in attendanceInformation:
        #grade_dict = model_to_dict(item.student)
        item_dict = model_to_dict(item)
        #item_dict['student'] = grade_dict
        #students.append(item_dict)
        stable = StudentAttendanceTable(item_dict)"""
    print "tttttttttttt",examList
    html = render_to_string("teacher/listExamSchedule.html", {'examList':examList})
    return HttpResponse(html)

    
def getTeacherInformation(request):
    print " In getTeacherInformation"
    teacher_id = request.GET.get('teacher_id')
    print "TeacherId is -- " , teacher_id
    teacherInformation = Teacher.objects.filter(teacher_id=teacher_id)
    print "teacherInformation",teacherInformation
    teachers=[]
    for item in teacherInformation:
        #grade_dict = model_to_dict(item)
        item_dict = model_to_dict(item)
        #item_dict['teacher'] = grade_dict
        teachers.append(item_dict)
    print "teachers", teachers
    logger.debug("going back")
    return  JsonResponse(teachers, safe=False)
    
    
@csrf_exempt
def updateTeacherDetails(request):
    logger.debug('start of updateTeacherDetails Method')
    
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        method = request.POST.get('method')
        teacherID=request.POST.get('teacherID')
        phnNo=request.POST.get('phnNo')
        Email=request.POST.get('Email')
        print "TeacherID is -- " , teacherID
        print "Phone No is -- " , phnNo
        print "Email is -- " , Email
        print "Method is -- " , method
        #count = ClassSubject.objects.filter(grade_id=class_name).count()
        #logger.debug(count)
        flag = 0
        if method=='edit':
            logger.debug("In Edit")
            s = Teacher.objects.get(teacher_id=teacherID)
            
            if s.teacher_contact_no != phnNo:
                s.teacher_contact_no = phnNo
                flag = 1
            
            if s.teacher_email_id != Email:
                s.teacher_email_id = Email
                flag = 1
                    
            if flag == 1:
                s.save()
            else:
                print 'No changes detected'
    return HttpResponse(value)
    
    
def getBatchClassIdbyClass(request):
    print "inside getBatchClassIdbyClass"
    classVal = request.GET.get('classVal')
    print "ClassVal--" , classVal
    batch_class_id = BatchClasses.objects.filter(grade=classVal)
    logger.debug(batch_class_id)
    #data = serializers.serialize('json',class_subject_id )
    subjectsDict=[]
    for item in batch_class_id :
        dict=model_to_dict(item)
        subjectsDict.append(dict) 
    print "Dict --- " , subjectsDict
    logger.debug(subjectsDict)
    return  JsonResponse(subjectsDict, safe=False)
    
    
def getSections(request):
    print "inside getSections"
    bacthClass_Id = request.GET.getlist('bacthClass_Id[]')
    print "bacthClass_Id--" , bacthClass_Id
    batchSectioninfo = BatchClassSection.objects.filter(batch_class__in=bacthClass_Id)
    logger.debug(batchSectioninfo)
    #data = serializers.serialize('json',class_subject_id )
    subjectsDict=[]
    for item in batchSectioninfo :
        grade_dict = model_to_dict(item.class_sec)
        item_dict = model_to_dict(item)
        item_dict['class_sec'] = grade_dict
        subjectsDict.append(item_dict)
    print "SectionDict --- " , subjectsDict
    logger.debug(subjectsDict)
    return  JsonResponse(subjectsDict, safe=False)

    
def getBatchClassSectionIds(request):
    logger.debug("inside getBatchClassSectionIds")
    sectionVal = request.GET.get('sectionVal')
    batchClassVal = request.GET.getlist('batchClassVal[]')
    print "sectionVal -- " , sectionVal
    print "batchClassVal -- " , batchClassVal
    batchClassSectionID = BatchClassSection.objects.filter(batch_class__in=batchClassVal, class_sec=sectionVal)
    print "batchClassSectionID-- " , batchClassSectionID
    batchclassSecId=[]
    for item in batchClassSectionID:
        grade_dict = model_to_dict(item.class_sec)
        item_dict = model_to_dict(item)
        item_dict['class_sec'] = grade_dict
        batchclassSecId.append(item_dict)
    print "batchclassSecId  -- " , batchclassSecId
    logger.debug("going back")
    return  JsonResponse(batchclassSecId, safe=False)
    
    
def getResult(request):
    print "getResult"
    StudentID = request.GET.getlist('StudentID[]')
    examType = request.GET.get('examType')
    print "StudentID -- " , StudentID
    print "ExamType -- " , examType
    rankingInfo = Ranking.objects.filter(student__in=StudentID, exam_type=examType)
    print "rankingInfo-- " , rankingInfo
    batchclassSecId=[]
    resultList = resultTable(rankingInfo)
    """"for item in rankingInfo:
        grade_dict = model_to_dict(item.student)
        item_dict = model_to_dict(item)
        item_dict['student'] = grade_dict
        batchclassSecId.append(item_dict)"""
    print "batchclassSecId  -- " , resultList
    html = render_to_string("teacher/viewResultList.html", {'resultList':resultList})
    return HttpResponse(html)
    
def getStudentId(request):
    print "inside getStudentId"
    batchClassSectionId = request.GET.getlist('batchClassSectionId[]')
    print "batchClassSectionId--" , batchClassSectionId
    studentInfo = Student.objects.filter(batch_class_sec__in=batchClassSectionId)
    logger.debug(studentInfo)
    #data = serializers.serialize('json',class_subject_id )
    subjectsDict=[]
    for item in studentInfo :
        dict=model_to_dict(item)
        subjectsDict.append(dict) 
    print "Dict --- " , subjectsDict
    logger.debug(subjectsDict)
    return  JsonResponse(subjectsDict, safe=False)
    
    
    
    