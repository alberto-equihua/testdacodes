"""courses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from courseapi.views import index_view,view_view,create_view,edit_view,delete_view,action_to

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminpanel/',index_view,name="index"),
    path('action_to/',action_to,name='action_to'),
    path('view/',view_view,name='view'),
    path('create/',create_view,name="create"),
    path('edit/',edit_view,name="edit"),
    path('delete/',delete_view,name="delete"),
    path('api/', include('courseapi.api.urls'))
]