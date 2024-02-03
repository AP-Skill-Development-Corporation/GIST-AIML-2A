from django.db import models

# Create your models here.

class Student(models.Model):
	k = [
		('0','-- Select Branch --'),
		('1','Computer Science and Engineering'),
		('2','Artificial Intelligence/Machine Learning'),
		('3','Others'),
	]
	rn = models.CharField(max_length=12)
	sn = models.CharField(max_length=150)
	sy = models.IntegerField(default=1)
	sb = models.CharField(default='0',choices=k,max_length=5)

	