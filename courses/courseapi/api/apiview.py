from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from datetime import date
from django.http import HttpResponse, JsonResponse

from courseapi.models import Course, Lesson, ResponseQuestion, Question, Users, Exam, CourseResult, LessonResult, AssignedCourse
from courseapi.api.serializers import (
    CourseSerializer, LessonSerializer, UsersSerializer, ResponseSerializer, 
    QuestionSerializer, ExamSerializer, CourseResultSerializer, LessonResultSerializer, AssignedCourseSerializer
)

@api_view(['GET', 'POST'])
def api_users_view(request):
    userfound = None
    userfound = Users.objects.all()
    if request.method == 'GET':
        serializer = UsersSerializer(userfound, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def api_courses_view(request):
    courses = None
    student_id = 0
    if request.method == 'GET':
        courses = AssignedCourse.objects.all()
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if data.get('username'):
            student_id = Users.objects.get(username=data['username'])
            if student_id:
                courses = AssignedCourse.objects.filter(student_id=student_id.id)
    serializer = AssignedCourseSerializer(courses, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'POST'])
def api_lessons_view(request):
    courses = None
    student_id = 0
    if request.method == 'GET':
        lessons = Lesson.objects.all()
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if data.get('username'):
            course_id = AssignedCourse.objects.filter(
                student_id__username=data['username']
            )[0]
            lessons = Lesson.objects.filter(
                course_id=course_id.course_id.id
            )
    serializer = LessonSerializer(lessons, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'POST'])
def api_questions_view(request):
    questions = None
    if request.method == 'GET':
        questions = Question.objects.all()
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if data.get('username'):
            course_id = AssignedCourse.objects.filter(
                student_id__username=data['username']
            )[0]
            questions = Question.objects.filter(
                lesson_id__course_id=course_id.course_id.id
            )
    serializer = QuestionSerializer(questions, many=True)
    return JsonResponse(serializer.data, safe=False)