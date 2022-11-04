from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Staff"),(3,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

#create Admin model start:-
class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    create_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()
#Admin model finished;

#create staff model start

class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address=models.TextField()
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    objects = models.Manager()

#staff model finished

#create course model start

class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=250)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    objects = models.Manager()
#course model finished

#cteate subject model start
class Subjects(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=250)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE,default=1)
    staff_id=models.ForeignKey(Staffs,on_delete=models.CASCADE) #now adding staff field in subject model and linking using foreign key.
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    objects = models.Manager()

#subject model finished

#create students model:-
class Students(models.Model):
    id=models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender=models.CharField(max_length=250)
    profile_pic=models.FileField()
    address=models.TextField()
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING) #adding course field in student model and relating it course model using foreign key
    session_start_year=models.DateField()
    session_end_year=models.DateField()
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    object = models.Manager()

#students model finished;

#now create attendance model

class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    attendance_date=models.DateField(auto_now_add=True)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    object = models.Manager()

#create attendance report model

class AttendanceReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(Attendance,on_delete=models.DO_NOTHING)
    status=models.BooleanField(default=False)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    object=models.Manager()

#create students leave report Model
class LeaveReportStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    leave_date=models.CharField(max_length=250)
    leave_message=models.TextField()
    leave_status=models.BooleanField(default=False)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    object = models.Manager()

#create staffs leave report
class LeaveReportStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=250)
    leave_message = models.TextField()
    leave_status = models.BooleanField(default=False)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    object = models.Manager()

#create student feedback model

class FeedBackStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_report= models.TextField()
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    object = models.Manager()

#create staff feedback model

class FeedBackStaffs(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_report= models.TextField()
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    object = models.Manager()

#create student notification model
class NotificationStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    message = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    object = models.Manager()

#create staff notification
class NotificationStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    message = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    object = models.Manager()

#now my all database model has been ctrated

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance==2:
            Staffs.objects.create(admin=instance)
        if instance==3:
            Students.objects.create(admin=instance,course_id=Courses.objects.get(id=1),session_start_year="2020-01-01",session_end_year="2020-12-12",address="",prfile_pic="",gender="")

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,created,**kwargs):
        if instance.user_type==1:
            instance.adminhod.save()
        if instance.user_type==2:
            instance.staffs.save()
        if instance.user_type==3:
            instance.students.save()
