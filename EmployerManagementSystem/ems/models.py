from django.db import models

class CompanyAdmin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=100)
    admin_email = models.EmailField(max_length=100)
    admin_password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.admin_id) + " - " + str(self.admin_name) + " - " + str(self.admin_email)

class EmployerData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile = models.EmailField(max_length=15)
    design = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + " - " + str(self.name) + " - " + str(self.email)

