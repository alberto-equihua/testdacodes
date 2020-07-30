from rest_framework import serializers
from courseapi.models import Course, Lesson, ResponseQuestion, Question, Users, Exam, CourseResult, LessonResult, AssignedCourse

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['name','type','username']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name','number','score']

class LessonSerializer(serializers.ModelSerializer):
    course_id = CourseSerializer(many=False,read_only=False)
    class Meta:
        model = Lesson
        fields = ['name','number','score','course_id','details']

class QuestionSerializer(serializers.ModelSerializer):
    lesson_id = LessonSerializer(many=False, read_only=False)
    class Meta:
        model = Question
        fields = ['name','score','lesson_id']

class ResponseSerializer(serializers.ModelSerializer):
    question_id = QuestionSerializer(many=False,read_only=False)
    class Meta:
        model = ResponseQuestion
        fields = ['name','is_correct','question_id']

class ExamSerializer(serializers.ModelSerializer):
    student_id = UsersSerializer(many=False, read_only=False)
    course_id = CourseSerializer(many=False, read_only=False)
    lesson_id = LessonSerializer(many=False, read_only=False)
    question_ids = ResponseSerializer(many=True, read_only=False)
    class Meta:
        model = Exam
        fields = ['student_id','date','course_id','lesson_id','question_ids']

class LessonResultSerializer(serializers.ModelSerializer):
    lesson_id = LessonSerializer(many=False, read_only=False)
    class Meta:
        model = LessonResult
        fields = ['lesson_id','state']
    
class CourseResultSerializer(serializers.ModelSerializer):
    course_id = CourseSerializer(many=False, read_only=False)
    student_id = UsersSerializer(many=False, read_only=False)
    lesson_result_ids = LessonResultSerializer(many=True, read_only=False)
    class Meta:
        model = CourseResult
        fields = ['course_id','student_id','state','lesson_result_ids']

class AssignedCourseSerializer(serializers.ModelSerializer):
    course_id = CourseSerializer(many=False, read_only=False)
    #student_id = UsersSerializer(many=False, read_only=False)
    class Meta:
        model = AssignedCourse
        fields = ['course_id']