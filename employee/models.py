from django.db import models  
class Employee(models.Model):  
    employee_name = models.CharField(max_length=100)  
    employee_email = models.EmailField(unique=True)  
    class Meta:  
        db_table = "employee"