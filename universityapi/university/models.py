from django.db import models

# Create your models here.

#creating university models
class University(models.Model):
    university_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('private','private'),('Government','Governmnet'),("Sem-Gov",'Sem-Gov')))
    added_data=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    # it is override the object which shows in form 
    def __str__(self):
        return self.name+"-"+self.location
    
    #create student model
    
class Student(models.Model):
    name=models.CharField(max_length=100)
    Roll_no=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    # photo=models.ImageField(upload_to='photo/',blank=True,null=True)
    # about=models.TextField()
    branch=models.CharField(max_length=50,choices=(
        ('CSE','CSE'),
        ('IT','IT'),
        ('ECE','ECE'),
        ('ME','ME')
        
    ))
    #told relation between universities and student which help to find which 
    # student belong to which university
    university_name=models.ForeignKey(University,on_delete=models.CASCADE)
    
    # Create teacher model
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    type=models.CharField(max_length=100,choices=(('private','private'),('Government','Governmnet'),("Sem-Gov",'Sem-Gov')) ,  null=True,
        blank=True)
    
    def __str__(self):
        return self.name
    

    # Relationship between teacher and university
    #here university show in html in django frame look like University
    university = models.ForeignKey(University, on_delete=models.CASCADE)
   
 #create staff model
 
class Staff(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=20)
    location=models.CharField(max_length=30)
    #relationship between staff and teacher
    
    
    
    
    teachers=models.ForeignKey(Teacher,on_delete=models.PROTECT)
    
    
         
    
    
