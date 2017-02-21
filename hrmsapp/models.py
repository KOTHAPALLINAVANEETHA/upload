from django.db import models
from django import forms
#from archive_field.fields import ArchiveField
from django.core.urlresolvers import reverse

# Create your models here.
BLOODGROUPS=(
	('O+','opositive'),
	('O-','Onegative'),
	('AB+','ABpositive'),
	('AB-','ABnegative'),
)
MARITALSTATUS=(
    ('S','single'),
    ('M','married'),
    ('U','unmarried'),
)
DESIGNATIONS=(
	('ACC','Accountant'),
	('TL','Teamlead'),
	('Exe','executive'),
	('Man','manager'),
	('LA','linuxadministrator'),
	('NT','networktrainer'),
	('PD','pythondeveloper'),
	('TM','traineemanager'),
	('US-IT','us-it recruiter'),
	('TC','technicalconsultant'),
	('SR','seniorexecutive'),
	('ASST','assistantmanager'),
	('MD','microsoftdynamics-practicehead'),
	('SA','systemadministrator'),
	('INT','intern'),
	('LI','linuxintern'),
	('OA','officeassistant'),
)
DEPARTMENTS=(
    ('ES','ES01'),
    ('ES','ES02'),
    ('ES','ES03'),
    ('ES','ES04'),
    ('ES','ES05'),
    ('ES','ES06'),
    ('ES','ES07'),
    ('ES','ES08'),
    ('ES','ES09'),
    ('ES','ES10'),
    ('ES','ES12'),
)
CODES={
    ('ES01','Management'),
    ('ES02','HR'),
    ('ES03','Training and department'),
    ('ES04','Softare and development'),
    ('ES05','Bench sales'),
    ('ES06','IT Recruitment'),
    ('ES07','ClientAcquistion'),
    ('ES08','Recruitment'),
    ('ES09','Accounts'),
    ('ES10','Immigration'),
    ('ES11','Operations'),
    ('ES12','IT Support'),
}
LEAVES=(
    ('LA','leavesavailed'),
    ('LAV','leavesavailable'),
    ('LR','leaverequest'),
)


class Personal(models.Model):
    Emp_ID = models.CharField(primary_key=True,default=1,max_length=10)
    Name = models.CharField(max_length=30,verbose_name="employeename")
    Surname =  models.CharField(max_length=30,verbose_name = "employee_surname")
    ContactNumber = models.CharField(max_length=40)
    emailaddress = models.EmailField(max_length=20,verbose_name = "email")
    Residentialaddress = models.CharField(max_length=30, verbose_name = "Residentialaddress")
    EmergencyContact = models.CharField(max_length=40)
    DOB = models.DateField(max_length=10,blank=True,null=True)
    bloodgroup = models.CharField(max_length=10,choices=BLOODGROUPS)
    marital_status =  models.CharField(max_length=20,choices=MARITALSTATUS)
    Father_name =  models.CharField(max_length=30, verbose_name="Fathername")
    Mother_name =  models.CharField(max_length=40,verbose_name="Mothername")
    Spouse_name =  models.CharField(max_length=40,verbose_name="Spousename")
    kidsdetails = models.IntegerField(default=0)


    def __unicode__(self):
		return  '%s'%(self.Name)


class Official(models.Model):
    EMP_ID = models.ForeignKey('Personal',on_delete=models.CASCADE)
    Designations = models.CharField(max_length=40,choices=DESIGNATIONS)
    DOJ = models.DateField(max_length=20,blank=True,null=True)
    Supervisor = models.CharField(max_length=40,verbose_name="supervisor")
    Subordinates = models.CharField(max_length=20, verbose_name="subordinates")
    departments = models.CharField(primary_key=True,max_length=20,choices=DEPARTMENTS)
    codes = models.CharField(max_length=30,choices=CODES)

    def __unicode__(self):
    	return str(self.Designations)
'''

class Department(models.Model):
    departments = models.CharField(primary_key=True,max_length=20,choices=DEPARTMENTS)
    codes = models.CharField(max_length=20,choices=CODES)
'''
class Leave(models.Model):
    leaves = models.CharField(max_length=30,choices=LEAVES)
    leaves_taken = models.DateField(max_length=30,blank=True,null=True)


    def __unicode__(self):
    	return str(self.leaves)

class Salary(models.Model):
    EMP_ID = models.ForeignKey('Personal',on_delete=models.CASCADE)
    monthly_salary = models.IntegerField(default=10000,blank=True,null=True)
'''
class Archieve(models.Model):
    archieve = ArchveFileField(upload_to='test_archive')
'''
class Archive(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()

    def get_absolute_url(self):
        return reverse('archive-detail', kwargs={'pk': self.pk})

class Upload(models.Model):
    personal_doc = models.FileField(upload_to='Documents/')
    office_doc = models.FileField(upload_to='Documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.uploaded_at)







