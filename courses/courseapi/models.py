from django.db import models

USER_TYPES = (
    ("student","Student"),
    ("professor","Professor")
)

class Users(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=10, default="")
    password = models.CharField(max_length=10, default="")
    type = models.CharField(choices=USER_TYPES, default="student",max_length=15)

class Course(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=4)
    score = models.FloatField()
    sequence = models.IntegerField(default=1)

class Lesson(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=4)
    score = models.FloatField()
    details = models.TextField()
    sequence = models.IntegerField(default=1)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

class Question(models.Model):
    name = models.CharField(max_length=100)
    score = models.FloatField()
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)

class ResponseQuestion(models.Model):
    name = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

class Exam(models.Model):
    student_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField()
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    lesson_id = models.ForeignKey(Lesson,on_delete=models.CASCADE)

class LessonResult(models.Model):
    lesson_id = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    state = models.CharField(max_length=15)

class CourseResult(models.Model):
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    student_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    state = models.CharField(max_length=15)

class AssignedCourse(models.Model):
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    student_id = models.ForeignKey(Users,on_delete=models.CASCADE)