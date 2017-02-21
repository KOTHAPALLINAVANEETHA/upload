# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('leaves', models.CharField(max_length=30, choices=[(b'LA', b'leavesavailed'), (b'LAV', b'leavesavailable'), (b'LR', b'leaverequest')])),
                ('leaves_taken', models.DateField(max_length=30, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Official',
            fields=[
                ('Designations', models.CharField(max_length=40, choices=[(b'ACC', b'Accountant'), (b'TL', b'Teamlead'), (b'Exe', b'executive'), (b'Man', b'manager'), (b'LA', b'linuxadministrator'), (b'NT', b'networktrainer'), (b'PD', b'pythondeveloper'), (b'TM', b'traineemanager'), (b'US-IT', b'us-it recruiter'), (b'TC', b'technicalconsultant'), (b'SR', b'seniorexecutive'), (b'ASST', b'assistantmanager'), (b'MD', b'microsoftdynamics-practicehead'), (b'SA', b'systemadministrator'), (b'INT', b'intern'), (b'LI', b'linuxintern'), (b'OA', b'officeassistant')])),
                ('DOJ', models.DateField(max_length=20, null=True, blank=True)),
                ('Supervisor', models.CharField(max_length=40, verbose_name=b'supervisor')),
                ('Subordinates', models.CharField(max_length=20, verbose_name=b'subordinates')),
                ('departments', models.CharField(max_length=20, serialize=False, primary_key=True, choices=[(b'ES', b'ES01'), (b'ES', b'ES02'), (b'ES', b'ES03'), (b'ES', b'ES04'), (b'ES', b'ES05'), (b'ES', b'ES06'), (b'ES', b'ES07'), (b'ES', b'ES08'), (b'ES', b'ES09'), (b'ES', b'ES10'), (b'ES', b'ES12')])),
                ('codes', models.CharField(max_length=30, choices=[(b'ES08', b'Recruitment'), (b'ES05', b'Bench sales'), (b'ES07', b'ClientAcquistion'), (b'ES06', b'IT Recruitment'), (b'ES11', b'Operations'), (b'ES04', b'Softare and development'), (b'ES09', b'Accounts'), (b'ES10', b'Immigration'), (b'ES02', b'HR'), (b'ES12', b'IT Support'), (b'ES03', b'Training and department'), (b'ES01', b'Management')])),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('Emp_ID', models.CharField(default=1, max_length=10, serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=30, verbose_name=b'employeename')),
                ('Surname', models.CharField(max_length=30, verbose_name=b'employee_surname')),
                ('ContactNumber', models.CharField(max_length=40)),
                ('emailaddress', models.EmailField(max_length=20, verbose_name=b'email')),
                ('Residentialaddress', models.CharField(max_length=30, verbose_name=b'Residentialaddress')),
                ('EmergencyContact', models.CharField(max_length=40)),
                ('DOB', models.DateField(max_length=10, null=True, blank=True)),
                ('bloodgroup', models.CharField(max_length=10, choices=[(b'O+', b'opositive'), (b'O-', b'Onegative'), (b'AB+', b'ABpositive'), (b'AB-', b'ABnegative')])),
                ('marital_status', models.CharField(max_length=20, choices=[(b'S', b'single'), (b'M', b'married'), (b'U', b'unmarried')])),
                ('Father_name', models.CharField(max_length=30, verbose_name=b'Fathername')),
                ('Mother_name', models.CharField(max_length=40, verbose_name=b'Mothername')),
                ('Spouse_name', models.CharField(max_length=40, verbose_name=b'Spousename')),
                ('kidsdetails', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monthly_salary', models.IntegerField(default=10000, null=True, blank=True)),
                ('EMP_ID', models.ForeignKey(to='hrmsapp.Personal')),
            ],
        ),
        migrations.AddField(
            model_name='official',
            name='EMP_ID',
            field=models.ForeignKey(to='hrmsapp.Personal'),
        ),
    ]
