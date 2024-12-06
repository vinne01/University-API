from django.contrib import admin
from django.urls import path,include
#router and universityviewset import
from university.views import UniversityViewSet,StudentViewSet,TeacherViewSet,StaffViewSet
from rest_framework import routers



router=routers.DefaultRouter()
router.register(r'universities',UniversityViewSet)
router.register(r'student',StudentViewSet)
router.register(r'teacher',TeacherViewSet)
router.register(r'staff',StaffViewSet)
urlpatterns = [
    path('',include(router.urls))
   
]