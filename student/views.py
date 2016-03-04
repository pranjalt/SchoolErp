import os

from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.template import Context
from SchoolERP.models import Sections, School,Class,BatchClasses,Student,Parent,StudentAddress,ParentStudent,ClassSection,BatchClassSection,ExamResult,Batch,ExamTypeSyllabus,ExamAssign,Assignment,Syllabus,ClassSubject,PreviousInstituteDetails,Ranking
from student.serializers import BatchClassesSerializers
from school.tables import SectionTable
import logging
from datetime import date
from student.forms import studentForm,parentForm,studentTempAddressForm,studentPermanantAddressForm,SectionsForm,classForm,batchForm,examResultForm,examTypeForm,subjectForm,assignmentForm,SyllabusForm,clsForm,PInstituAddressForm,previousIntituteDetailsForm
from django.views.decorators.csrf import  requires_csrf_token
from student.tables import StudentTable,StudentResultTable,studReportCardTab,assignmentTable,StudentRankingTable
from django.core import serializers
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.forms import formset_factory
from django.forms.models import inlineformset_factory
from django.db.transaction import commit
from django.db import transaction
from django.template.loader import get_template, LoaderOrigin
from django.forms.models import model_to_dict
from django.core.context_processors import csrf
from __builtin__ import setattr
from django.template import loader
logger = logging.getLogger(__name__)
from django.template.loader import render_to_string
from django.db.models import Avg,F, Sum

def homePge(request):
    #form = RegistrationForm()
    logger.debug("this is a debug message!")
    return render_to_response("base.html", RequestContext(request,{}))
    
def schoolList(request):
    #form = RegistrationForm()
    logger.debug("this is a debug message!")
    return render_to_response("school/schoolList.html", RequestContext(request,{}))

def sectionList(request):
    logger.debug("start of sectionList")
    sectionList = Sections.objects.all()
    section = SectionTable(Sections.objects.all())
    return render_to_response("school/sectionList.html", {'sectionList':section,'section':sectionList})

def add_school(request):
    return "success"

@requires_csrf_token
def addSection(request):
    logger.debug("start of add Section")
    try:
        if request.method == 'POST':
           sectionName = request.POST.get('sectionName');
           print sectionName
           createDate = date;
           section=Sections.objects.create(section = sectionName,create_data=createDate)
           section.save()
           return render_to_response('school/sectionList.html',RequestContext(request))        
        else :
           return render_to_response(RequestContext(request),'school/sectionList.html',{
            'error_message': "Something went wrong.Kindly try after sometime",
        })   
    except (Exception):
        return render_to_response(RequestContext(request),'school/sectionList.html',{
            'error_message': "Something went wrong.Kindly try after sometime",
        })
def studentList(request):
    logger.debug("start of studentList function")
    form=studentForm()
    student= StudentTable()
    parForm=parentForm()
    PermAddrForm=studentPermanantAddressForm()
    tempAddrForm=studentTempAddressForm()
    bform=batchForm()
    clsform=classForm()
    secForm=SectionsForm() 
    pIntituteDetailsForm=previousIntituteDetailsForm()
    pInstituteAddrFrom=PInstituAddressForm()
    print"===================="
    return render(request,"student/studentList.html", {'student':student,'form':form,"parForm":parForm,'PermAddrForm':PermAddrForm,'tempAddrForm':tempAddrForm,'batchForm':bform,'classForm':clsform,'secForm':secForm,'pIntituteDetailsForm':pIntituteDetailsForm,'pInstituteAddrFrom':pInstituteAddrFrom})

def handle_uploaded_file(f,file_name):
    with open(file_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@transaction.atomic
def addStudentDetails(request):
    
    media_root = 'D://studentImages/student'
    logger.debug("start of addStudentDetails method :")
    print "in student add form"
    if request.POST:
       
        action_type= request.POST['action_type']
        PermAddrForm=studentPermanantAddressForm(request.POST)
        tempAddrForm=studentTempAddressForm(request.POST)
        pIntituteAddrForm=PInstituAddressForm(request.POST)
        pIntituteAddrForm.errors
        PermAddrForm.errors
        tempAddrForm.errors
        
        addr_fields = ['flatNo', 'street1', 'street2','city','pincode', 'state' ]
        
        if action_type == "add":
            form=studentForm(request.POST,request.FILES)
            print "in student add form form :",form
            parForm=parentForm(request.POST)
            
            pInstituteForm=previousIntituteDetailsForm(request.POST)
            
        else:
            student_id = request.POST['student_id']
            parent_id = request.POST['parent_id']
            
            student = Student.objects.get(student_id=student_id)
            parent = Parent.objects.get(parent_id=parent_id)
        
            form=studentForm(request.POST,request.FILES,instance=student)
            parForm=parentForm(request.POST, instance=parent)
            
            prev_institute_id =request.POST['previous_institute_id']
            if prev_institute_id is None  :
                pInstituteForm = previousIntituteDetailsForm(request.POST)
            else:   
                prev_institute_obj = PreviousInstituteDetails.objects.get(previous_institute_id=prev_institute_id)
                pInstituteForm = previousIntituteDetailsForm(request.POST,instance=prev_institute_obj)
           
        print "student form error :",form.errors
        print "Is student valid :",form.is_valid()
        print "Parent Form Error :",parForm.is_valid()
        print "Is Parent Form Valid :",parForm.errors
        print "Previous Institute Form error :",pInstituteForm.errors
        print "previous institute form valid :",pInstituteForm.is_valid()
        
        if form.is_valid() and parForm.is_valid() and pInstituteForm.is_valid():
             
            print "in if condition validate form and parent form"
            pInstitute = pInstituteForm.save()            
            student=form.save(commit=False)
            student.previous_institute = pInstitute
            student.save()
            
            if action_type == "add":
                student_id = student.student_id
                name = request.FILES['student_image_file'].name
                ext = name.split('.')[-1]
                print "ext ::::::: ",ext
                file_path = media_root + os.sep + "student_image_%s" % student_id + '.' + ext
                handle_uploaded_file(request.FILES['student_image_file'], file_path)
                print file_path
                student.student_pic = 'static/student/' + "student_image_%s.%s" % (student_id, ext)
                student.save()
            
            parent=parForm.save()            
            
            if action_type == "add":
                studParent= ParentStudent.objects.create(parent=parent,student=student)
                studParent.save()
            
            if PermAddrForm.is_valid() and tempAddrForm.is_valid() and pIntituteAddrForm.is_valid():
                print "in if condition validte form and address form"
                if action_type == "add":
                    model_dict = {}
                    for field in addr_fields:
                        model_dict[field] = PermAddrForm.cleaned_data[field]
                    p_address = StudentAddress(**model_dict)
                    p_address.type= 'permenant'
                    p_address.student = student
                    p_address.save() 
    
                    for field in addr_fields:
                        model_dict[field] = tempAddrForm.cleaned_data['temp'+field]
                    t_address = StudentAddress(**model_dict)
                    t_address.type= 'temporary'
                    t_address.student = student
                    t_address.save()
                    
                    for field in addr_fields:
                        print "in addr_fields if condition :"
                        model_dict[field] = pIntituteAddrForm.cleaned_data['pInstitute'+field]
                    prev_institute_addr = StudentAddress(**model_dict)
                    prev_institute_addr.type= 'PreviousInstituteAddr'
                    prev_institute_addr.student = student
                    prev_institute_addr.save()
                        
                else:
                    p_address = StudentAddress.objects.get(student=student, type="permenant")
                    t_address = StudentAddress.objects.get(student=student, type="temporary")
                   
                    prev_institute_addr = StudentAddress.objects.get(student=student, type="PreviousInstituteAddr")
                    print " in else cndtn edit 2222222",prev_institute_addr
                        
                    #if prev institute is not given,and entered at on edit then it fails to add all 3 address    
                    for field in addr_fields:
                        setattr(p_address, field, PermAddrForm.cleaned_data[field])
                        setattr(t_address, field, tempAddrForm.cleaned_data['temp' + field])
                        setattr(prev_institute_addr,field, pIntituteAddrForm.cleaned_data['pInstitute' + field])
                        
                    p_address.save()
                    t_address.save() 
                    prev_institute_addr.save()            
        else:
            print "form errors :"
            print form.errors
            print parForm.errors
            print pInstituteForm.errors
    Studform=studentForm()
    studentTable= StudentTable()
    parForm=parentForm()
    template= get_template('student/studentList.html')
    PermAddrForm=studentPermanantAddressForm()
    tempAddrForm=studentTempAddressForm()
    pIntituteDetailsForm=previousIntituteDetailsForm()
    pInstituteAddrFrom=PInstituAddressForm()
    
    variables = Context({
                        'student':studentTable,
                        'form':Studform,
                        'parForm':parForm,
                        'PermAddrForm':PermAddrForm,
                        'tempAddrForm':tempAddrForm,
                        'pIntituteDetailsForm':pIntituteDetailsForm,
                        'pInstituteAddrFrom':pInstituteAddrFrom
                         })   
    output = template.render(variables)
    #return HttpResponse(output)
    return redirect('/school/?default_load_tab=Students')
    
def getclassesBySelectedBatch(request):
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
    
    
def getsectionBySelectedClass(request ,batchclassId):
    logger.debug("start of getsectionBySelectedClass method :")
    batchclassId =request.GET.get('batchclassId')
    ClsSection= BatchClassSection.objects.filter(batch_class = batchclassId)

    sections=[]
    for item in ClsSection: 
        section_dict = model_to_dict(item.class_sec)
        item_dict = model_to_dict(item)
        item_dict['section_info'] = section_dict
        sections.append(item_dict)  
    print sections    
    return  JsonResponse(sections, safe=False)
    


def viewStudent(request,studentId):
    studentId =request.GET.get('studentId')
    
    parent_student = ParentStudent.objects.get(student=studentId)
    
        
    t_student_addr=StudentAddress.objects.get(student=studentId,type='temporary')
    p_student_addr=StudentAddress.objects.get(student=studentId,type='permenant')
    try :
        prev_institute=StudentAddress.objects.get(student=studentId,type='PreviousInstituteAddr')
    except StudentAddress.DoesNotExist :
        prev_institute =None 
        
    if prev_institute is not None  :
        modelDict={'student':model_to_dict(parent_student.student),
                    'parent':model_to_dict(parent_student.parent),
                    'tAddr':model_to_dict(t_student_addr),
                    'pAddr':model_to_dict(p_student_addr),
                    'batch':model_to_dict(parent_student.student.batch_class_sec.batch_class.batch),
                    'classVal':model_to_dict(parent_student.student.batch_class_sec.batch_class.grade),
                    'section':model_to_dict(parent_student.student.batch_class_sec.class_sec),
                    'pIntituteDetails':model_to_dict(parent_student.student.previous_institute),
                    'pInstituteAddr':model_to_dict(prev_institute)}
    else :
        modelDict={'student':model_to_dict(parent_student.student),
                    'parent':model_to_dict(parent_student.parent),
                    'tAddr':model_to_dict(t_student_addr),
                    'pAddr':model_to_dict(p_student_addr),
                    'batch':model_to_dict(parent_student.student.batch_class_sec.batch_class.batch),
                    'classVal':model_to_dict(parent_student.student.batch_class_sec.batch_class.grade),
                    'section':model_to_dict(parent_student.student.batch_class_sec.class_sec)}
        
    return  JsonResponse(modelDict)


def deleteStudent(request,studentId):
    logger.info("start of delete student method")
    try:
        studentId = request.GET.get('studentId',None)
        if studentId is None:
            logger.exception('schoolCode = '+studentId)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('studentId = '+studentId)
            ParentStudent.objects.filter(student=studentId).delete()
            StudentAddress.objects.filter(student=studentId).delete()
            Student.objects.filter(student_id=studentId).delete()
    except Student.DoesNotExist:
        logger.exeption('student Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delete Student method")
    return HttpResponse("success")
    
def examResultSearchList(request) :
    logger.info("start of examResultSearchList method")
    studResultForm=examResultForm
    bform=batchForm()
    clsform=classForm()
    secForm=SectionsForm() 
    examTypeFrm=examTypeForm()
    logger.debug("ajax call")
    studResults = ExamResult.objects.all()   
    logger.info("start of exam Result SearchList method")   
    studResultTable = StudentResultTable(studResults)
    logger.info("end of examResultSearchList method")
    
    return render_to_response("student/studentResult.html", 
                  {'studResultTable':studResultTable,
                   'studResultForm':studResultForm,
                   'bform':bform,'clsform':clsform,
                   'secForm':secForm,'examTypeFrm':examTypeFrm})
    

def getStudentResults(request):
    logger.info("start of getStudentResults method")
    bcsId = request.GET.get('bcsId',None)
    examTypeId =request.GET.get('examTypeId',None)
    if bcsId !=None and examTypeId!=None:
        classSubSyllabus= ExamTypeSyllabus.objects.filter(exam_type=examTypeId)
        studResults=ExamResult.objects.filter(student__in= Student.objects.filter(batch_class_sec=bcsId),exam_assign__in=ExamAssign.objects.filter(class_sub_syll__in=classSubSyllabus))    
    studResultForm=examResultForm
    bform=batchForm()
    clsform=classForm()
    secForm=SectionsForm() 
    examTypeFrm=examTypeForm()
    st = []
    ids = set()
    for rec in studResults:        
        if rec.student in ids:
            continue
        else:
            ids.add(rec.student)            
        st.append(rec)   
    studResultTable = StudentResultTable(st)
        
    html = render_to_string("student/studentResultPart.html", {'studResultTable':studResultTable,})
    logger.info("end of getStudentResults method")
    return HttpResponse(html)

def viewStudentReult(request):
    logger.info("start of viewStudentReult method")
    studentId = request.GET.get('studentId',None)
    examTypeId=request.GET.get('examTypeId',None)
    classSubSyllabus= ExamTypeSyllabus.objects.filter(exam_type=examTypeId)
    studExamResult=ExamResult.objects.filter(student=studentId, exam_assign__in=ExamAssign.objects.filter(class_sub_syll__in=classSubSyllabus))
    modelDict =[]
    for item in studExamResult :
        subjectModel=model_to_dict(item.exam_assign.class_sub_syll.syllabus.class_subject.subject)
        studDetails = model_to_dict(item.student)
        studResult= model_to_dict(item)
        studResult['studDetails'] =studDetails
        studResult['subjectDetails'] =subjectModel
        modelDict.append(studResult)
    
    logger.info("end of viewStudentReult method")
    return JsonResponse(modelDict,safe=False)
    
def assignmentsList(request):
    logger.info("start of assignmentsList method")
    assignment= Assignment.objects.all()
    assignmentTableData = assignmentTable(assignment)
    subForm=subjectForm()
    assgmntForm =assignmentForm()
    SyllForm=SyllabusForm()
    clsform=clsForm()
    return render(request,"student/Assignments.html", {'assignmentTable':assignmentTableData,'subForm':subForm,'assgmntForm':assgmntForm,'SyllForm':SyllForm,'clsform':clsform})

def getSubjectSyllabusDetails(request):
    logger.info("start of getSubjectSyllabusDetails method")
    classId =request.GET.get('classId',None) 
    syllabusDetails =Syllabus.objects.filter(class_subject__in=ClassSubject.objects.filter(grade=classId))
    
    modelDict =[]
    for obj in syllabusDetails:
        subj=model_to_dict(obj.class_subject.subject)
        syllabus = model_to_dict(obj)
        syllabus['subject']=subj
        modelDict.append(syllabus)
    print modelDict
    logger.info("end of getSubjectSyllabusDetails method")
    return JsonResponse(modelDict, safe=False)
    

def addUpdateAssignment(request):
    logger.info("start of addUpdateAssignment method")
  
    if request.POST:
            action_type= request.POST['action_type'] 
            if action_type=="add" :
                assgmntForm=assignmentForm(request.POST)
                print "errors :::: %s" % assgmntForm.errors
                print "valid ::: %s" % assgmntForm.is_valid 
                
            else :
                assignment_id = request.POST['assignment_id']
                assigmnt = Assignment.objects.get(assignment_id=assignment_id)
                assgmntForm=assignmentForm(request.POST, instance=assigmnt)
                
            if assgmntForm.is_valid :
                assgmntForm.save()
                print "save"
                   
    return  HttpResponse("success")  

def viewAssignment(request):
    print "in viewAssignmentFunction"
    assignmentId = request.GET.get('assignmentId',None)
    print "assignment Id",assignmentId
    assignmentDetails=Assignment.objects.get(assignment_id=assignmentId)
    modelDict={'assignment':model_to_dict(assignmentDetails),
               'syllabus':model_to_dict(assignmentDetails.syllabus),
               'classVal':model_to_dict(assignmentDetails.syllabus.class_subject.grade),
               'subject':model_to_dict(assignmentDetails.syllabus.class_subject.subject)
               }
    return JsonResponse(modelDict, safe=False)

def deleteAssignment(request):
    logger.info("start of delete Assignment method")
    try:
        assignmentId = request.GET.get('assignmentId',None)
        if assignmentId is None:
            logger.exception('Assignment Id = '+assignmentId)
            return render_to_response("exception.html", RequestContext(request,{}))
        else:
            logger.debug('assignmentId = '+assignmentId)
            Assignment.objects.filter(assignment_id=assignmentId).delete()
    except Assignment.DoesNotExist:
        logger.exeption('Assignment Object does not exists')
        return render_to_response("exception.html", RequestContext(request,{}))
    except Exception:
        logger.exception('Main Exception')
        return render_to_response("exception.html", RequestContext(request,{}))         
    logger.info("end of delete Assignment method")
    return HttpResponse("success")




def StudentRankingList(request):
    logger.info("start of Student Ranking List method")
    bform=batchForm()
    clsform=classForm()
    secForm=SectionsForm() 
    examTypeFrm=examTypeForm()
    logger.debug("ajax call")
    studRanking = Ranking.objects.all()   
    logger.info("Student Ranking List method")   
    studRankingTable = StudentRankingTable(studRanking)
    logger.info("Student Ranking List method")
    
    return render_to_response("student/studentRanking.html", 
                  {'studRankingTable':studRankingTable,
                   'bform':bform,'clsform':clsform,
                   'secForm':secForm,'examTypeFrm':examTypeFrm})
    

def getStudentRankingByClassExam(request):
    bcsId = request.GET.get('bcsId',None)
    examTypeId =request.GET.get('examTypeId',None)
    if bcsId !=None and examTypeId!=None:
        print " exam type =======",examTypeId
        studRanking=Ranking.objects.filter(student__in= Student.objects.filter(batch_class_sec=bcsId),exam_type=examTypeId).order_by('ranking')  
    studRankingTable = StudentRankingTable(studRanking)
        
    html = render_to_string("student/studentRankingPart.html", {'studRankingTable':studRankingTable,})
    logger.info("end of getStudentResults method")
    return HttpResponse(html)
    