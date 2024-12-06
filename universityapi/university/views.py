from django.shortcuts import render
from rest_framework import viewsets
from university.models import University
from university.serializers import UniversitySerializer,StudentSerializer,TeacherSerializer,StaffSerializer
#it used when used @action for used company_id 
from rest_framework.decorators import action
#write above code to remove error which comes in response
from rest_framework.response import Response
from university.models import University,Student,Teacher,Staff

# Create your views here.
class UniversityViewSet(viewsets.ModelViewSet):
    queryset=University.objects.all()
    serializer_class=UniversitySerializer
    
    
    #here get help to find all information about university
    @action(detail=True,methods=['get'])
    #here pk check university_id is valid or not
    def student(self,request,pk=None):
        try:
        
          university_name=University.objects.get(pk=pk)
          emps=Student.objects.filter(university_name=university_name)
          emps_serializer=StudentSerializer(emps,many=True,context={'request':request})
          return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
        'message':'University name might not exist !!'
    })
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    #teacher
class TeacherViewSet(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer  
    
    #staff
@action(detail=True,methods=['get'])
def staff(self,request,pk=None):
        try:
        
          teachers=Teacher.objects.get(pk=pk)
          emps=Student.objects.filter(teachers=teachers)
          emps_serializer=StaffSerializer(emps,many=True,context={'request':request})
          return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
        'message':'University name might not exist !!'
    })
class StaffViewSet(viewsets.ModelViewSet):
    queryset=Staff.objects.all()
    serializer_class=StaffSerializer
        
    
      