from django.db import models
from django.contrib import admin
class bankloan(models.Model):
	Name=models.CharField(max_length=100)
	Accountnumber=models.IntegerField(primary_key="Accountnumber")
	Moblienumber=models.IntegerField()
	Startingdate=models.DateField()
	Email=models.EmailField()
	Amount=models.IntegerField()
	Interest=models.FloatField()
	Endingdate=models.IntegerField()
class bankloanAdmin(admin.ModelAdmin):
	list_display=('Name','Accountnumber','Moblienumber','Startingdate','Email','Amount','Interest','Endingdate')



