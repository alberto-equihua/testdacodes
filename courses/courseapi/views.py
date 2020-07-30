from django.shortcuts import render
from courseapi.models import Course, Lesson, ResponseQuestion, Question, Users, Exam, CourseResult, LessonResult, AssignedCourse
from django.http import HttpResponsePermanentRedirect

def index_view(request, *args, **kwargs):
    users = Users.objects.all()
    courses = Course.objects.all()
    lessons = Lesson.objects.all()
    questions = Question.objects.all()
    responses = ResponseQuestion.objects.all()
    assigned_course = AssignedCourse.objects.all()
    context = {
        'users': users,'courses':courses,'lessons':lessons,
        'questions':questions,'responses':responses,
        'assigned_course':assigned_course
    }
    return render(request, "index.html", context)

def action_to(request, *args, **kwargs):
    id = request.POST.get('id', False)
    model = request.POST.get('model', False)
    data = courses_list = lesson_list = question_list = student_list = None
    #print(request.POST.get('create'),request.POST.get('edit'), model)
    if request.POST.get('create'):
        if model in ('lesson','question','response','assigned'):
            courses_list = Course.objects.all()
            lesson_list = Lesson.objects.all()
            question_list = Question.objects.all()
            student_list = Users.objects.all()
        return render(request, "create.html", {'model':model,'courses_list':courses_list,'lesson_list':lesson_list,'question_list':question_list,'student_list':student_list})
    elif request.POST.get('edit'):
        if model == 'user':
            data = Users.objects.get(id=id)
        elif model == 'course':
            data = Course.objects.get(id=id)
        elif model == 'lesson':
            data = Lesson.objects.get(id=id)
            courses_list = Course.objects.all()
        elif model == 'question':
            data = Question.objects.get(id=id)
            lesson_list = Lesson.objects.all()
        elif model == 'response':
            data = ResponseQuestion.objects.get(id=id)
            question_list = Question.objects.all()
        elif model == 'assigned':
            data = AssignedCourse.objects.get(id=id)
            courses_list = Course.objects.all()
            student_list = Users.objects.all()
        return render(request, "edit.html", 
            {'model':model,'data': data,'courses_list':courses_list,'lesson_list':lesson_list,'question_list':question_list,'student_list':student_list}
        )
    elif request.POST.get('delete'):
        if model == 'user':
            data = Users.objects.get(id=id)
        elif model == 'course':
            data = Course.objects.get(id=id)
        elif model == 'lesson':
            data = Lesson.objects.get(id=id)
        elif model == 'question':
            data = Question.objects.get(id=id)
        elif model == 'response':
            data = ResponseQuestion.objects.get(id=id)
        elif model == 'assigned':
            data = AssignedCourse.objects.get(id=id)
        return render(request, "view.html", {'model':model,'data': data})
    return render(request, "index.html", {})

def view_view(request, *args, **kwargs):
    return render(request, "view.html", {})

def create_view(request, *args, **kwargs):
    model = request.POST.get('model', False)
    if model == 'user':
        new_u = Users()
        new_u.name = request.POST.get('name', False)
        new_u.username = request.POST.get('username', False)
        new_u.type = "student" if request.POST.get('type') else "professor"
        new_u.password = request.POST.get('password', False)
        new_u.save()
    elif model == 'course':
        new_course = Course()
        new_course.name = request.POST.get('name', False)
        new_course.score = request.POST.get('score', False)
        new_course.sequence = request.POST.get('sequence', False)
        new_course.save()
    elif model == 'lesson':
        new_less = Lesson()
        new_less.name = request.POST.get('name', False)
        new_less.score = request.POST.get('score', False)
        new_less.sequence = request.POST.get('sequence', False)
        new_less.details = request.POST.get('details', False)
        course_id = request.POST.get('course_id', False)
        course_id = Course.objects.get(id=course_id)
        new_less.course_id = course_id
        new_less.save()
    elif model == 'question':
        new_question = Question()
        new_question.name = request.POST.get('name', False)
        new_question.score = request.POST.get('score', False)
        lesson_id = request.POST.get('lesson_id', False)
        lesson_id = Lesson.objects.get(id=lesson_id)
        new_question.lesson_id = lesson_id
        new_question.save()
    elif model == 'response':
        is_correct = False
        new_resp = ResponseQuestion()
        new_resp.name = request.POST.get('name', False)
        if request.POST.get('is_correct') == 'on':
            is_correct = True
        new_resp.is_correct = is_correct
        question_id = request.POST.get('question_id', False)
        question_id = Question.objects.get(id=question_id)
        new_resp.question_id = question_id
        new_resp.save()
    elif model == 'assigned':
        assig = AssignedCourse()
        course_id = request.POST.get('course_id', False)
        student_id = request.POST.get('student_id', False)
        course_id = Course.objects.get(id=course_id)
        student_id = Users.objects.get(id=student_id)
        assig.course_id = course_id
        assig.student_id = student_id
        assig.save()
    return HttpResponsePermanentRedirect("/adminpanel/")

def edit_view(request, *args, **kwargs):
    model = request.POST.get('model', False)
    id = request.POST.get('id', False)
    if model == 'user':
        new_u = Users.objects.get(id=id)
        new_u.name = request.POST.get('name', False)
        new_u.username = request.POST.get('username', False)
        new_u.type = "student" if request.POST.get('type') else "professor"
        new_u.password = request.POST.get('password', False)
        new_u.save()
    elif model == 'course':
        new_course = Course.objects.get(id=id)
        new_course.name = request.POST.get('name', False)
        new_course.score = request.POST.get('score', False)
        new_course.sequence = request.POST.get('sequence', False)
        new_course.save()
    elif model == 'lesson':
        new_less = Lesson.objects.get(id=id)
        new_less.name = request.POST.get('name', False)
        new_less.score = request.POST.get('score', False)
        new_less.sequence = request.POST.get('sequence', False)
        new_less.details = request.POST.get('details', False)
        course_id = request.POST.get('course_id', False)
        course_id = Course.objects.get(id=course_id)
        new_less.course_id = course_id
        new_less.save()
    elif model == 'question':
        new_question = Question.objects.get(id=id)
        new_question.name = request.POST.get('name', False)
        new_question.score = request.POST.get('score', False)
        lesson_id = request.POST.get('lesson_id', False)
        lesson_id = Lesson.objects.get(id=lesson_id)
        new_question.lesson_id = lesson_id
        new_question.save()
    elif model == 'response':
        is_correct = False
        new_resp = ResponseQuestion.objects.get(id=id)
        new_resp.name = request.POST.get('name', False)
        if request.POST.get('is_correct') == 'on':
            is_correct = True
        new_resp.is_correct = is_correct
        question_id = request.POST.get('question_id', False)
        question_id = Question.objects.get(id=question_id)
        new_resp.question_id = question_id
        new_resp.save()
    elif model == 'assigned':
        assig = AssignedCourse.objects.get(id=id)
        course_id = request.POST.get('course_id', False)
        student_id = request.POST.get('student_id', False)
        course_id = Course.objects.get(id=course_id)
        student_id = Users.objects.get(id=student_id)
        assig.course_id = course_id
        assig.student_id = student_id
        assig.save()
    return HttpResponsePermanentRedirect("/adminpanel/")

def delete_view(request, *args, **kwargs):
    model = request.POST.get('model', False)
    id = request.POST.get('id', False)
    if model == 'user':
        u = Users.objects.get(id=id)
        u.delete()
    elif model == 'course':
        c = Course.objects.get(id=id)
        c.delete()
    elif model == 'lesson':
        l = Lesson.objects.get(id=id)
        l.delete()
    elif model == 'question':
        q = Question.objects.get(id=id)
        q.delete()
    elif model == 'response':
        r = ResponseQuestion.objects.get(id=id)
        r.delete()
    elif model == 'assigned':
        assig = AssignedCourse.objects.get(id=id)
        assig.delete()
    return HttpResponsePermanentRedirect("/adminpanel/")