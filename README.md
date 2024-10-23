# Ex02 Django ORM Web Application
## Date: 22/10/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
```
admin.py
from django.contrib import admin
from .models import bankloan,bankloanAdmin
admin.site.register(bankloan,bankloanAdmin)

models.py

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


```
### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM


## OUTPUT
![Alt text](<Screenshot 2024-10-23 142752.png>)




## RESULT
Thus the program for creating a database using ORM hass been executed successfully
