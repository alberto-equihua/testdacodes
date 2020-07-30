from django.contrib import admin
from courseapi.models import Course, Lesson, ResponseQuestion, Question, Users, Exam, CourseResult, LessonResult

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(ResponseQuestion)
admin.site.register(Question)
admin.site.register(Users)
admin.site.register(Exam)
admin.site.register(LessonResult)
admin.site.register(CourseResult)
