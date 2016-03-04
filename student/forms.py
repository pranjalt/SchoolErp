'''
Created on 13-Jan-2016

@author: Administrator
'''
from SchoolERP.models import Student,BatchClassSection,Class,Parent,ParentStudent,StudentAddress,City,State,Batch,BatchClasses,Sections,StudentAddress,ClassSection,ExamResult,ExamType,Assignment,Subject,Syllabus,PreviousInstituteDetails
from django import forms
from django.forms.models import inlineformset_factory


class parentForm(forms.ModelForm):
    fatherName = forms.CharField(label="father_name",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','required':'true','data-fv-notempty-message':'The father name is required and cannot be empty','placeholder':'Father Name'}))
    motherName = forms.CharField(label="mother_name",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Mother Name'}))
    guardianName = forms.CharField(label="guardian name",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','required':'true','placeholder':'Guardian Name'}))
    fatherContactNo = forms.IntegerField(label="father contact no",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','maxlength':'10','date-error':'not valid contact number','placeholder':'10 digits'}))
    motherContactNo = forms.IntegerField(label="mother contact no",widget=forms.TextInput(attrs={'class':'form-control col-sm-3 bfh-phone','maxlength':'10','date-error':'not valid contact number','placeholder':'10 digits'}))
    guardianContactNo = forms.IntegerField(label="guardian contact no",widget=forms.TextInput(attrs={'class':'form-control col-sm-3 bfh-phone','maxlength':'10','date-error':'not valid contact number','placeholder':'10 digits'}))
    fatherEmailAddr = forms.CharField(label="father_email",widget=forms.EmailInput(attrs={'class':'form-control col-sm-3','type':'email','data-error':'email address is invalid','placeholder':'test@gmail.com'}))
    motherEmailAddr = forms.CharField(label="Mother_email",widget=forms.EmailInput(attrs={'class':'form-control col-sm-3','type':'email','data-error':'email address is invalid','placeholder':'test@gmail.com'}))
    guardianEmailAddr = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control col-sm-3','type':'email','data-error':'email address is invalid','placeholder':'test@gmail.com'}))
    
    class Meta:
        model = Parent
        fields = ('fatherName', 'motherName', 'guardianName', 'fatherContactNo', 'motherContactNo','guardianContactNo','fatherEmailAddr','motherEmailAddr','guardianEmailAddr')

CLASS_EMPTY = [('','')] 

class studentForm(forms.ModelForm):
    
    #username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3'}))
    firstName = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'First Name'}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={'class':'col-sm-3 form-control','placeholder':'Last Name'}))
    dateOfBirth = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control col-sm-3 date','placeholder':'dd-mm-yyyy', 'type':'date','data-fv-date':'true','data-fv-date-message':'The value is not a valid date'}))
    gender = forms.ChoiceField(choices=((None, ''), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')),widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    
    batch_class_sec = forms.ModelChoiceField(queryset=BatchClassSection.objects.all(), label="academy details",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','id':'bcsId','value':'','type':'hidden'}))
    contactNo = forms.IntegerField(label="Conatct Number",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','maxlength':'12' ,'required':'required','date-error':'not valid contact number','placeholder':'Contact Number'}))
    aadhaarNo = forms.CharField(label="AAdhar Number",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','type':'number','maxlength':'15','date-error':'Aadhar card number is not valid'}))
    admissionNo = forms.CharField(label="Adminssion Number",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Aadhar Number'}))
    dateOfAdmission = forms.DateField(label="Date Of Addmission",widget=forms.DateInput(attrs={'class':'form-control col-sm-3 date','placeholder':'dd-mm-yyyy', 'type':'date','data-fv-date':'true','data-fv-date-message':'The value is not a valid date'}))
    category = forms.CharField(label="Category",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Cotegory'}))
    motherTongue = forms.CharField(label="mother_tongue",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Mother Tongue'}))
    #student_pic =forms.FileField(required=False,)
    #previous_institute = forms.ModelChoiceField(queryset=PreviousInstituteDetails.objects.all(),widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Mother Tongue'}))
    
    def __init__(self, *args, **kwargs):
        super(studentForm, self).__init__(*args, **kwargs)
        #self.fields['firstName'].required = True
        fields = ['firstName', 'lastName', 'dateOfBirth']
        for field in fields:
            self.fields[field].required = False

    class Meta: 
        model = Student
        fields = ('firstName','lastName','dateOfBirth','gender','batch_class_sec','contactNo','aadhaarNo','admissionNo','dateOfAdmission','category','motherTongue',)
       
         
class studentTempAddressForm(forms.ModelForm):
    #student = forms.IntegerField()
    tempflatNo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Flat Number'}))
    tempstreet1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Street 1'}))
    tempstreet2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Street 2'}))
    tempcity = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    temppincode = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'pincode'}))
    tempstate = forms.ModelChoiceField(queryset=State.objects.all(),widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    #tempType = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3'}))
    class Meta:
        model = StudentAddress
        fields = ('flatNo','street1','street1','city','pincode','state')
        
        
class studentPermanantAddressForm(forms.ModelForm):
    #student = forms.IntegerField()
    flatNo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Flat Number'}))
    street1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Street 1'}))
    street2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Street 2'}))
    city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    pincode = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'pincode'}))
    state = forms.ModelChoiceField(queryset=State.objects.all(),widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    #type = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3'}))
    class Meta:
        model = StudentAddress
        fields = ('flatNo','street1','street1','city','pincode','state')  

#AddressFormset = inlineformset_factory(Student, StudentAddress, fields=('flat_no', 'street1','street2'),extra=1, can_delete=False)


class batchForm(forms.ModelForm): 
    batch = forms.ModelChoiceField(queryset=Batch.objects.all(),label="class",widget=forms.Select(attrs={'class':'form-control col-sm-3 bcsDiv','id':'idBatch'}))

    class Meta :
        model= Batch
        fields = ('batch',)

class classForm(forms.ModelForm): 
    grade_id = forms.ModelChoiceField(queryset=BatchClasses.objects.all(),required=False,label="class",widget=forms.Select(attrs={'class':' col-sm-3 bcsDiv form-control!important','id':'idClass'}))
    
    class Meta :
       model= BatchClasses
       fields = ('grade_id',)
       
    

class SectionsForm(forms.ModelForm): 
    section = forms.ModelChoiceField(queryset=Sections.objects.all(),required=False,label="class",widget=forms.Select(attrs={'class':'form-control col-sm-3 bcsDiv','id':'idSection'}))

    class Meta :
        model= ClassSection
        fields = ('section',)
        
class examResultForm(forms.ModelForm):
    exam_assign = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3'}))
    student_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3'}))
    marks_obtained = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3'}))
    total_marks = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3'}))
    status = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3'}))

    class Meta :
        model= ExamResult
        fields = ('exam_assign','student','total_marks','status')
        
class examTypeForm(forms.ModelForm):
    exam_type= forms.ModelChoiceField(queryset=ExamType.objects.all(),widget=forms.Select(attrs={'class':'form-control col-sm-3 ','id':'idExamType'}))
    
    class Meta :
        model= ExamType
        fields = ('exam_type',)

        
class subjectForm(forms.ModelForm): 
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(),widget=forms.Select(attrs={'class':' col-sm-3 form-control!important classViewAccess','id':'idSubject'}))
    class Meta :
        model= Subject
        fields = ('subject',)
        
class SyllabusForm(forms.ModelForm):
    syllabus=forms.ModelChoiceField(queryset=Syllabus.objects.all(),widget=forms.Select(attrs={'class':' col-sm-3 form-control!important classViewAccess','id':'idSyllabus'}))

    class Meta :
        model= Syllabus
        fields = ('syllabus',)
        
class clsForm(forms.ModelForm):
    classVal = forms.ModelChoiceField(queryset=Class.objects.all(),widget=forms.Select(attrs={'class':' col-sm-3  form-control!important classViewAccess','id':'idClassAssgmnt'}))
    
    class Meta :
       model= Class
       fields = ('class_field',)

class assignmentForm(forms.ModelForm):
    
    assignment_description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control classViewAccess','id':'idAssgnment'}))
    from_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control classViewAccess','id':'idFromDate','type':'date','name':'fromDate','placeholder':'yyyy-mm-dd', 'data-fv-date':'true','data-fv-date-format':'YYYY/MM/DD','data-fv-date-message':'The value is not a valid date'}))
    to_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control classViewAccess','id':'idTodate','type':'date','name':'toDate','placeholder':'yyyy-mm-dd'}))
    syllabus=forms.ModelChoiceField(queryset=Syllabus.objects.all(),widget=forms.TextInput(attrs={'class':'form-control classViewAccess','id':'idAssSyllabus','type':'hidden' ,'value':''}))

    class Meta :
        model= Assignment
        fields = ('assignment_description','from_date','to_date','syllabus')
        
class previousIntituteDetailsForm(forms.ModelForm):
    #previous_institute_id = forms.IntegerField()
    institute_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3 readOnlyClass','id':'id_institute_name','placeholder':'institute Name'}))
    last_class_attended = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3 readOnlyClass','id':'id_last_class_attended','placeholder':'Last Class Attended'}))
    duration = forms.CharField(required=False,widget=forms.TextInput( attrs={'class':'form-control col-sm-3 readOnlyClass','id':'id_duration','placeholder':'Duration in Previous  Instiute'}))
    
    class Meta:
        model = PreviousInstituteDetails
        fields = ('previous_institute_id','institute_name','last_class_attended','duration')
 

class PInstituAddressForm(forms.ModelForm):
    #student = forms.IntegerField()
    pInstituteflatNo = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3 readOnlyClass','placeholder':'Flat Number', 'id':'id_PrevIntflatNo'}))
    pInstitutestreet1 = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3 readOnlyClass','placeholder':'Street 1','id':'id_PrevIntstreet1'}))
    pInstitutestreet2 = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3 readOnlyClass','placeholder':'Street 2','id':'id_PrevIntstreet2'}))
    pInstitutecity = forms.ModelChoiceField(required=False,queryset=City.objects.all(), widget=forms.Select(attrs={'class':'form-control col-sm-3 readOnlyClass','id':'id_PrevIntcity'}))
    pInstitutepincode = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3 readOnlyClass','placeholder':'pincode','id':'id_PrevIntpincode'}))
    pInstitutestate = forms.ModelChoiceField(required=False,queryset=State.objects.all(),widget=forms.Select(attrs={'class':'form-control col-sm-3 readOnlyClass','id':'id_PrevIntstate'}))
    #type = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-3'}))
    class Meta:
        model = StudentAddress
        fields = ('flatNo','street1','street1','city','pincode','state')  
        
    
    