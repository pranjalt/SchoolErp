from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
from principal.tables import *
from django.shortcuts import render_to_response,render
from django.shortcuts import RequestContext
import json as json
from django.template.loader import render_to_string
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import JsonResponse
from student.forms import *
from SchoolERP.models import *
from django.db.models import Count

import logging
logger = logging.getLogger(__name__)


def principalHomePge(request):
    
    logger.debug("this is a debug message!")
    return render_to_response("basePrincipal.html")

def listExamSchedule(request):
    
    bform=batchForm()
    clsform=classForm()
    examTypeFrm=examTypeForm()
    examAssign = ExamAssign.objects.all();
    print "examAssign",examAssign
    examScheduleTbl =examScheduleTable(examAssign)
    
    return render_to_response("principal/examSchedule.html", 
                  {'examScheduleTable':examScheduleTbl,
                   'bform':bform,'clsform':clsform,
                   'examTypeFrm':examTypeFrm})
    
  
def getExamScheduleDetails(request):
    bcId = request.GET.get('bcId',None)
    examTypeId=request.GET.get('examTypeId',None)
    bacthClass= BatchClasses.objects.get(batch_class_id=bcId)
    classId=bacthClass.grade
    examSchedule=ExamAssign.objects.filter(class_sub_syll__in =ExamTypeSyllabus.objects.filter(exam_type=examTypeId,syllabus__in=Syllabus.objects.filter(class_subject__in=ClassSubject.objects.filter(grade=classId))))
    print "examSchedule ::",examSchedule
    modelDict =[]
    for item in examSchedule :
        examScheduleModel= model_to_dict(item)
        subjectModel=model_to_dict(item.class_sub_syll.syllabus.class_subject.subject)
        classModel = model_to_dict(item.class_sub_syll.syllabus.class_subject.grade)
        examType = model_to_dict(item.class_sub_syll.syllabus.exam_type)
        examScheduleModel['examType']= examType
        examScheduleModel['subjectDetails'] =subjectModel
        examScheduleModel['classVal'] = classModel
        
        modelDict.append(examScheduleModel)
    
    return JsonResponse(modelDict, safe=False)

    
def classResultSearchList(request):
    logger.info(" In principal ,start of classResultSearchList method")
    #studResultForm=examResultForm
    bform=batchForm()
    clsform=classForm()
    secForm=SectionsForm() 
    examTypeFrm=examTypeForm()
    logger.debug("ajax call")
    ranking = Ranking.objects.all()   
    logger.info("start of exam Result SearchList method")   
    rankingTable = RankingTable(ranking)
    logger.info("In Principal ,end of classResultSearchList method")
    
    return render_to_response("principal/ClassResult.html", 
                  {'rankingTable':rankingTable,
                   'bform':bform,'clsform':clsform,
                   'secForm':secForm,'examTypeFrm':examTypeFrm})
    
      

def viewClassResult(request):
    bcsId = request.GET.get('bcsId',None)
    examTypeId=request.GET.get('examTypeId',None)
    
    topperResult = Ranking.objects.filter(student__in = Student.objects.filter(batch_class_sec=BatchClassSection.objects.get(batch_class_section_id = bcsId)),status = 'pass',exam_type=examTypeId).order_by('-percentage_marks')[:3]
    failStudResult = Ranking.objects.filter(student__in = Student.objects.filter(batch_class_sec=BatchClassSection.objects.get(batch_class_section_id = bcsId)),exam_type=examTypeId).order_by('percentage_marks')[:3]

    allPssStud = Ranking.objects.filter(student__in = Student.objects.filter(batch_class_sec=BatchClassSection.objects.get(batch_class_section_id = bcsId)),status = 'pass',exam_type=examTypeId)
    failStud = Ranking.objects.filter(student__in = Student.objects.filter(batch_class_sec=BatchClassSection.objects.get(batch_class_section_id = bcsId)),status = 'fail',exam_type=examTypeId)
    examAttendedStud = Ranking.objects.filter(student__in = Student.objects.filter(batch_class_sec=BatchClassSection.objects.get(batch_class_section_id = bcsId)),exam_type=examTypeId)
    
    studCount = examAttendedStud.count()
    passStudCount = allPssStud.count()
    failCount = failStud.count()
    passPercent = passStudCount * 100 /studCount
    failPercent = failCount * 100 /studCount
    
    modelDict ={}
    classPassDict=[]
    classFailDict = []
    for item in topperResult :
        topRankingStudModel= model_to_dict(item)
        student=model_to_dict(item.student)
        topRankingStudModel['studentDetails']= student
        classPassDict.append(topRankingStudModel) 
        
    
    modelDict['topRankers'] = classPassDict
    
    for item in  failStudResult :
        lastRankingStudModel = model_to_dict(item)
        student=model_to_dict(item.student)
        lastRankingStudModel['studentDetails']= student
        classFailDict.append(lastRankingStudModel)
    
    modelDict['failRankers'] = classFailDict
    
    modelDict['passPercent'] =passPercent
    modelDict['failPercent'] = failPercent
    modelDict['passStudCount'] = passStudCount
    modelDict['failStudCount'] = failCount
    modelDict['totalStud'] = studCount
    
    print modelDict
    
    return JsonResponse(modelDict, safe=False)