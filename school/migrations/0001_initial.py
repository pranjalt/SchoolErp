# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('batch_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('batch', models.CharField(blank=True, max_length=45, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'batch',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BatchClasses',
            fields=[
                ('batch_class_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'batch_classes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BatchClassSection',
            fields=[
                ('batch_class_section_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'batch_class_section',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('city', models.CharField(blank=True, max_length=45, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('class_field', models.CharField(blank=True, db_column='class', max_length=5, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'class',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClassSection',
            fields=[
                ('class_sec_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'class_section',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClassSubject',
            fields=[
                ('class_subject_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'class_subject',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClassSubjectSyllabus',
            fields=[
                ('class_sub_syll_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'class_subject_syllabus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClassTeacher',
            fields=[
                ('class_teacher_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'class_teacher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClassTeacherSubject',
            fields=[
                ('class_teacher_sub_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'class_teacher_subject',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClassTimetable',
            fields=[
                ('class_timetable_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('from_time', models.DateTimeField(blank=True, null=True)),
                ('to_time', models.DateTimeField(blank=True, null=True)),
                ('day', models.CharField(blank=True, max_length=10, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'class_timetable',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExamAssign',
            fields=[
                ('exam_assign_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('from_time', models.DateTimeField(blank=True, null=True)),
                ('to_time', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('day', models.CharField(blank=True, max_length=10, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'exam_assign',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExamType',
            fields=[
                ('exam_type_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('exam_type', models.CharField(blank=True, max_length=45, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'exam_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('parent_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('father_name', models.CharField(blank=True, max_length=45, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=45, null=True)),
                ('guardian_name', models.CharField(blank=True, max_length=45, null=True)),
                ('father_contact_no', models.BigIntegerField(blank=True, null=True)),
                ('mother_contact_no', models.BigIntegerField(blank=True, null=True)),
                ('guardian_contact_no', models.BigIntegerField(blank=True, null=True)),
                ('father_email_addr', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_email_addr', models.CharField(blank=True, max_length=100, null=True)),
                ('guardian_email_addr', models.CharField(blank=True, max_length=100, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'parent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParentStudent',
            fields=[
                ('parent_student_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'parent_student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('principal_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('principal_name', models.CharField(blank=True, max_length=45, null=True)),
                ('principal_contact_no', models.CharField(blank=True, max_length=45, null=True)),
                ('principal_email_addr', models.CharField(blank=True, max_length=100, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'principal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_code', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('school_name', models.CharField(blank=True, max_length=45, null=True)),
                ('branch', models.CharField(blank=True, max_length=45, null=True)),
                ('census_code', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('fax_no', models.BigIntegerField(blank=True, null=True)),
                ('telephone_no', models.BigIntegerField(blank=True, null=True)),
                ('email_address', models.CharField(blank=True, max_length=100, null=True)),
                ('website_url', models.CharField(blank=True, max_length=45, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'school',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('section_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('section', models.CharField(blank=True, max_length=1, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sections',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('state_name', models.CharField(blank=True, max_length=45, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'state',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=45, null=True)),
                ('last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('contact_no', models.BigIntegerField(blank=True, null=True)),
                ('aadhaar_no', models.CharField(blank=True, max_length=40, null=True)),
                ('admission_no', models.CharField(blank=True, max_length=45, null=True)),
                ('date_of_admission', models.DateField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=10, null=True)),
                ('mother_tongue', models.CharField(blank=True, max_length=20, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_no', models.CharField(blank=True, max_length=45, null=True)),
                ('street1', models.CharField(blank=True, max_length=45, null=True)),
                ('street2', models.CharField(blank=True, max_length=45, null=True)),
                ('pincode', models.BigIntegerField(blank=True, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'student_address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('subject', models.CharField(blank=True, max_length=45, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'subject',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('syllabus_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('syllabus', models.CharField(blank=True, max_length=45, null=True)),
                ('topic', models.CharField(blank=True, max_length=45, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'syllabus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('teacher_first_name', models.CharField(blank=True, max_length=45, null=True)),
                ('teacher_last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('teacher_contact_no', models.BigIntegerField(blank=True, null=True)),
                ('teacher_email_id', models.CharField(blank=True, max_length=100, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'teacher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TeacherTimetable',
            fields=[
                ('teacher_timetable_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('from_time', models.DateTimeField(blank=True, null=True)),
                ('to_time', models.DateTimeField(blank=True, null=True)),
                ('day', models.CharField(blank=True, max_length=10, null=True)),
                ('create_user', models.CharField(blank=True, max_length=20, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'teacher_timetable',
                'managed': False,
            },
        ),
    ]
