from rest_framework import serializers
#university is app
from university.models import University,Student,Teacher,Staff
#create serializers here
class UniversitySerializer(serializers.HyperlinkedModelSerializer):
    university_id=serializers.ReadOnlyField()
    class Meta :
        model=University
        fields="__all__"
        
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    
    class Meta:
        model=Student
        fields="__all__"  
        
#teacher
class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    teacher_id=serializers.ReadOnlyField()
    
    class Meta:
        model=Teacher
        fields="__all__"   
        
#Staff
class StaffSerializer(serializers.HyperlinkedModelSerializer):
     staff_no=serializers.ReadOnlyField()
     
     class Meta:
         model= Staff
         fields="__all__"                     