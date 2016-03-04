from django.conf.urls import patterns, include, url
from django.contrib import admin
from school import views
from student import views as stud_views
from principal import views as princ_views
from teacher import views as teacher_views
from parent import views as parent_view

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns(
                    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^getSyllabusDetails/', views.getSyllabusDetails),
    url(r'^school/', views.homePge),
    url(r'^getPrincipal/', views.getPrincipalList),
    url(r'^getClassDetails/', views.getClass),
    url(r'^getSyllabus/', views.getSyllabus),
    url(r'^getExamType/', views.getExamType),
    url(r'^getClassSubject/', views.getClassSubject),
    url(r'^getBatchClass/', views.getBatchClass),
    url(r'^getTeacher/', views.getTeacher),
    url(r'^getTeacherDetails/', views.getTeacherDetails),
    url(r'^getClassTimetableDetails/', views.getClassTimeDetails),
    url(r'^getBatchClassTeacher/', views.getBatchClassTeacher),
    url(r'^listSchool/', views.schoolList),
	
    # for class Subject #
    url(r'^listClassSubject/', views.classSubject),
    url(r'^getClass/', views.getClassList),
    url(r'^viewClass/', views.viewClass),
    url(r'^getSubject/', views.getSubjectList),
    url(r'^addClassSub/', views.addClassSub, name="classSub"),
    url(r'^delClassSubject/(?:ID=(?P<ID>\d+)/)?$', views.delClassSubject),
    url(r'^viewClassSubject/(?:ID=(?P<ID>\d+)/)?$', views.viewClassSubject),
    #End Class Subject #
	  
    # For Syllabus Module #
    url(r'^listSyllabus', views.syllabusList),
    url(r'^addSyllabusTopic/', views.addSyllabusTopic, name="addSyllabusTopic"),
    url(r'^delSyllabus/(?:syllabusId=(?P<syllabusId>\d+)/)?$', views.delSyllabus),
    url(r'^viewSyllabus/(?:syllabusId=(?P<syllabusId>\d+)/)?$', views.viewSyllabus),
    # End of Syllabus Module#
    url(r'^viewClassSection/(?:classSectionId=(?P<classSectionId>\d+)/)?$', views.getClassSectionDetails),
    url(r'^viewExamAssign/(?:examAssignCode=(?P<examAssignCode>\d+)/)?$', views.getExamAssign), 
    url(r'^viewClassTimetable/(?:classTimetableCode=(?P<classTimetableCode>\d+)/)?$', views.getClassTimetableDetails),
    url(r'^viewTeacherTimetable/(?:teacherTimetableCode=(?P<teacherTimetableCode>\d+)/)?$', views.getTeacherTimetableDetails),  
    url(r'^listClassTimetable/', views.listClassTimetable),
    url(r'^listClassTimetable1/', views.listClassTimetable1),
    url(r'^listTeacherTimetable/', views.listTeacherTimetable),
    url(r'^listTeacherTimetable1/', views.listTeacherTimetable1),
    url(r'^listClassSection/', views.listClassSection),
    # for Exam Type Syllabus #
    url(r'^examTypeSyllabusList/', views.ExamTypeSyll),
    url(r'^getSubjectByClass/', views.getSubjectByClass),
    url(r'^getClassSubjectId/', views.getClassSubjectId),
    url(r'^getExamTypeList/', views.getExamTypeList),
    url(r'^getClassSubjectIdbySyllabus/', views.getClassSubjectIdbySyllabus),
    url(r'^viewExam/(?:examTypeSyllabusID=(?P<examTypeSyllabusID>\d+)/)?$', views.viewExam),
    url(r'^addExamTypeSyllabus/', views.addExamTypeSyllabus, name="examTypeSyllabus"),
    url(r'^viewExamTypeSyllabus/(?:examTypeSyllabusID=(?P<examTypeSyllabusID>\d+)/)?$', views.getSylDetails),
    url(r'^delExamSyllabus/(?:examTypeSyllabusID=(?P<examTypeSyllabusID>\d+)/)?$', views.delExamSyllabus),
    # End of Exam Type Syllabus #
    #For Class Teacher Subject module#
    url(r'^classTeacherSubjectList/', views.classTeacherSubjectList),
    url(r'^getBatch/', views.getBatches),
    url(r'^viewSubject/', views.viewSubject),
    url(r'^viewSection/', views.viewSection),
    url(r'^viewTeacher/', views.viewTeacher),
    url(r'^getClassbyBatch/', views.getClassbyBatch),
    url(r'^getBatchClassId/', views.getBatchClassId),
    url(r'^getSectionbyBatch/', views.getSectionbyBatch),
    url(r'^getBatchClassSectionId/', views.getBatchClassSectionId),
    url(r'^getClassTeacherId/', views.getClassTeacherId),
    url(r'^addClassTeacherSubjects/', views.addClassTeacherSubjects, name="addClassTeacherSubjects"),
    url(r'^viewClassTeacherSubject/(?:ID=(?P<ID>\d+)/)?$', views.viewClassTeacherSubject),
    url(r'^viewBatch/(?:batchClassSubjectId=(?P<batchClassSubjectId>\d+)/)?$', views.viewBatch),
    #End of exam Teacher Subject Module #
    url(r'^addSchool/', views.addSchool,name="school"),
    url(r'^delSchool/(?:schoolCode=(?P<schoolCode>\d+)/)?$', views.delSchool),
    url(r'^viewSchool/(?:schoolCode=(?P<schoolCode>\d+)/)?$', views.getSchoolDetails), 
    #url(r'^listStudents/', student_views.studentList),

    url(r'^listStudents/', stud_views.studentList),
    url(r'^addStudent/', stud_views.addStudentDetails, name="student"),
    #url(r'^listSchools/', views.school_List),
    #url(r'^listStudents/', stud_views.studentList),
    #url(r'^addStudent/', stud_views.addStudentDetails, name="student"),
   
    url(r'^listSections/', views.sectionList),
    url(r'^addSection/', views.addSection),
    url(r'^delSection/(?:sectionId=(?P<sectionId>\d+)/)?$', views.delSection),
    url(r'^listBatches/', views.batchList),
    url(r'^listSubjects/', views.subjectList),
    url(r'^listClasses/', views.classList),
    url(r'^listExam/', views.examList),
    url(r'^listSyllabus', views.syllabusList),
    url(r'^addBatch/', views.addBatch,name="batch"),
    url(r'^addSubject/', views.addSubject,name="subject"),
    url(r'^addClass/', views.addClass,name="class"),
    url(r'^addClassSection/', views.addClassSection,name="classSection"),
    url(r'^addExam/', views.addExam,name="exam"),
    url(r'^assignExams/', views.assignExams,name="assignExams"),
    url(r'^classTimetable/', views.classTimetable,name="classTimetable"),
    url(r'^teacherTimetable/', views.teacherTimetable,name="teacherTimetable"),
    url(r'^addSyllabus/', views.addSyllabus,name="syllabus"),
    url(r'^delBatch/(?:batchId=(?P<batchId>\d+)/)?$', views.delBatch),
    url(r'^listTeacher/', views.teacherList),
    url(r'^addTeacher/', views.addTeacher),
    url(r'^delTeacher/(?:teacherId=(?P<teacherId>\d+)/)?$', views.delTeacher),
    url(r'^delSubject/(?:subjectId=(?P<subjectId>\d+)/)?$', views.delSubject),
    url(r'^delClass/(?:classId=(?P<classId>\d+)/)?$', views.delClass),
    url(r'^delClassSection/(?:classSectionId=(?P<classSectionId>\d+)/)?$', views.delClassSection),
    url(r'^delExam/(?:examId=(?P<examId>\d+)/)?$', views.delExam),
    url(r'^delClassTimetable/(?:classTimetableCode=(?P<classTimetableCode>\d+)/)?$', views.delClassTimetable),
    url(r'^delTeacherTimetable/(?:teacherTimetableCode=(?P<teacherTimetableCode>\d+)/)?$', views.delTeacherTimetable),
    #url(r'^getclassesBySelectedBatch/(?:batchId=(?P<batchId>\d+)/)?$',stud_views.getclassesBySelectedBatch),
    url(r'^listBatchClasses/', views.listBatchClasses),
    url(r'^getBatchClassOptions/', views.getBatchClassOptions),
    url(r'^addBatchClass/', views.addBatchClass),
    url(r'^delBatchClass/(?:batchClassId=(?P<batchClassId>\d+)/)?$', views.delBatchClass),
    url(r'^viewBatchClass/(?:batchClassId=(?P<batchClassId>\d+)/)?$', views.viewBatchClass),

    url(r'^listBatchClassSection/', views.listBatchClassSec),
    url(r'^getBatchClassSecOptions/', views.getBatchClassSecOptions),
    url(r'^addBatchClassSec/', views.addBatchClassSec),
    url(r'^delBatchClassSec/(?:batchClassSecId=(?P<batchClassSecId>\d+)/)?$', views.delBatchClassSec),
    url(r'^viewBatchClassSec/(?:batchClassSecId=(?P<batchClassSecId>\d+)/)?$', views.viewBatchClassSec),
    url(r'^getClassByBatch/(?:batchId=(?P<batchId>\d+)/)?$', views.getclassesBySelectedBatch),
    url(r'^listExamAssign/', views.examAssignList),
    url(r'^getclassesBySelectedBatch/$',stud_views.getclassesBySelectedBatch),
    url(r'^viewStudent/(?:studentId=(?P<studentId>\d+)/)?$',stud_views.viewStudent),
    url(r'^deleteStudent/(?:studentId=(?P<studentId>\d+)/)?$', stud_views.deleteStudent),
    url(r'^getsectionBySelectedClass/(?:batchclassId=(?P<batchclassId>\d+)/)?$',stud_views.getsectionBySelectedClass),
    # student Results url
    url(r'^examResultSearchList/$',stud_views.examResultSearchList, name="examResult"),
    url(r'^getStudentResults/$',stud_views.getStudentResults),
    url(r'^viewStudentReult/$',stud_views.viewStudentReult),
    
    url(r'^delExamAssign/(?:examAssignId=(?P<examAssignId>\d+)/)?$', views.delExamAssign),
    url(r'^viewExamAssign/(?:examAssignCode=(?P<examAssignCode>\d+)/)?$', views.getExamAssign), 
    url(r'^delExamAssign/(?:examAssignId=(?P<examAssignId>\d+)/)?$', views.delExamAssign),
    url(r'^classTeacherList/', views.listClassTeacher),
    url(r'^delClassTeacher/(?:ID=(?P<ID>\d+)/)?$', views.delClassTeacher),
    url(r'^addClassTeacher/', views.addClassTeacher,name="classTeacher"),
    url(r'^getSecAccBatchClass/', views.getSecAccBatchClass),
    url(r'^viewClassTeacher/(?:classTeacherId=(?P<classTeacherId>\d+)/)?$', views.getClassTeacherDetails),
    
    #Student Assignment
    url(r'^listAssignments/$',stud_views.assignmentsList),
    url(r'^getSubjectSyllabusDetails/$',stud_views.getSubjectSyllabusDetails),
    url(r'^addUpdateAssignment/$',stud_views.addUpdateAssignment, name="assignment"),
    url(r'^viewAssignment/$',stud_views.viewAssignment),
    url(r'^deleteAssignment/$',stud_views.deleteAssignment),
    
    #StudentRanking List
    url(r'^listStudentRanking/$',stud_views.StudentRankingList),
    url(r'^getStudentRankingByClassExam/$',stud_views.getStudentRankingByClassExam),
     #For Class Attendance#
    url(r'^listClassAttendance/', views.listClassAttendance),
    url(r'^getStudentbyBatchClassSecID/', views.getStudentbyBatchClassSecID),
    url(r'^getAttendanceInformation/', views.getAttendanceInformation, name="getAttendanceInformation"),
    #Class Attendance Ends Here#
    #For Teacher Attendance#
    url(r'^listTeacherAttendance/', views.listTeacherAttendance),
    url(r'^getTeacherAttndenceInfo/', views.getTeacherAttndenceInfo, name="getTeacherAttndenceInfo"),
    #Teacher Attendance Ends Here#
    url(r'^studentAttendance/', views.studentAttendance),
    url(r'^teacherAttendance/', views.teacherAttendance),
     #For Teacher Module#
    url(r'^teacher/', teacher_views.teacherHomePage),
    #For View Syllabus#
    url(r'^viewSyllabusTeacherModule/', teacher_views.viewSyllabusTeacherModule),
    url(r'^getBatchClassSecIdbyTeacher/', teacher_views.getBatchClassSecIdbyTeacher),
    url(r'^getClassbyBacthClassId/', teacher_views.getClassbyBacthClassId),
    url(r'^getSyllabusData/', teacher_views.getSyllabusData, name="getSyllabusData"),
    #End of View Syllabus#
    #For View Results#
    url(r'^viewResultTeacherModule/', teacher_views.viewResultTeacherModule),
    url(r'^getResult/', teacher_views.getResult),
    #End of View Results#
    #For Exam Schedule#
    url(r'^viewExamScheduleTeacherModule/', teacher_views.viewExamScheduleTeacherModule),
    url(r'^getSyllabusId/', teacher_views.getSyllabusId),
    url(r'^getExamTypeSyllabusId/', teacher_views.getExamTypeSyllabusId),
    url(r'^getExamScheduleInfo/', teacher_views.getExamScheduleInfo),
    #End of Exam Schedule#
    #For View Profile#
    url(r'^viewProfileTeacherModule/', teacher_views.viewProfileTeacherModule),
    url(r'^getTeacherInformation/', teacher_views.getTeacherInformation),
    url(r'^updateTeacherDetails/', teacher_views.updateTeacherDetails),
    #End of View Profile#
    #For View Attendance#
    url(r'^viewAttendanceTeacherModule/', teacher_views.viewAttendanceTeacherModule),
    url(r'^getBatchClassIdbyClass/', teacher_views.getBatchClassIdbyClass),
    url(r'^getSections/', teacher_views.getSections),
    url(r'^getBatchClassSectionIds/', teacher_views.getBatchClassSectionIds),
    url(r'^getStudentId/', teacher_views.getStudentId),
    #End of View Attendance#
    #For View TimeTable#
    url(r'^viewTimeTableTeacherModule/', teacher_views.viewTimeTableTeacherModule),
    #End of View TimeTable#
    #Teacher Module Ends Here#

    
    #principal module
    url(r'^principal/', princ_views.principalHomePge),
    url(r'^listExamSchedule/', princ_views.listExamSchedule),
    url(r'^getExamScheduleDetails/', princ_views.getExamScheduleDetails),
    url(r'^classResultSearchList/', princ_views.classResultSearchList),
    url(r'^viewClassResult/', princ_views.viewClassResult),
	url(r'^populateTeacher/', views.populateTeacher),
	#Student Portal
    url(r'^student/$',parent_view.studentHome),
    url(r'^viewStudSyllabus/', parent_view.viewSyllabus),
    url(r'^getStudSyllabus/', parent_view.getSyllabus, name="getStudSyllabus"),
    url(r'^viewExamSchedule/', parent_view.viewExamSchedule),
    url(r'^getStudExamSchedule/',parent_view.getExamSchedule),
    url(r'^viewHomework/',parent_view.viewHomework),
    url(r'^getStudHomework/',parent_view.getHomework),
    url(r'^viewTimeTable/',parent_view.viewTimeTable),
    url(r'^viewAttendance/',parent_view.viewAttendance),
    url(r'^getStudAttendance/',parent_view.getStudAttendance),
    url(r'^viewResult/',parent_view.viewResult),
    url(r'^getStudResult/',parent_view.getStudResult),
    url(r'^viewStudProfile/', parent_view.viewStudProfile),
    url(r'^getStudProfile/', parent_view.getStudProfile),
    url(r'^updateStudDetails/', parent_view.updateStudDetails),
	
	
)
urlpatterns += staticfiles_urlpatterns()
