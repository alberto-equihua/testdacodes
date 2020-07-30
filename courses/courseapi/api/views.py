from rest_framework import viewsets
from courseapi.models import Course, Lesson, ResponseQuestion, Question, Users, Exam, CourseResult, LessonResult, AssignedCourse
from courseapi.api.serializers import (
    CourseSerializer, LessonSerializer, UsersSerializer, ResponseSerializer, 
    QuestionSerializer, ExamSerializer, CourseResultSerializer, LessonResultSerializer, AssignedCourseSerializer
)
class CourseViewSet(viewsets.ModelViewSet):
    queryset = AssignedCourse.objects.all()
    serializer_class = AssignedCourseSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = ResponseQuestion.objects.all()
    serializer_class = ResponseSerializer