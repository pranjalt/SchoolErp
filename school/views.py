from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
from SchoolERP.models import *
from school.tables import *
from django.shortcuts import render_to_response,render
from django.shortcuts import RequestContext
import json as json
from django.template.loader import render_to_string
from django.core import serializers
from django.forms.models import model_to_dict
from django.http import JsonResponse
import logging
from django.http.response import HttpResponse, JsonResponse
logger = logging.getLogger(__name__)
from django.http import HttpResponseRedirect

def homePge(request):
    #form = RegistrationForm()
    logger.debug("this is a debug message!")
    default_load_tab = ""
    try:
        default_load_tab = request.GET['default_load_tab']
    except:
        default_load_tab = ""
    return render_to_response("base.html", {'default_load_tab':default_load_tab})

def getPrincipalList(request):
    principalList = Principal.objects.all()
    data= serializers.serialize("json", principalList)
    return HttpResponse(data)
    
def schoolList(request):
    logger.debug("start of schoolList")
    schoolList = School.objects.all()
    school = SchoolTable(schoolList)
    return render_to_response("school/schoolList.html", {'schoolList':school})

@csrf_exempt
def addSchool(request):
    logger.debug('start of addSchool Method')
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        school_code = request.POST.get('school_code')
        schoolName=request.POST.get('schoolName')
        schoolBranch=request.POST.get('schoolBranch')
        principal=request.POST.get('principal')
        censusCode=request.POST.get('censusCode')
        address=request.POST.get('address')
        faxNo=request.POST.get('faxNo')
        telNo=request.POST.get('telNo')
        emailAddress=request.POST.get('emailAddress')
        websiteUrl=request.POST.get('websiteUrl')
        method = request.POST.get('method')
        
        count = School.objects.filter(school_name=schoolName).count()
        flag = 0
        if method=='edit':
            
            s = School.objects.get(school_code=school_code)
            
            if s.school_name != schoolName:
                s.school_name = schoolName
                flag = 1
            
            if s.branch != schoolBranch:
                s.branch = schoolBranch
                flag = 1
                
            if s.principal.principal_id != principal:
                s.principal.principal_id = principal
                flag = 1
             
            if s.census_code != censusCode:
                s.census_code = censusCode
                flag = 1
            
            if s.address != address:
                s.address = address
                flag = 1
               
            if s.fax_no != faxNo:
                s.fax_no = faxNo
                flag = 1
              
            if s.telephone_no != telNo:
                s.telephone_no = telNo
                flag = 1
               
            if s.email_address != emailAddress:
                s.email_address = emailAddress
                flag = 1
             
            if s.website_url != websiteUrl:
                s.website_url = websiteUrl
                flag = 1
            
            if flag == 1:
                s.save()
            else:
                print 'No changes detected'
            logger.debug('updated successfully')
            
        elif count != 0:
            value = 'false'
        else:
            if method=='add':
                print 'inside add'
                school=School.objects.create(school_name = schoolName, branch=schoolBranch, census_code=censusCode,
                                             address=address, fax_no=faxNo,telephone_no=telNo,email_address=emailAddress,
                                             website_url=websiteUrl, principal_id=principal, create_user = request.user)
                school.save()
                print 'saved'   
                value = 'save'
            
    return HttpResponse(value) 

def delSchool(request,schoolCode):
    logger.info("start of delSchool method")
    try:
        schoolCode = request.GET.get('schoolCode',None)
        print schoolCode
        if schoolCode is None:
            logger.exception('schoolCode = '+schoolCode)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('schoolCode = '+schoolCode)
            School.objects.filter(school_code=schoolCode).delete()
    except School.DoesNotExist:
        logger.exeption('School Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delSchool method")
    return render_to_response("school/schoolList.html", RequestContext(request,{}))

def getSchoolDetails(request,schoolCode):
    schoolCode = request.GET.get('schoolCode',None)
    print 'schoolCode ', schoolCode
    school = School.objects.filter(school_code=schoolCode)
    print school
    data= serializers.serialize("json", school)
    print data
    return HttpResponse(data)

def subjectList(request):
    logger.debug("start of subjectList")
    subjectList = Subject.objects.all()
    subject = SubjectTable(subjectList)
    return render_to_response("school/subjectList.html", {'subjectList':subject})

def classList(request):
    logger.debug("start of classList")
    classList = Class.objects.all()
    classes = ClassTable(Class.objects.all())
    return render_to_response("school/classList.html", {'classList':classes,'classes':classList})

def examList(request):
    logger.debug("start of examList")
    examList = ExamType.objects.all()
    exam = ExamTable(ExamType.objects.all())
    return render_to_response("school/examList.html", {'examList':exam,'exam':examList})


def syllabusList(request):
    logger.debug("start of examList")
    syllabusList = Syllabus.objects.all()
    syllabus = SyllabusTable(Syllabus.objects.all())
    return render_to_response("school/syllabusList.html", {'syllabusList':syllabus,'syllabus':syllabusList})

def teacherList(request):
    logger.info("start of teacherList")
    try:
        teacherList = Teacher.objects.all()
        logger.debug("Fetch teacher List")
        teacher = TeacherTable(teacherList)
    except Sections.DoesNotExist:
        logger.exeption('Teacher Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))  
    logger.info("end of teacherList") 
    return render_to_response("school/teacherList.html", {'teacher':teacher})

def sectionList(request):
    logger.info("start of sectionList")
    try:
        sectionList = Sections.objects.all()
        logger.debug("Fetch section List")
        section = SectionTable(Sections.objects.all())
    except Sections.DoesNotExist:
        logger.exeption('Section Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))  
    logger.info("end of sectionList") 
    return render_to_response("school/sectionList.html", {'sectionList':section,'section':sectionList})
@csrf_exempt
def addTeacher(request):
    logger.info("start of add Teacher")
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        teacherFirstName = request.POST.get('teacherFirstName')
        teacherId = request.POST.get('teacherId')
        teacherLastName = request.POST.get('teacherLastName')
        contactNumber = request.POST.get('contactNumber')
        emailId = request.POST.get('emailId')
        method = request.POST.get('method')
        count = Teacher.objects.filter(teacher_email_id=emailId).count()
        logger.debug(count)
        if count != 0 and method == 'edit':
            value = 'true'
            t = Teacher.objects.get(teacher_id=teacherId)  
            t.teacher_first_name = teacherFirstName
            t.teacher_last_name=teacherLastName
            t.teacher_contact_no=contactNumber
            t.teacher_email_id=emailId
            t.save()
            value = 'updated'
            logger.debug('updated succefully') 
        elif count != 0 :
            value ='false'
        else:
            if method=='add':
                teacher=Teacher.objects.create(teacher_first_name=teacherFirstName,
                                               teacher_last_name=teacherLastName,
                                               teacher_contact_no=contactNumber,teacher_email_id=emailId,create_user=request.user)
                teacher.save()
                value = 'save'         
    return HttpResponse(value) 

@csrf_exempt
def addSection(request):
    logger.info("start of add Section")
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        sectionName = request.POST.get('sectionName')
        sectionId = request.POST.get('sectionId')
        method = request.POST.get('method')
        count = Sections.objects.filter(section=sectionName).count()
        if count != 0:
            value = 'false'
        else:
            if method=='add':
                section=Sections.objects.create(section = sectionName,create_user = request.user)
                section.save()
                value = 'save'
            elif method == 'edit':
                s = Sections.objects.get(sectionId=sectionId)  
                s.section = sectionName
                s.save()
                value = 'updated'
                logger.debug('updated succefully')             
    return HttpResponse(value) 
     
     
def batchList(request):
    logger.debug("start of batchList")
    batchList = Batch.objects.all()
    batch = BatchTable(batchList)
    return render_to_response("school/batchList.html", {'batchList':batch})

def getClassList(request):
    classList = Class.objects.all()
    data= serializers.serialize("json", classList)
    return HttpResponse(data)

def getTeacher(request):
    teacherList = Teacher.objects.all()
    data= serializers.serialize("json", teacherList)
    return HttpResponse(data)

def getSubjectList(request):
    subjectList = Subject.objects.all()
    data= serializers.serialize("json", subjectList)
    return HttpResponse(data)

@csrf_exempt
def addBatch(request):
    logger.debug('start of addBatch Method')
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        batchId = request.POST.get('batchId')
        batchName=request.POST.get('batchName')
        method = request.POST.get('method')
        count = Batch.objects.filter(batch=batchName).count()
        if count != 0:
            value = 'false'
        else:
            if method=='add':
                batch=Batch.objects.create(batch = batchName,create_user = request.user)
                batch.save()
                value = 'save'
            elif method == 'edit':
                b = Batch.objects.get(batch_id=batchId)  
                b.batch = batchName
                b.save()
                value = 'updated'
                logger.debug('updated succefully')
    return HttpResponse(value) 
        
def delTeacher(request,teacherId):
    logger.info("start of delTeacher method")
    try:
        teacherId = request.GET.get('teacherId',None)
        if teacherId is None:
            logger.exception('teacherId = '+teacherId)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('teacherId = '+teacherId)
            Teacher.objects.filter(teacher_id=teacherId).delete()
    except Teacher.DoesNotExist:
        logger.exeption('Teacher Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delTeacher method")
    return render_to_response("school/teacherList.html", RequestContext(request,{}))

def delBatch(request,batchId):
    logger.info("start of delBatch method")
    try:
        batchId = request.GET.get('batchId',None)
        print batchId
        if batchId is None:
            logger.exception('batchId = '+batchId)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('batchId = '+batchId)
            Batch.objects.filter(batch_id=batchId).delete()
    except Batch.DoesNotExist:
        logger.exeption('Batch Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delBatch method")
    return render_to_response("school/batchList.html", RequestContext(request,{}))

def delSection(request,sectionId):
    logger.info("start of delSection method")
    try:
        sectionId = request.GET.get('sectionId',None)
        if sectionId is None:
            logger.exception('sectionId = '+sectionId)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('sectionId = '+sectionId)
            Sections.objects.filter(sectionId=sectionId).delete()
    except Sections.DoesNotExist:
        logger.exeption('Section Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delSection method")
    return render_to_response("school/sectionList.html", RequestContext(request,{}))

@csrf_exempt
def addSubject(request):
    logger.debug('start of addSubject Method')
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        subjectId = request.POST.get('subjectId')
        subjectName=request.POST.get('subjectName')
        method = request.POST.get('method')
        count = Subject.objects.filter(subject=subjectName).count()
        print count
        if count != 0:
            value = 'false'
        else:
            if method=='add':
                subject=Subject.objects.create(subject = subjectName,create_user = request.user)
                subject.save()
                value = 'save'
            elif method == 'edit':
                s = Subject.objects.get(subject_id=subjectId)  
                s.subject = subjectName
                s.save()
                value = 'updated'
                logger.debug('updated succefully')
    return HttpResponse(value) 

def delSubject(request,subjectId):
    logger.info("start of delSubject method")
    try:
        subjectId = request.GET.get('subjectId',None)
        print subjectId
        if subjectId is None:
            logger.exception('subjectId = '+subjectId)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('subjectId = '+subjectId)
            Subject.objects.filter(subject_id=subjectId).delete()
    except Subject.DoesNotExist:
        logger.exeption('Subject Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delSubject method")
    return render_to_response("school/subjectList.html", RequestContext(request,{}))

@csrf_exempt
def addClass(request):
    logger.debug('start of addClass Method')
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        classId = request.POST.get('classId')
        className=request.POST.get('className')
        method = request.POST.get('method')
        count = Class.objects.filter(class_field=className).count()
        print count
        if count != 0:
            value = 'false'
        else:
            if method=='add':
                class_field=Class.objects.create(class_field = className,create_user = request.user)
                class_field.save()
                value = 'save'
            elif method == 'edit':
                s = Class.objects.get(class_id=classId)  
                s.class_field = className
                s.save()
                value = 'updated'
                logger.debug('updated succefully')
    return HttpResponse(value) 

def delClass(request,classId):
    logger.info("start of delClass method")
    try:
        classId = request.GET.get('classId',None)
        print classId
        if classId is None:
            logger.exception('classId = '+classId)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('classId = '+classId)
            Class.objects.filter(class_id=classId).delete()
    except Class.DoesNotExist:
        logger.exeption('Class Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delClass method")
    return render_to_response("school/classList.html", RequestContext(request,{}))

@csrf_exempt
def addExam(request):
    logger.debug('start of addExam Method')
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        examId = request.POST.get('examId')
        examName=request.POST.get('examName')
        method = request.POST.get('method')
        count = ExamType.objects.filter(exam_type=examName).count()
        print count
        if count != 0:
            value = 'false'
        else:
            if method=='add':
                exam_type=ExamType.objects.create(exam_type = examName,create_user = request.user)
                exam_type.save()
                value = 'save'
            elif method == 'edit':
                s = ExamType.objects.get(exam_type_id=examId)  
                s.exam_type = examName
                s.save()
                value = 'updated'
                logger.debug('updated succefully')
    return HttpResponse(value) 

def delExam(request,examId):
    logger.info("start of delExam method")
    try:
        examId = request.GET.get('examId',None)
        print examId
        if examId is None:
            logger.exception('examId = '+examId)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('examId = '+examId)
            ExamType.objects.filter(exam_type_id=examId).delete()
    except ExamType.DoesNotExist:
        logger.exeption('Exam Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delExam method")
    return render_to_response("school/examList.html", RequestContext(request,{}))

def listBatchClasses(request):
    logger.debug("start of batchList")
    batchClassList = BatchClasses.objects.all()
    batchClass = BatchClassTable(batchClassList)
    return render_to_response("school/batchClassList.html", {'batchClassList':batchClass})

def getBatchClassOptions(request):
    logger.debug("start of getBatchClassOptions")
    batchList_json = serializers.serialize('json', Batch.objects.all())
    batchList = json.loads(batchList_json)
    
    classList_json = serializers.serialize('json',Class.objects.all())
    classList = json.loads(classList_json)
    print classList_json
    json_data = json.dumps( {'batchList':batchList, 'classList':classList} )
    return HttpResponse( json_data)

@csrf_exempt
def addBatchClass(request):
    logger.debug("Start of addBatchClass")
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        batchClassId=request.POST.get('batchClassId')
        batchName=request.POST.get('batchName')
        className = request.POST.get('className')
        method = request.POST.get('method')
        count = BatchClasses.objects.filter(batch=batchName, grade=className).count()
       
        if count != 0:
            value = 'false'
        else:
            if method=='add':              
                batchClass=BatchClasses.objects.create(batch_id = batchName, grade_id=className,create_user = request.user)
                batchClass.save()
                value = 'save'
            elif method == 'edit':
                b = BatchClasses.objects.get(batch_class_id=batchClassId)  
                b.batch = Batch.objects.get(batch_id = batchName)
                b.grade = Class.objects.get(class_id = className)
                b.save()
               
                value = 'updated'
                logger.debug('updated succefully')
    return HttpResponse(value) 

def delBatchClass(request,batchClassId):
    logger.info("start of delBatchClass method")
    try:
        batchClassId = request.GET.get('batchClassId',None)
        print batchClassId
        if batchClassId is None:
            logger.exception('batchClassId = '+batchClassId)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('batchClassId = '+batchClassId)
            BatchClasses.objects.filter(batch_class_id=batchClassId).delete()
    except Batch.DoesNotExist:
        logger.exeption('BatchClass Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delBatchClass method")
    return render_to_response("school/batchClassList.html", RequestContext(request,{}))

def delExamAssign(request,examAssignId):
    logger.info("start of delExamAssign method")
    try:
        examAssignId = request.GET.get('examAssignId',None)
        print examAssignId
        if examAssignId is None:
            logger.exception('examAssignId = '+examAssignId)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('examAssignId = '+examAssignId)
            ExamAssign.objects.filter(exam_assign_id=examAssignId).delete()
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delExamAssign method")
    return render_to_response("school/examAssignList.html", RequestContext(request,{}))

def viewBatchClass(request,batchClassId):
    logger.info("start of viewBatchClass method")
    batchClassId = request.GET.get('batchClassId',None)
    print batchClassId
    batchClass = BatchClasses.objects.filter(batch_class_id=batchClassId)
    data= serializers.serialize("json", batchClass)
    print data
    return HttpResponse(data)
    
def listBatchClassSec(request):
    logger.debug("start of batchClassSecList")
    batchClassSecList = BatchClassSection.objects.all()
    batchClassSec = BatchClassSectionTable(batchClassSecList)
    return render_to_response("school/batchClassSectionList.html", {'batchClassSecList':batchClassSec})
    
def getBatchClassSecOptions(request):
    logger.debug("start of getBatchClassSecOptions")
    batchClasses = BatchClasses.objects.all()
    batches = []
    grades = []
    for item in batchClasses:
        batch_dict = model_to_dict(item.batch)
        grade_dict = model_to_dict(item.grade)
        item_dict = model_to_dict(item)
        item_dict['batch'] = batch_dict
        item_dict['grade'] = grade_dict
        batches.append(item_dict)      
        grades.append(item_dict)  
    
    secList_json = serializers.serialize('json',Sections.objects.all())
    sectionList = json.loads(secList_json)
    result = json.dumps({'batchClassList':batches,'sectionList':sectionList})
    return HttpResponse(result)

@csrf_exempt
def addBatchClassSec(request):
    logger.debug("Start of addBatchClassSec")
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        batchClassSecId=request.POST.get('batchClassSecId')
        print batchClassSecId
        batchName=request.POST.get('batchName')
        className = request.POST.get('className')
        section = request.POST.get('section')
        method = request.POST.get('method')
        print batchName, className, method
        batchClassObj = BatchClasses.objects.filter(batch=batchName, grade=className)
        #logger.debug(batchClassObj.batch_class_id)
        print batchClassObj[0]
        batchClassId = batchClassObj[0].batch_class_id
        count = BatchClassSection.objects.filter(batch_class=batchClassId, class_sec=section).count()
        print count
        if count != 0:
            value = 'false'
        else:
            if method=='add':
                logger.debug('in add')
                
                batchClassSec=BatchClassSection.objects.create(batch_class_id=batchClassId,create_user=request.user)
                batchClassSec.class_sec = Sections.objects.get(sectionId = section)
                logger.debug(batchClassSec)
                batchClassSec.save()
                value = 'save'
            elif method == 'edit':
                b = BatchClassSection.objects.get(batch_class_section_id=batchClassSecId)  
                b.batch_class = BatchClasses.objects.get(batch_class_id = batchClassId)
                b.class_sec = Sections.objects.get(sectionId = section)
                b.save()
                print b
                value = 'updated'
                logger.debug('updated succefully')
    return HttpResponse(value)

def delBatchClassSec(request,batchClassSecId):
    logger.info("start of delBatchClassSec method")
    try:
        batchClassSecId = request.GET.get('batchClassSecId',None)
        print batchClassSecId
        if batchClassSecId is None:
            logger.exception('batchClassSecId = '+batchClassSecId)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('batchClassSecId = '+batchClassSecId)
            BatchClassSection.objects.filter(batch_class_section_id=batchClassSecId).delete()
    except Batch.DoesNotExist:
        logger.exeption('BatchClasssection Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delBatchClassSec method")
    return render_to_response("school/batchClassSectionList.html", RequestContext(request,{}))

def viewBatchClassSec(request,batchClassSecId):
    logger.info("start of viewBatchClass method")
    batchClassSecId = request.GET.get('batchClassSecId',None)
    print batchClassSecId
    batchClassSec = BatchClassSection.objects.filter(batch_class_section_id=batchClassSecId)
    
    batches = []
    grades = []
    for item in batchClassSec:
        batch_dict = model_to_dict(item.batch_class.batch)
        grade_dict = model_to_dict(item.batch_class.grade)
        item_dict = model_to_dict(item)
        item_dict['batch'] = batch_dict
        item_dict['grade'] = grade_dict
        batches.append(item_dict)      
        grades.append(item_dict)  
    
    print 'batches in view ', batches
    print 'grades in view ',grades
    return  JsonResponse(batches, safe=False)
    #data= serializers.serialize("json", batchClassSec)
    #print data
    #return HttpResponse(data)
    
def getclassesBySelectedBatch(request,batchId):
    logger.debug("start of getclassesBySelectedBatch method :")
    batchId = request.GET.get('batchId')
    b_classes = BatchClasses.objects.filter(batch=batchId)
    grades=[]
    for item in b_classes: 
        grade_dict = model_to_dict(item.grade)
        item_dict = model_to_dict(item)
        item_dict['grade'] = grade_dict
        grades.append(item_dict)  
        
    return  JsonResponse(grades, safe=False)
    
    
def examAssignList(request):
    logger.debug("start of examAssignList")
    examAssignList = ExamAssign.objects.all()
    examAssign = ExamAssignTable(examAssignList)
    return render_to_response("school/examAssignList.html", {'examAssignList':examAssign})

@csrf_exempt
def addSyllabus(request):
    logger.debug('start of addClass Method')
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        syllabusId = request.POST.get('syllabusId')
        syllabusName=request.POST.get('syllabusName')
        method = request.POST.get('method')
        count = Syllabus.objects.filter(syllabus=syllabusName).count()
        print count
        if count != 0:
            value = 'false'
        else:
            if method=='add':
                syllabus=Syllabus.objects.create(syllabus = syllabusName,create_user = request.user)
                syllabus.save()
                value = 'save'
            elif method == 'edit':
                s = Syllabus.objects.get(syllabus_id=syllabusId)  
                s.syllabus = syllabusName
                s.save()
                value = 'updated'
                logger.debug('updated succefully')
    return HttpResponse(value)

def classSubject(request):
    logger.debug("start of classSubject")
    classSubjectList = ClassSubject.objects.all()
    classsubject = ClassSubjectTable(classSubjectList)
    return render_to_response("school/listClassSubject.html", {'classSubjectList':classsubject})

@csrf_exempt
def addClassSub(request):
    logger.debug('start of addSchool Method')
    
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        class_subject_id=request.POST.get('class_subject_id')
        class_name=request.POST.get('class_name')
        subject_name=request.POST.get('subject_name')
        method = request.POST.get('method')
        logger.debug(class_name)
        logger.debug(subject_name)
        logger.debug(method)
        #count = ClassSubject.objects.filter(grade_id=class_name).count()
        #logger.debug(count)
        flag = 0
        if method=='edit':
            logger.debug("INDsas")
            s = ClassSubject.objects.get(class_subject_id=class_subject_id)
            
            if s.grade_id != class_name:
                s.grade_id = class_name
                flag = 1
            
            if s.subject_id != subject_name:
                s.subject_id = subject_name
                flag = 1
            
            if flag == 1:
                s.save()
            else:
                print 'No changes detected'
        
        #elif count != 0:
         #   value = 'false'
        else:
            if method=='add':
                logger.debug("InsideADD")
                school=ClassSubject.objects.create(subject_id = subject_name, grade_id=class_name, create_user = request.user)
                school.save()
                print 'saved'   
                value = 'save'
            #elif method == 'edit':
                #s = School.objects.get(school_code=school_code)  
                #s.school_name = schoolName
                #s.save()
                #value = 'updated'
                #logger.debug('updated successfully')
    return HttpResponse(value) 

def delClassSubject(request,ID):
    logger.info("start of delSchool method")
    try:
        ID = request.GET.get('ID',None)
        print ID
        if ID is None:
            logger.exception('ID = '+ID)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('ID = '+ID)
            ClassSubject.objects.filter(class_subject_id=ID).delete()
    except ClassSubject.DoesNotExist:
        logger.exeption('School Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delSchool method")
    return render_to_response("school/listClassSubject.html", RequestContext(request,{}))

def viewClassSubject(request,ID):
    ID = request.GET.get('ID',None)
    print 'ID ', ID
    classSubject = ClassSubject.objects.filter(class_subject_id=ID)
    print classSubject
    data= serializers.serialize("json", classSubject)
    print data
    return HttpResponse(data)

def ExamTypeSyll(request):
    logger.debug("start of examTypeSyllabus")
    ampList = ExamTypeSyllabus.objects.all()
    logger.debug(ampList)
    examSyllabus = ExamSyllabusTable(ampList)
    return render_to_response("school/examTypeSyllabusList.html", {'ampList':examSyllabus})

def getSubjectByClass(request):
    logger.debug("inside getSubjectByClass")
    class_id = request.GET.get('class_id')
    logger.debug(class_id)
    subject = ClassSubject.objects.filter(grade=class_id)
    classValue = ClassSubject.objects.filter(grade=class_id).values('class_subject_id')
    logger.debug(subject)
    logger.debug(classValue)
    subjects=[]
    for item in subject:
        grade_dict = model_to_dict(item.subject)
        item_dict = model_to_dict(item)
        item_dict['subject'] = grade_dict
        subjects.append(item_dict)
    logger.debug(subjects)
    return  JsonResponse(subjects, safe=False)

def getClassSubjectId(request):
    logger.debug("inside getSubjectByClass")
    classDropdownId = request.GET.get('classDropdownId')
    subjectDropdownId = request.GET.get('subjectDropdownId')
    logger.debug(classDropdownId)
    logger.debug(subjectDropdownId)
    class_subject_id = ClassSubject.objects.filter(grade=classDropdownId, subject=subjectDropdownId)
    logger.debug(class_subject_id)
    #data = serializers.serialize('json',class_subject_id )
    subjectsDict=[]
    for item in class_subject_id :
        dict=model_to_dict(item)
        subjectsDict.append(dict) 
    logger.debug(subjectsDict)
    return  JsonResponse(subjectsDict, safe=False)

def getExamTypeList(request):
    examTypeL = ExamType.objects.all()
    data= serializers.serialize("json", examTypeL)
    return HttpResponse(data)

@csrf_exempt
def addExamTypeSyllabus(request):
    logger.debug('start of addExamTypeSyllabus Method')
    
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        examTypeSyllabusId = request.POST.get('examTypeSyllabusId')
        syllabus_id=request.POST.get('syllabus_id')
        exam_type_id=request.POST.get('exam_type_id')
        method = request.POST.get('method')
        logger.debug(syllabus_id)
        logger.debug(exam_type_id)
        logger.debug(method)
        #count = ClassSubject.objects.filter(grade_id=class_name).count()
        #logger.debug(count)
        flag = 0
        if method=='edit':
            logger.debug("INDsas")
            s = ExamTypeSyllabus.objects.get(exmaType_syll_id=examTypeSyllabusId)
            
            if s.syllabus_id != syllabus_id:
                s.syllabus_id = syllabus_id
                flag = 1
            
            if s.exam_type_id != exam_type_id:
                s.exam_type_id = exam_type_id
                flag = 1
            
            if flag == 1:
                s.save()
            else:
                print 'No changes detected'
        
        #elif count != 0:
         #   value = 'false'
        else:
            if method=='add':
                logger.debug("InsideADD")
                examTypeSyllabusData=ExamTypeSyllabus.objects.create(syllabus_id = syllabus_id, exam_type_id=exam_type_id, create_user = request.user)
                examTypeSyllabusData.save()
                print 'saved'   
                value = 'save'
            #elif method == 'edit':
                #s = School.objects.get(school_code=school_code)  
                #s.school_name = schoolName
                #s.save()
                #value = 'updated'
                #logger.debug('updated successfully')
    return HttpResponse(value) 

def getSylDetails(request,schoolCode):
    examTypeSyllabusID = request.GET.get('examTypeSyllabusID',None)
    print 'examTypeSyllabusID ', examTypeSyllabusID
    exsyl = ExamTypeSyllabus.objects.filter(exmaType_syll_id=examTypeSyllabusID)
    print exsyl
    data= serializers.serialize("json", exsyl)
    print data
    return HttpResponse(data)

def delExamSyllabus(request,examTypeSyllabusID):
    logger.info("start of delSchool method")
    try:
        examTypeSyllabusID = request.GET.get('examTypeSyllabusID',None)
        print examTypeSyllabusID
        if examTypeSyllabusID is None:
            logger.exception('examTypeSyllabusID = '+examTypeSyllabusID)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('examTypeSyllabusID = '+examTypeSyllabusID)
            ExamTypeSyllabus.objects.filter(exmaType_syll_id=examTypeSyllabusID).delete()
    except ExamTypeSyllabus.DoesNotExist:
        logger.exeption('School Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delSchool method")
    return render_to_response("school/examTypeSyllabusList.html", RequestContext(request,{}))

def getSyllabusDetails(request):
    logger.debug("inside getSyllabusDetails")
    syllabusId = request.GET.get('syllabusId')
    logger.debug(syllabusId)
    syllabus = Syllabus.objects.filter(class_subject_id=syllabusId)
    logger.debug(syllabus)
    #data = serializers.serialize('json',syllabus)
    syllabusDetails=[]
    for item in syllabus :
        dict=model_to_dict(item)
        syllabusDetails.append(dict) 
    logger.debug(syllabusDetails)
    return  JsonResponse(syllabusDetails, safe=False)


#code by gaurav bhargava
def getClass(request):
    classList_json = serializers.serialize('json',Class.objects.all())
    classList = json.loads(classList_json)
   
    examTypeList_json = serializers.serialize('json',ExamType.objects.all())
    examTypeList = json.loads(examTypeList_json)
    
    sectionList_json = serializers.serialize('json',Sections.objects.all())
    sectionList = json.loads(sectionList_json)
    
    batchList_json = serializers.serialize('json',Batch.objects.all())
    batchList = json.loads(batchList_json)
    
    periodList_json = serializers.serialize('json',Period.objects.all())
    periodList = json.loads(periodList_json)
    
    teacherList_json = serializers.serialize('json',Teacher.objects.all())
    teacherList = json.loads(teacherList_json)
    
    json_data = json.dumps( {'classList':classList, 'examTypeList':examTypeList,'sectionList': sectionList, 'batchList':batchList,'periodList':periodList,'teacherList':teacherList} )
    return HttpResponse(json_data)

def getSyllabus(request):
    class_id = request.GET.get('class_id')
    subject_id = request.GET.get('subject_id')
    class_subject = ClassSubject.objects.filter(grade=class_id,subject=subject_id)
    for item in class_subject :
        #clas_sub_id.append(item.class_subject_id)
        clas_sub = item.class_subject_id
    syllabus_ids = Syllabus.objects.filter(class_subject= clas_sub)
    syl_ids = []
    for item in syllabus_ids: 
        syl_ids.append(item)
    print syl_ids, "syl_ids"
    
    syl_json= serializers.serialize('json', syl_ids)
    sylList = json.loads(syl_json)
    data = json.dumps( {'sylList':sylList} )
    print data,"data"
    return HttpResponse(data)

def getExamType(request):
    class_id = request.GET.get('class_id')
    subject_id = request.GET.get('subject_id')
    syllabus_id = request.GET.get('syllabus_id')
    class_subject = ClassSubject.objects.filter(grade=class_id,subject=subject_id)
    for item in class_subject :
        #clas_sub_id.append(item.class_subject_id)
        clas_sub = item.class_subject_id
    exam_type = Syllabus.objects.get(class_subject= clas_sub,syllabus_id=syllabus_id)
    examDict={'examType':model_to_dict(exam_type.exam_type)}
    
   
    print examDict
    return JsonResponse(examDict)

def getClassSubject(request):
    class_id = request.GET.get('class_id')
    batch_id = request.GET.get('batch_id')
    print class_id, "class_id"
    subjectList = ClassSubject.objects.filter(grade=class_id).prefetch_related('subject')
    print subjectList,"subjectList"
    subject=[]
    for item in subjectList : 
        print item.subject,"item.subject"
        subject.append(item.subject)
        print subject,"subject"
    subject_json = serializers.serialize('json', subject)
    subjectList1 = json.loads(subject_json)
    print "subjectList1",subjectList1
    
    sectionList = ClassSection.objects.filter(class_field=class_id).prefetch_related('section')
    section=[]
    for item in sectionList:
        section.append(item.section)
    section_json = serializers.serialize('json', section)
    sectionList1 = json.loads(section_json)



    sectionAccBatchList = BatchClassSection.objects.filter(batch_class__in = BatchClasses.objects.filter(batch=batch_id,grade=class_id))
    print sectionAccBatchList
    section2=[]
    for item in sectionAccBatchList:
        section2.append(item.class_sec)
    section_json2 = serializers.serialize('json', section2)
    sectionList2 = json.loads(section_json2)

    json_data = json.dumps( {'subjectList1':subjectList1, 'sectionList1':sectionList1,'sectionList2':sectionList2 } )
    return HttpResponse(json_data)



def getBatchClass(request):
    batch_id= request.GET.get('batch_id')
    classList = BatchClasses.objects.filter(batch=batch_id).prefetch_related('grade')
    grade = []
    for item in classList:
        grade.append(item.grade)
    class_json = serializers.serialize('json', grade)
    print class_json
    classList1 = json.loads(class_json)
    print classList1
    json_data = json.dumps( {'classList1': classList1} )
    return HttpResponse(json_data)

def getBatchClassTeacher(request):
    batch= request.GET.get('batch')
    class_name= request.GET.get('class_name')
    section= request.GET.get('section')
    subject= request.GET.get('subject')
    
    class_subject = ClassSubject.objects.filter(grade=class_name,subject=subject)
    for item in class_subject :
        clas_sub = item.class_subject_id
        print clas_sub, "clas_sub"
        
    batch_class = BatchClasses.objects.filter(batch=batch, grade= class_name)
    for item in batch_class:
        batch_class_id = item.batch_class_id
        print batch_class_id,"batch_class_id"
    
    batch_class_sec = BatchClassSection.objects.filter(batch_class=batch_class_id,class_sec=section)
    print batch_class_sec
    
    for item in batch_class_sec:
        b_c_s = item.batch_class_section_id
        print b_c_s,"batch_class_section_id"
    
    class_teacher = ClassTeacher.objects.filter(batch_class_sec= b_c_s)
    for item in class_teacher:
        class_teacher_id = item.class_teacher_id
        print class_teacher_id,"class_teacher_id"
    
    teacherList = ClassTeacherSubject.objects.filter(class_subject=clas_sub,class_teacher=class_teacher)
    teacher=[] 
    for item in teacherList: 
        teacher.append(item.class_teacher.teacher)
        print teacher,"teacher"
    class_json = serializers.serialize('json', teacher)
    print class_json
    classList1 = json.loads(class_json)
    print classList1
    json_data = json.dumps( {'classList1': classList1} )
    return HttpResponse(json_data)

def getClassSectionDetails(request,classSectionId):
    classSectionId = request.GET.get('classSectionId',None)
    print 'classSectionId ', classSectionId
    classSec = ClassSection.objects.filter(class_sec_id=classSectionId)
    print classSec
    data= serializers.serialize("json", classSec)
    print data
    return HttpResponse(data)

def getClassTimetableDetails(request,classTimetableCode):
    classTimetableCode = request.GET.get('classTimetableCode',None)
    print 'classTimetableCode ', classTimetableCode
    classTT = ClassTimetable.objects.filter(class_timetable_id=classTimetableCode)
    
    grades = []
    subjects = []
    sections = []
    periods = []  
    for item in classTT:
        grades_dict = model_to_dict(item.class_subject.grade)
        subject_dict = model_to_dict(item.class_subject.subject)
        section_dict = model_to_dict(item.class_section.section)
        period_dict = model_to_dict(item.period)
        item_dict = model_to_dict(item)
        item_dict['subjects'] = subject_dict
        item_dict['grades'] = grades_dict
        item_dict['sections'] = section_dict
        item_dict['periods'] = period_dict
        grades.append(item_dict)      
        subjects.append(item_dict)  
        sections.append(item_dict)
        periods.append(item_dict)
        print grades
    return  JsonResponse(grades, safe=False)
    #data= serializers.serialize("json", clas_sub)
    #print data
    #return HttpResponse(data)

def getExamAssign(request,examAssignCode):
    examAssignCode = request.GET.get('examAssignCode',None)
    print 'examAssignCode ', examAssignCode
    examAssign = ExamAssign.objects.filter(exam_assign_id=examAssignCode)
    
    grades = []
    subjects = []
    syllabus = []
    for item in examAssign:
        grades_dict = model_to_dict(item.class_sub_syll.syllabus.class_subject.grade)
        subject_dict = model_to_dict(item.class_sub_syll.syllabus.class_subject.subject)
        syllabus_dict = model_to_dict(item.class_sub_syll.syllabus)
        item_dict = model_to_dict(item)
        item_dict['subjects'] = subject_dict
        item_dict['grades'] = grades_dict
        item_dict['syllabus'] = syllabus_dict
        grades.append(item_dict)      
        subjects.append(item_dict)  
        syllabus.append(item_dict)
    print grades,"grades"
    return  JsonResponse(grades, safe=False)

def getTeacherTimetableDetails(request,teacherTimetableCode):
    teacherTimetableCode = request.GET.get('teacherTimetableCode',None)
    print 'teacherTimetableCode ', teacherTimetableCode
    teacherTT = TeacherTimetable.objects.filter(teacher_timetable_id=teacherTimetableCode)
    batches = []
    grades = []
    subjects = []
    sections = []
    teachers = []
    periods = []
    for item in teacherTT:
        grades_dict = model_to_dict(item.class_teacher_sub.class_teacher.batch_class_sec.batch_class.grade)
        subject_dict = model_to_dict(item.class_teacher_sub.class_subject.subject)
        section_dict = model_to_dict(item.class_teacher_sub.class_teacher.batch_class_sec.class_sec)
        batch_dict = model_to_dict(item.class_teacher_sub.class_teacher.batch_class_sec.batch_class.batch)
        teacher_dict = model_to_dict(item.class_teacher_sub.class_teacher.teacher)
        period_dict = model_to_dict(item.period)
        item_dict = model_to_dict(item)
        item_dict['subjects'] = subject_dict
        item_dict['grades'] = grades_dict
        item_dict['sections'] = section_dict
        item_dict['batches'] = batch_dict
        item_dict['teachers'] = teacher_dict
        item_dict['periods'] = period_dict
        grades.append(item_dict)      
        subjects.append(item_dict)  
        sections.append(item_dict)
        batches.append(item_dict)
        teachers.append(item_dict)
        periods.append(item_dict)
        print grades,"grades"
    return  JsonResponse(grades, safe=False)

def listClassTimetable(request):
    logger.debug("start of listClassTimetable")
    try:
        classList = Class.objects.values('class_id','class_field')
        print classList,"classList"
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{})) 
    return render_to_response("school/classTimetableList.html", {'classTimetableList':classTimetable})

def listClassTimetable1(request):
    try:
        logger.debug("start of listClassTimetable1")
        classTimetableList = ClassTimetable.objects.all()
        print classTimetableList,"classTimetableList"
        classTimetable = ClassTimetableTable(classTimetableList)
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{})) 
    return render_to_response("school/classTimetableList1.html", {'classTimetableList':classTimetable})
    logger.debug("listClassTimetable1 over ")

def listTeacherTimetable(request):
    logger.debug("start of listTeacherTimetable")
    try:
        teacherList = Teacher.objects.values('teacher_first_name','teacher_last_name')
        print teacherList,"taecherlist"
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{})) 
    return render_to_response("school/teacherTimetableList.html", {'teacherList':teacherList})

def listTeacherTimetable1(request):
    try:
        logger.debug("start of listTeacherTimetable1")
        teacherTimetableList = TeacherTimetable.objects.all()
        logger.debug(teacherTimetableList)
        teacherTimetable = TeacherTimetableTable(teacherTimetableList)
        logger.debug(teacherTimetable)
        print teacherTimetable,"asdasdasdjalsdjk"
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{})) 
    return render_to_response("school/teacherTimetableList1.html", {'teacherTimetableList':teacherTimetable})
    logger.debug("teacherTimetable over ")
    
def listClassSection(request):
    logger.debug("start of listClassSection")
    classSectionList = ClassSection.objects.all()
    classSection = ClassSectionTable(classSectionList)
    return render_to_response("school/classSectionList.html", {'classSectionList':classSection})



@csrf_exempt
def addClassSection(request):
    logger.debug('start of addClassSection Method')
    value = 'empty'
    try: 
        if request.is_ajax() and request.method=='POST':
            classSectionId = request.POST.get('classSectionId')
            className = request.POST.get('className')
            section = request.POST.get('section')
            method = request.POST.get('method')
            print classSectionId,"asdasd"
            print className,"asdjahsdjlkjaklj"
            print section,"asldhajlkdjakls"
            count = ClassSection.objects.filter(class_field=className,section=section).count()
            if count != 0 :
                value='false'
            else :
                if method=='edit':
                    print "comgin in edit"
                    b = ClassSection.objects.get(class_sec_id=classSectionId)
                    b.class_field = Class.objects.get(class_id=className)
                    b.section = Sections.objects.get(sectionId=section) 
                    b.save()
                    value = 'updated'
                    logger.debug("updated successfully")
           
                
               
                elif method=='add':
                    print "coming in add"
                    classNameField = Class.objects.get(class_id=className)
                    sectionField = Sections.objects.get(sectionId=section)
                    classSection =ClassSection.objects.create(class_field =classNameField ,section=sectionField,create_user = request.user)
                    classSection.save()
                    value = 'save'
        print value,"value"
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))      
    return HttpResponse(value) 
                
@csrf_exempt
def classTimetable(request):
    
    logger.debug('start of classTimetable Method')
    value = 'empty'
    try:
        if request.is_ajax() and request.method=='POST':
            class_timetable_id = request.POST.get('class_timetable_id')
            print class_timetable_id
            class_name = request.POST.get('class_name')
            subject = request.POST.get('subject')
            section = request.POST.get('section')
            period = request.POST.get('period')
            day = request.POST.get('day')
            method = request.POST.get('method')
            class_sub = ClassSubject.objects.filter(grade=class_name,subject=subject)
            class_sec = ClassSection.objects.filter(class_field=class_name,section=section)
            
            for item in class_sub :
                clas_sub = item.class_subject_id
                print clas_sub, "asdkakjsdhlj"
            for item in class_sec:
                clas_sec = item.class_sec_id
                print clas_sec, "clas_+sec"
           
            count = ClassTimetable.objects.filter(class_section = clas_sec,class_subject=clas_sub,period=period,day=day).count()
            if count != 0 :
                value='false'
            else :
                if method=='edit':
                    logger.debug("comgin in edit ")
                    b = ClassTimetable.objects.get(class_timetable_id=class_timetable_id)
                    b.class_subject = ClassSubject.objects.get(class_subject_id = clas_sub)
                    b.class_section = ClassSection.objects.get(class_sec_id = clas_sec)
                    b.period = Period.objects.get(period_id=period)
                    b.day = day
                    b.save()
                    value = 'updated'
                    logger.debug("updated successfully")
            
                if method=='add':
                    print "coming in add"
                    class_subj = ClassSubject.objects.get(class_subject_id = clas_sub)
                    class_sect = ClassSection.objects.get(class_sec_id = clas_sec)
                    peri = Period.objects.get(period_id=period)
                    print class_subj, "jahdsjkahsdjha"
                    timetable=ClassTimetable.objects.create(class_subject= class_subj,class_section=class_sect,period=peri,day=day,create_user = request.user)
                    timetable.save()
                    value = 'save'
        print value,"value"
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))      
    return HttpResponse(value) 

@csrf_exempt
def teacherTimetable(request):
    
    logger.debug('start of teacherTimetable Method')
    value = 'empty'
    try:
        if request.is_ajax() and request.method=='POST':
            teacher_timetable_id = request.POST.get('teacher_timetable_id')
            print teacher_timetable_id
            batch = request.POST.get('batch')
            class_name = request.POST.get('class_name')
            subject = request.POST.get('subject')
            section = request.POST.get('section')
            teacher = request.POST.get('teacher')
            period = request.POST.get('period')
            print period,"period"
            day = request.POST.get('day')
            method = request.POST.get('method')
            
            class_sub = ClassSubject.objects.filter(grade=class_name,subject=subject)
            for item in class_sub :
                clas_sub = item.class_subject_id
                print clas_sub, "clas_sub"
            batch_class = BatchClasses.objects.filter(batch=batch,grade= class_name)
            for item in batch_class:
                bat_clas = item.batch_class_id
                print bat_clas, "bat_clas"
            bat_class_sec = BatchClassSection.objects.filter(batch_class=bat_clas,class_sec=section)
            for item in bat_class_sec:
                b_c_s = item.batch_class_section_id
                print b_c_s,"b_c_s"
            class_teach = ClassTeacher.objects.filter(batch_class_sec=b_c_s,teacher=teacher)
            for item in class_teach:
                c_t = item.class_teacher_id
                print c_t,"ct"
            class_teach_sub = ClassTeacherSubject.objects.filter(class_teacher=c_t,class_subject= clas_sub)
            for item in class_teach_sub:
                c_t_s = item.class_teacher_sub_id
                print c_t_s,"cts"
            count = TeacherTimetable.objects.filter(class_teacher_sub_id=c_t_s,day=day,period=period).count()
            if count != 0: 
                value = 'false'
            else:
                if method=='edit':
                    b = TeacherTimetable.objects.get(teacher_timetable_id=teacher_timetable_id)
                    b.class_teacher_sub = ClassTeacherSubject.objects.get(class_teacher_sub_id=c_t_s)
                    b.period = Period.objects.get(period_id=period)
                    b.day = day
                    b.save()
                    value = 'updated'
                    logger.debug("updated successfully")
                
                if method=='add':
                    print "coming in add"
                    per = Period.objects.get(period_id=period)
                    timetable=TeacherTimetable.objects.create(class_teacher_sub_id=c_t_s,period=per,day=day,create_user = request.user)
                    timetable.save()
                    value = 'save'
        print value,"value"
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))      
    return HttpResponse(value) 

def delClassSection(request,classSectionId):
    logger.info("start of delClassSection method")
    try:
        classSectionId = request.GET.get('classSectionId',None)
        print classSectionId
        if classSectionId is None:
            logger.exception('classSectionId = '+classSectionId)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('classSectionId = '+classSectionId)
            ClassSection.objects.filter(class_sec_id=classSectionId).delete()
    except ClassSection.DoesNotExist:
        logger.exeption('ClassSection Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delClassSection method")
    return render_to_response("school/classSectionList.html", RequestContext(request,{}))

def delClassTimetable(request,classTimetableCode):
    logger.info("start of delClassTimetable method")
    try:
        classTimetableCode = request.GET.get('classTimetableCode',None)
        print classTimetableCode
        if classTimetableCode is None:
            logger.exception('classTimetableCode = '+classTimetableCode)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('classTimetableCode = '+classTimetableCode)
            ClassTimetable.objects.filter(class_timetable_id=classTimetableCode).delete()
    except ClassSubject.DoesNotExist:
        logger.exeption('Class Subject does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delClassTimetable method")
    return render_to_response("school/classTimeTableList1.html", RequestContext(request,{}))

def delTeacherTimetable(request,teacherTimetableCode):
    logger.info("start of delTeacherTimetable method")
    try:
        teacherTimetableCode = request.GET.get('teacherTimetableCode',None)
        print teacherTimetableCode
        if teacherTimetableCode is None:
            logger.exception('teacherTimetableCode = '+teacherTimetableCode)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('teacherTimetableCode = '+teacherTimetableCode)
            TeacherTimetable.objects.filter(teacher_timetable_id=teacherTimetableCode).delete()
    except ClassTeacherSubject.DoesNotExist:
        logger.exeption('Class Subject Teacher does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delTeacherTimetable method")
    return render_to_response("school/teacherTimeTableList1.html", RequestContext(request,{}))

@csrf_exempt
def assignExams(request):
    logger.debug('start of assignExams Method')
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        examAssignCode= request.POST.get('examAssignCode')
        class_name = request.POST.get('class_name')
        print class_name, "asdahjskdaskdjh"
        exam_type=request.POST.get('exam_type')
        subject = request.POST.get('subject')
        syllabus = request.POST.get('syllabus')
        from_time = request.POST.get('from_time')
        to_time = request.POST.get('to_time')
        date = request.POST.get('date')
        day = request.POST.get('day')
        method = request.POST.get('method')
        print exam_type,syllabus,"examtye pand syll"
        
        class_subject_detail = ClassSubject.objects.get(grade= class_name, subject=subject)
        print class_subject_detail, "casllasdajhsdajksdh"
       
        sylla = Syllabus.objects.filter(class_subject=class_subject_detail.class_subject_id,exam_type=exam_type,syllabus=syllabus)
        print sylla,"sylla"
        for items in sylla:
            print items.syllabus_id,"asdajskl"
            syll = items.syllabus_id
            print syll,"syll"
        class_sub_syll_id = ExamTypeSyllabus.objects.filter(syllabus=syll)
        for items in class_sub_syll_id:
            c_s_s = items.exmaType_syll_id
            print c_s_s,"css"
        count = ExamAssign.objects.filter(class_sub_syll=c_s_s,from_time=from_time,to_time=to_time,date=date,day=day).count()
        if count != 0:
            value = 'false'
        else:
            if method=='add':
                syllab = ExamTypeSyllabus.objects.get(exmaType_syll_id=c_s_s)
                examAssign = ExamAssign.objects.create(class_sub_syll=syllab,from_time=from_time,to_time=to_time,date=date,day=day,create_user = request.user)
                examAssign.save()
                value = 'save'
            elif method == 'edit':
                syllab = ExamTypeSyllabus.objects.get(exmaType_syll_id=c_s_s)
                b = ExamAssign.objects.get(exam_assign_id=examAssignCode)
                b.class_sub_syll=syllab
                b.from_time=from_time
                b.to_time=to_time
                b.date=date
                b.day=day
                b.save()
                value = 'updated'
                logger.debug('updated succefully')
    return HttpResponse(value) 


@csrf_exempt
def addSyllabusTopic(request):
    logger.debug('start of addSyllabus Method')
    
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        class_subject_id=request.POST.get('class_subject_id')
        syllabusId=request.POST.get('syllabusId')
        examType=request.POST.get('examType')
        syllabusName=request.POST.get('syllabusName')
        topicName=request.POST.get('topicName')
        method = request.POST.get('method')
        logger.debug(class_subject_id)
        logger.debug(syllabusName)
        logger.debug(topicName)
        logger.debug(method)
        logger.debug(syllabusId)
        #count = ClassSubject.objects.filter(grade_id=class_name).count()
        #logger.debug(count)
        flag = 0
        if method=='edit':
            logger.debug("INDsas")
            s = Syllabus.objects.get(syllabus_id=syllabusId)
            y = ExamTypeSyllabus.objects.get(syllabus_id=syllabusId)
            
            if s.syllabus != syllabusName:
                s.syllabus = syllabusName
                flag = 1
            
            if s.topic != topicName:
                s.topic = topicName
                flag = 1
                
            if s.class_subject_id != class_subject_id:
                s.class_subject_id = class_subject_id
                flag = 1
                
                    
            if s.exam_type_id != examType:
                s.exam_type_id = examType
                flag = 1
                y.exam_type_id = examType
            
            if flag == 1:
                s.save()
                y.save()
            else:
                print 'No changes detected'
        
        #elif count != 0:
         #   value = 'false'
        else:
            if method=='add':
                logger.debug("InsideADD")
                addSyllabus=Syllabus.objects.create(class_subject_id=class_subject_id, syllabus=syllabusName, topic = topicName, exam_type_id = examType, create_user = request.user)
                addSyllabus.save()
                logger.debug(addSyllabus.syllabus_id)
                logger.debug(addSyllabus.exam_type_id)
                entry = ExamTypeSyllabus.objects.create(syllabus_id=addSyllabus.syllabus_id, exam_type_id=addSyllabus.exam_type_id, create_user = request.user)
                entry.save()
                logger.debug(addSyllabus)
                
                print 'saved'   
                value = 'save'
            #elif method == 'edit':
                #s = School.objects.get(school_code=school_code)  
                #s.school_name = schoolName
                #s.save()
                #value = 'updated'
                #logger.debug('updated successfully')
    return HttpResponse(value)

def delSyllabus(request,syllabusId):
    logger.info("start of delSyllabus method")
    try:
        syllabusId = request.GET.get('syllabusId',None)
        print syllabusId
        if syllabusId is None:
            logger.exception('syllabusId = '+syllabusId)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('syllabusId = '+syllabusId)
            Syllabus.objects.filter(syllabus_id=syllabusId).delete()
    except Syllabus.DoesNotExist:
        logger.exeption('School Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delSchool method")
    return render_to_response("school/syllabusList.html", RequestContext(request,{}))

def viewSyllabus(request,syllabusId):
    logger.debug("In syllabusDetails")
    syllabusId = request.GET.get('syllabusId',None)
    print 'syllabusId ', syllabusId
    syllabusDetails = Syllabus.objects.filter(syllabus_id=syllabusId)
    print syllabusDetails
    batches = []
    grades = []
    for item in syllabusDetails:
        batch_dict = model_to_dict(item.class_subject.grade)
        print "exam -- ", item.class_subject.grade
        grade_dict = model_to_dict(item.class_subject.subject)
        print "exam -- ", item.class_subject.subject
        item_dict = model_to_dict(item)
        item_dict['grade'] = batch_dict
        item_dict['subject'] = grade_dict
        batches.append(item_dict)      
        grades.append(item_dict)
    
    print 'syllabusDetails in view ', batches
    return  JsonResponse(batches, safe=False)

def getTeacherDetails(request):
    teacher_id = request.GET.get('teacher_id')
    print teacher_id,"teacher_id"
    try:
        #class_teacher = ClassTeacher.objects.filter(teacher=teacher_id)
        #class_t=[]
        #for items in class_teacher:
        #    class_t.append(items.class_teacher_id)
        #    print class_t,"class_t"
        class_teacher_sub = ClassTeacherSubject.objects.filter(class_teacher__in=ClassTeacher.objects.filter(teacher=teacher_id).values('class_teacher_id'))
        teacherTimetable = TeacherTimetable.objects.filter(class_teacher_sub__in=class_teacher_sub)
        
        
        subjects=[]
        grades = []
        batches = []
        sections = []
        teachers = []
        periods= []
        for item in teacherTimetable:
            batch_dict = model_to_dict(item.class_teacher_sub.class_teacher.batch_class_sec.batch_class.batch)
            grade_dict = model_to_dict(item.class_teacher_sub.class_teacher.batch_class_sec.batch_class.grade)
            subject_dict = model_to_dict(item.class_teacher_sub.class_subject.subject)
            section_dict = model_to_dict(item.class_teacher_sub.class_teacher.batch_class_sec.class_sec)
            teacher_dict = model_to_dict(item.class_teacher_sub.class_teacher.teacher)
            period_dict = model_to_dict(item.period)
            item_dict = model_to_dict(item)
            item_dict['batch'] = batch_dict
            item_dict['grade'] = grade_dict
            item_dict['subject'] = subject_dict
            item_dict['section'] = section_dict
            item_dict['teacher'] = teacher_dict
            item_dict['period'] = period_dict
            batches.append(item_dict)      
            grades.append(item_dict) 
            subjects.append(item_dict)
            sections.append(item_dict)
            teachers.append(item_dict)
            periods.append(item_dict) 
        print teachers,"teachers"
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))      
    
    return  JsonResponse(teachers, safe=False)


def getClassTimeDetails(request):
    class_id = request.GET.get('class_id')
    section_id = request.GET.get('section_id')
    try:
        class_sub = ClassSubject.objects.filter(grade= class_id).values('class_subject_id')
        class_sec = ClassSection.objects.filter(class_field=class_id,section=section_id).values('class_sec_id')
        classTimetable = ClassTimetable.objects.filter(class_subject__in=class_sub,class_section__in=class_sec)
        print "classTimetable",classTimetable
        subjects=[]
        grades = []
        sections = []
        periods= []
        for item in classTimetable:
            grade_dict = model_to_dict(item.class_subject.grade)
            subject_dict = model_to_dict(item.class_subject.subject)
            section_dict = model_to_dict(item.class_section.section)
            period_dict = model_to_dict(item.period)
            item_dict = model_to_dict(item)
            item_dict['grade'] = grade_dict
            item_dict['subject'] = subject_dict
            item_dict['section'] = section_dict
            item_dict['period'] = period_dict
            grades.append(item_dict) 
            subjects.append(item_dict)
            sections.append(item_dict)
            periods.append(item_dict) 
        print grades,"grades"
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))      
    
    return  JsonResponse(grades, safe=False)
    
    



def listClassTeacher(request):
    logger.debug("start of listClassTeacher")
    classTeacherList = ClassTeacher.objects.all()
    classTeacher = ClassTeacherTable(classTeacherList)
    return render_to_response("school/classTeacher.html", {'classTeacher':classTeacher})

def delClassTeacher(request,ID):
    logger.info("start of delClassTeacher method")
    try:
        ID = request.GET.get('ID',None)
        print ID
        if ID is None:
            logger.exception('ID = '+ID)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('ID = '+ID)
            ClassTeacher.objects.filter(class_teacher_id=ID).delete()
    except ClassTeacher.DoesNotExist:
        logger.exeption('Class Teacher Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delClassTeacher method")
    return render_to_response("school/classTeacher.html", RequestContext(request,{}))

@csrf_exempt
def addClassTeacher(request):
    logger.debug('start of addClassTeacher Method')
    value = 'empty'
    try: 
        if request.is_ajax() and request.method=='POST':
            classTeacherId = request.POST.get('classTeacherId')
            class_name = request.POST.get('class_name')
            section_name = request.POST.get('section_name')
            batch_name = request.POST.get('batch_name')
            teacher_name = request.POST.get('teacher_name')
            method = request.POST.get('method')
            print class_name,section_name,batch_name,teacher_name,"asdasd"
            batchClass = BatchClasses.objects.filter(batch=batch_name,grade=class_name)
            batchClassId = batchClass[0].batch_class_id
            batchClassSec = BatchClassSection.objects.filter(batch_class=batchClassId,class_sec=section_name)
            print batchClassSec
            batchClassSecId = batchClassSec[0].batch_class_section_id 
            count = ClassTeacher.objects.filter(batch_class_sec=batchClassSecId,teacher=teacher_name).count()
            print count
            if count != 0 :
                value='false'
            else :
                if method=='edit':
                    print "comgin in edit"
                    classTeacher = ClassTeacher.objects.get(class_teacher_id=classTeacherId)
                    classTeacher.batch_class_sec = BatchClassSection.objects.get(batch_class_section_id=batchClassSecId)
                    classTeacher.teacher = Teacher.objects.get(teacher_id = teacher_name)
                    logger.debug(classTeacher)
                    classTeacher.save()
                    value = 'updated'
                    logger.debug("updated successfully")
           
                elif method=='add':
                    print "coming in add"
                    classTeacher=ClassTeacher.objects.create(create_user=request.user)
                    classTeacher.batch_class_sec = BatchClassSection.objects.get(batch_class_section_id=batchClassSecId)
                    classTeacher.teacher = Teacher.objects.get(teacher_id = teacher_name)
                    logger.debug(classTeacher)
                    classTeacher.save()
                    value = 'save'
        print value,"value"
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))      
    return HttpResponse(value) 

def getSecAccBatchClass(request):
    logger.debug("start of getSecAccBatchClass")
    batchName=request.GET.get('batch_id')
    className = request.GET.get('class_id')
    print className,batchName
    batchClassSec = BatchClassSection.objects.filter(batch_class__in=BatchClasses.objects.filter(batch=batchName,grade=className))
    print batchClassSec
    sections = []
    for item in batchClassSec:
        sections_dict = model_to_dict(item.class_sec)
        item_dict = model_to_dict(item)
        item_dict['section'] = sections_dict       
        sections.append(item_dict)      
    print sections    
    return  JsonResponse(sections, safe=False)

def getClassTeacherDetails(request,classTeacherId):
    logger.debug("start of getClassTeacherDetails")
    classTeacherId = request.GET.get('classTeacherId')
    print classTeacherId
    classTeacher = ClassTeacher.objects.filter(class_teacher_id=classTeacherId)
    print classTeacher
    teacher = []
    batch = []
    grade = []
    section = []
    for item in classTeacher:
        item_dict = model_to_dict(item)
        teacher_dict = model_to_dict(item.teacher)       
        item_dict['teacher'] = teacher_dict 
        teacher.append(item_dict)
        
        batch_dict = model_to_dict(item.batch_class_sec.batch_class.batch)       
        item_dict['batch'] = batch_dict       
        batch.append(item_dict)
        
        grade_dict = model_to_dict(item.batch_class_sec.batch_class.grade)       
        item_dict['grade'] = grade_dict       
        grade.append(item_dict) 
        
        section_dict = model_to_dict(item.batch_class_sec.class_sec)       
        item_dict['section'] = section_dict       
        section.append(item_dict)     
    
    print teacher    
    return  JsonResponse(teacher, safe=False)


def populateTeacher(request):
    logger.debug("inside populateTeacher")
    batchClass_SecId = request.GET.get('batchClass_SecId')
    logger.debug(batchClass_SecId)
    teacherName = ClassTeacher.objects.filter(batch_class_sec=batchClass_SecId)
    logger.debug(teacherName)
    teachers=[]
    for item in teacherName:
        grade_dict = model_to_dict(item.teacher)
        item_dict = model_to_dict(item)
        item_dict['teacher'] = grade_dict
        teachers.append(item_dict)
    logger.debug(teachers)
    logger.debug("going back")
    return  JsonResponse(teachers, safe=False)

def classTeacherSubjectList(request):
    logger.debug("start of classTeacherSubjectList")
    classTeachSub = ClassTeacherSubject.objects.all()
    logger.debug(classTeachSub)
    classTeacherSubTable = ClassTeacherSubjectTable(classTeachSub)
    return render_to_response("school/classTeacherSubjectList.html", {'classTeachSub':classTeacherSubTable})

def getBatches(request):
    batchList = Batch.objects.all()
    data= serializers.serialize("json", batchList)
    return HttpResponse(data)

def viewSubject(request):
    logger.debug("inside viewSubject")
    classSubjectID = request.GET.get('classSubjectID')
    logger.debug(classSubjectID)
    subject = ClassSubject.objects.filter(class_subject_id=classSubjectID)
    logger.debug(subject)
    subjects=[]
    for item in subject:
        grade_dict = model_to_dict(item.subject)
        item_dict = model_to_dict(item)
        item_dict['subject'] = grade_dict
        subjects.append(item_dict)
    logger.debug(subjects)
    print 'Subjects are --', subjects
    return  JsonResponse(subjects, safe=False)

def viewSection(request):
    logger.debug("inside viewSection")
    batch_class_secID = request.GET.get('batch_class_secID')
    logger.debug(batch_class_secID)
    subject = BatchClassSection.objects.filter(batch_class_section_id=batch_class_secID)
    logger.debug(subject)
    subjects=[]
    for item in subject:
        grade_dict = model_to_dict(item.class_sec)
        item_dict = model_to_dict(item)
        item_dict['class_sec'] = grade_dict
        subjects.append(item_dict)
    logger.debug(subjects)
    print 'sections are --', subjects
    return  JsonResponse(subjects, safe=False)

def viewTeacher(request):
    logger.debug("inside viewTeacher")
    classTeacherId = request.GET.get('classTeacherId')
    logger.debug(classTeacherId)
    subject = ClassTeacher.objects.filter(class_teacher_id=classTeacherId)
    logger.debug(subject)
    subjects=[]
    for item in subject:
        grade_dict = model_to_dict(item.teacher)
        item_dict = model_to_dict(item)
        item_dict['teacher'] = grade_dict
        subjects.append(item_dict)
    logger.debug(subjects)
    print 'teachers are --', subjects
    return  JsonResponse(subjects, safe=False)

def getClassbyBatch(request):
    logger.debug("inside getClassbyBatch")
    batch_id = request.GET.get('batch_id')
    logger.debug(batch_id)
    classNames = BatchClasses.objects.filter(batch=batch_id)
    logger.debug(classNames)
    classes=[]
    for item in classNames:
        grade_dict = model_to_dict(item.grade)
        item_dict = model_to_dict(item)
        item_dict['grade'] = grade_dict
        classes.append(item_dict)
    logger.debug(classes)
    logger.debug("going back")
    return  JsonResponse(classes, safe=False)

def getBatchClassId(request):
    logger.debug("inside getSubjectByClass")
    classDropdownId = request.GET.get('classDropdownId')
    batchDropdownId = request.GET.get('batchDropdownId')
    logger.debug(classDropdownId)
    logger.debug(batchDropdownId)
    batch_class_id = BatchClasses.objects.filter(grade=classDropdownId, batch_id=batchDropdownId)
    logger.debug(batch_class_id)
    #data = serializers.serialize('json',class_subject_id )
    subjectsDict=[]
    for item in batch_class_id :
        dict=model_to_dict(item)
        subjectsDict.append(dict) 
    logger.debug(subjectsDict)
    return  JsonResponse(subjectsDict, safe=False)

def getSectionbyBatch(request):
    logger.debug("inside getSectionbyBatch")
    batch_class_id = request.GET.get('batch_class_id')
    logger.debug(batch_class_id)
    sectionNames = BatchClassSection.objects.filter(batch_class=batch_class_id)
    logger.debug(sectionNames)
    sections=[]
    for item in sectionNames:
        grade_dict = model_to_dict(item.class_sec)
        item_dict = model_to_dict(item)
        item_dict['class_sec'] = grade_dict
        sections.append(item_dict)
    logger.debug(sections)
    print 'sections are --', sections
    logger.debug("going back")
    return  JsonResponse(sections, safe=False)

def getBatchClassSectionId(request):
    logger.debug("inside getBatchClassSectionId")
    SectionDropId = request.GET.get('SectionDropId')
    batchClassID = request.GET.get('batchClassID')
    logger.debug(SectionDropId)
    logger.debug(batchClassID)
    batchClassSectionID = BatchClassSection.objects.filter(class_sec=SectionDropId, batch_class=batchClassID )
    logger.debug(batchClassSectionID)
    batchclassSecId=[]
    for item in batchClassSectionID:
        grade_dict = model_to_dict(item.class_sec)
        item_dict = model_to_dict(item)
        item_dict['class_sec'] = grade_dict
        batchclassSecId.append(item_dict)
    logger.debug(batchclassSecId)
    logger.debug("going back")
    return  JsonResponse(batchclassSecId, safe=False)

def getClassTeacherId(request):
    logger.debug("inside getClassTeacherId")
    teacherDropId = request.GET.get('teacherDropId')
    batchClassSectionID = request.GET.get('batchClassSectionID')
    logger.debug(teacherDropId)
    classTeacherId = ClassTeacher.objects.filter(teacher=teacherDropId,batch_class_sec=batchClassSectionID)
    logger.debug(classTeacherId)
    #data = serializers.serialize('json',class_subject_id )
    classTeacherDict=[]
    for item in classTeacherId :
        dict=model_to_dict(item)
        classTeacherDict.append(dict) 
    logger.debug(classTeacherDict)
    return  JsonResponse(classTeacherDict, safe=False)

@csrf_exempt
def addClassTeacherSubjects(request):
    logger.debug('start of addClassTeacherSubjects Method')
    
    value = 'empty'
    if request.is_ajax() and request.method=='POST':
        batchClassSubjectId=request.POST.get('batchClassSubjectId')
        classSubjectId=request.POST.get('classSubjectId')
        classTeacherId=request.POST.get('classTeacherId')
        batchClassID=request.POST.get('batchClassID')
        batchClassSecId=request.POST.get('batchClassSecId')
        method = request.POST.get('method')
        logger.debug(classSubjectId)
        logger.debug(classTeacherId)
        logger.debug(method)
        #count = ClassSubject.objects.filter(grade_id=class_name).count()
        #logger.debug(count)
        flag = 0
        if method=='edit':
            logger.debug("INDsas")
            s = ClassTeacherSubject.objects.get(class_teacher_sub_id=batchClassSubjectId)
            class_subject=ClassSubject.objects.get(class_subject_id=classSubjectId)
            if s.class_subject != class_subject:
                s.class_subject = class_subject
                flag = 1
            class_teacher=ClassTeacher.objects.get(class_teacher_id=classTeacherId)
            if s.class_teacher != class_teacher:
                s.class_teacher = class_teacher
                flag = 1
            batch_class=BatchClasses.objects.get(batch_class_id=batchClassID)
            if s.batch_class != batch_class:
                s.batch_class = batch_class
                flag = 1
            batch_class_sec=BatchClassSection.objects.get(batch_class_section_id=batchClassSecId)
            if s.batch_class_sec != batch_class_sec:
                s.batch_class_sec = batch_class_sec
                flag = 1
            
            
            if flag == 1:
                s.save()
            else:
                print 'No changes detected'
        
        #elif count != 0:
         #   value = 'false'
        else:
            if method=='add':
                logger.debug("InsideADD")
                class_subject=ClassSubject.objects.get(class_subject_id=classSubjectId)
                logger.debug(class_subject)
                class_teacher=ClassTeacher.objects.get(class_teacher_id=classTeacherId)
                logger.debug(class_teacher)
                batch_class=BatchClasses.objects.get(batch_class_id=batchClassID)
                batch_class_sec=BatchClassSection.objects.get(batch_class_section_id=batchClassSecId)
                school=ClassTeacherSubject.objects.create(class_subject=class_subject, class_teacher=class_teacher, batch_class=batch_class, batch_class_sec=batch_class_sec, create_user = request.user)
                school.save()
                print 'saved'   
                value = 'save'
            #elif method == 'edit':
                #s = School.objects.get(school_code=school_code)  
                #s.school_name = schoolName
                #s.save()
                #value = 'updated'
                #logger.debug('updated successfully')
    return HttpResponse(value) 

def viewClassTeacherSubject(request,ID):
    ID = request.GET.get('ID',None)
    print 'ID ', ID
    classTeacherSubjectID = ClassTeacherSubject.objects.filter(class_teacher_sub_id=ID)
    print classTeacherSubjectID
    data= serializers.serialize("json", classTeacherSubjectID)
    print data
    return HttpResponse(data)

def viewBatch(request,batchClassSubjectId):
    logger.info("start of viewBatch method")
    batchClassSubjectId = request.GET.get('batchClassSubjectId',None)
    print batchClassSubjectId
    batchClassSec = ClassTeacherSubject.objects.filter(class_teacher_sub_id=batchClassSubjectId)
    logger.debug(batchClassSec)
    batches = []
    grades = []
    for item in batchClassSec:
        batch_dict = model_to_dict(item.batch_class.batch)
        grade_dict = model_to_dict(item.batch_class.grade)
        item_dict = model_to_dict(item)
        item_dict['batch'] = batch_dict
        item_dict['grade'] = grade_dict
        batches.append(item_dict)      
        grades.append(item_dict)  
    
    print 'batches in view ', batches
    return  JsonResponse(batches, safe=False)
    #data= serializers.serialize("json", batchClassSec)
    #print data
    #return HttpResponse(data)
    
def viewClass(request):
    logger.info("start of viewClass method")
    ID = request.GET.get('ID',None)
    logger.debug(ID)
    classSubjectDetails= ClassSubject.objects.filter(class_subject_id=ID)
    logger.debug(classSubjectDetails)
    batches = []
    grades = []
    for item in classSubjectDetails:
        batch_dict = model_to_dict(item.grade)
        grade_dict = model_to_dict(item.subject)
        item_dict = model_to_dict(item)
        item_dict['grade'] = batch_dict
        item_dict['subject'] = grade_dict
        batches.append(item_dict)      
        grades.append(item_dict)
    
    print 'classSubjectDetails in view ', batches
    return  JsonResponse(batches, safe=False)
    #data= serializers.serialize("json", batchClassSec)
    #print data
    #return HttpResponse(data)
    
def viewExam(request,examTypeSyllabusID):
    logger.info("start of viewExam method")
    examTypeSyllabusID = request.GET.get('examTypeSyllabusID',None)
    logger.debug(examTypeSyllabusID)
    extsy= ExamTypeSyllabus.objects.filter(exmaType_syll_id=examTypeSyllabusID)
    logger.debug(extsy)
    batches = []
    grades = []
    for item in extsy:
        batch_dict = model_to_dict(item.exam_type)
        grade_dict = model_to_dict(item.syllabus)
        item_dict = model_to_dict(item)
        item_dict['exam_type'] = batch_dict
        item_dict['syllabus'] = grade_dict
        batches.append(item_dict)      
        grades.append(item_dict)
    
    print 'examtypeSyll in view ', batches
    return  JsonResponse(batches, safe=False)
    #data= serializers.serialize("json", batchClassSec)
    #print data
    #return HttpResponse(data)
    
def getClassSubjectIdbySyllabus(request):
    logger.info("start of getClassSubjectIdbySyllabus method")
    syllabusID = request.GET.get('syllabusID',None)
    logger.debug(syllabusID)
    sylDetails= Syllabus.objects.filter(syllabus_id=syllabusID)
    logger.debug(sylDetails)
    batches = []
    grades = []
    for item in sylDetails:
        batch_dict = model_to_dict(item.class_subject.grade)
        grade_dict = model_to_dict(item.class_subject.subject)
        item_dict = model_to_dict(item)
        item_dict['grade'] = batch_dict
        item_dict['subject'] = grade_dict
        batches.append(item_dict)      
        grades.append(item_dict)
    
    print 'sylDetails in view ', batches
    return  JsonResponse(batches, safe=False)
    #data= serializers.serialize("json", batchClassSec)
    #print data
    #return HttpResponse(data)

def listClassAttendance(request):
    logger.debug("start of listClassAttendance")
    attendance = StudentAttendanceTable(StudentAttendance.objects.all())
    return render_to_response("school/listClassAttendance.html", {'attendanceList':attendance})

def getStudentbyBatchClassSecID(request):
    logger.debug("inside getStudentbyBatchClassSecID")
    batchClass_SecId = request.GET.get('batchClass_SecId')
    logger.debug(batchClass_SecId)
    studentNames = Student.objects.filter(batch_class_sec=batchClass_SecId)
    logger.debug(studentNames)
    students=[]
    for item in studentNames:
        grade_dict = model_to_dict(item.batch_class_sec)
        item_dict = model_to_dict(item)
        item_dict['batch_class_sec'] = grade_dict
        students.append(item_dict)
        
    logger.debug(students)
    print 'students are --', students
    logger.debug("going back")
    return  JsonResponse(students, safe=False)

def getAttendanceInformation(request):
    logger.debug("inside getAttendanceInformation")
    StudentID = request.GET.getlist('StudentID[]')
    datefield = request.GET.get('datefield')
    logger.debug(StudentID)
    logger.debug(datefield)
    attendanceInformation = StudentAttendance.objects.filter(student__in=StudentID, date=datefield)
    print "attendence result",attendanceInformation
    students=[]
    attendanceList = StudentAttendanceTable(attendanceInformation)
    """"for item in attendanceInformation:
        #grade_dict = model_to_dict(item.student)
        item_dict = model_to_dict(item)
        #item_dict['student'] = grade_dict
        #students.append(item_dict)
        stable = StudentAttendanceTable(item_dict)"""
    print "tttttttttttt",attendanceList
    html = render_to_string("school/listAttendance.html", {'attendanceList':attendanceList})
    return HttpResponse(html)

def listTeacherAttendance(request):
    logger.debug("start of listTeacherAttendance")
    teacherAttend = TeacherAttendanceTable(TeacherAttendance.objects.all())
    return render_to_response("school/listTeacherAttendance.html", {'teacherList':teacherAttend})

def getTeacherAttndenceInfo(request):
    logger.debug("inside getTeacherAttndenceInfo")
    teacherId = request.GET.get('teacherId')
    datefield = request.GET.get('datefield')
    logger.debug(teacherId)
    logger.debug(datefield)
    teacherAttendanceInformation = TeacherAttendance.objects.filter(teacher=teacherId, date=datefield)
    print "attendence result",teacherAttendanceInformation
    students=[]
    teacherList = TeacherAttendanceTable(teacherAttendanceInformation)
    """"for item in attendanceInformation:
        #grade_dict = model_to_dict(item.student)
        item_dict = model_to_dict(item)
        #item_dict['student'] = grade_dict
        #students.append(item_dict)
        stable = StudentAttendanceTable(item_dict)"""
    print "tttttttttttt",teacherList
    html = render_to_string("school/listTAttendance.html", {'teacherList':teacherList})
    return HttpResponse(html)
def studentAttendance(request):
    return "success" 

def teacherAttendance(request):
    return "success"    
                