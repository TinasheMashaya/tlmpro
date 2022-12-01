from django import forms
from .models import LoginModel , CoursesModel ,StudentModel


# creating a form
class LoginForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = LoginModel

		# specify fields to be used
		fields = [
			"reg",
			"password",
		]

class CourseForm(forms.ModelForm):
    
	# create meta class
	class Meta:
		# specify model to be used
		model = CoursesModel()

		# specify fields to be used
		fields = [
			
			"course_name",
			"course_id",
			"lecturer",
			"picture",
			"rating",
			"assignment",
			"due_date",
			"grading",
			"description",
			"student_id"
		]
class StudentForm(forms.ModelForm):
    
	# create meta class
	class Meta:
		# specify model to be used
		model = StudentModel()

		# specify fields to be used
		fields = [
			
			"course_name",
			"course_id",
			"lecturer",
			"picture",
			"rating",
			"assignment",
			"due_date",
			"grading",
			"description",
			"student_id"
		]
