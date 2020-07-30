from django.urls import include, path
from courseapi.api.apiview import api_users_view,api_courses_view,api_lessons_view,api_questions_view
from rest_framework import routers
from courseapi.api import views

router = routers.DefaultRouter()
router.register(r'courses/test', views.CourseViewSet)
router.register(r'users/test', views.UsersViewSet)
router.register(r'lessons/test', views.LessonViewSet)
router.register(r'questions/test', views.QuestionViewSet)
router.register(r'responses/test', views.ResponseViewSet)

app_name = "courseapi"

urlpatterns = [
    path('', include(router.urls)),
    path('users/', api_users_view ,name='api_users'),
    path('courses/',api_courses_view,name='courses'),
    path('lessons/',api_lessons_view,name="lessons"),
    path('questions/',api_questions_view,name="questions")
    #path('courses/', CouseView.as_view(), name='courses'),
]