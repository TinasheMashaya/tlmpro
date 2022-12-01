# import the standard Django Model
# from built-in library
from django.db import models

# declare a new model with a name "GeeksModel"
class LoginModel(models.Model):

	# fields of the model
	reg = models.CharField(max_length = 200)
	password = models.TextField()

	# renames the instances of the model
	# with their title name
	def __str__(self):
		return self.reg


class CoursesModel(models.Model):
    
	# fields of the model
	course_name = models.CharField(max_length = 200)
	course_id =models.CharField(max_length = 200)
	lecturer = models.CharField(max_length = 200)
	picture = models.CharField(max_length = 200)
	rating= models.CharField(max_length = 200)
	assignment = models.CharField(max_length = 200)
	due_date= models.CharField(max_length = 200)
	grading = models.CharField(max_length = 200)
	description=  models.CharField(max_length = 200)
	student_id = models.CharField(max_length = 200)

class StudentModel(models.Model):
    
	# fields of the model
	course_name = models.CharField(max_length = 200)
	course_id =models.CharField(max_length = 200)
	lecturer = models.CharField(max_length = 200)
	picture = models.CharField(max_length = 200)
	rating= models.CharField(max_length = 200)
	assignment = models.CharField(max_length = 200)
	due_date= models.CharField(max_length = 200)
	grading = models.CharField(max_length = 200)
	description=  models.CharField(max_length = 200)
	student_id = models.CharField(max_length = 200)


	
	def __str__(self):
		return self.course_name


