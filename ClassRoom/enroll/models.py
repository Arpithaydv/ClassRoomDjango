from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_id = models.AutoField(primary_key=True)
    room_no = models.IntegerField()

    def __str__(self):
        return self.course_name

class Professor(models.Model):
    professor_name = models.CharField(max_length =40)
    professor_id = models.AutoField(primary_key=True)
    course_held = models.OneToOneField(Course)

    def __str__(self):
        return self.professor_name

class Student(models.Model):
    student_name = models.CharField(max_length=40)
    student_id = models.AutoField(primary_key=True)
    professor = models.ForeignKey(Professor)
    course = models.ForeignKey(Course)


    def __str__(self):
        return self.student_name