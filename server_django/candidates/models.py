from django.db import models
from datetime import datetime 

# Create your models here. Candidate model
class Candidate(models.Model):
    jobid = models.IntegerField(unique = False)
    jobtitle = models.CharField(max_length = 128, unique = False) 
    time = models.DateTimeField(default = datetime.now, blank = True)
    email = models.CharField(max_length = 256, unique = True)
    name = models.CharField(max_length = 128, unique = False)

    # To return this way when called
    def __str__(self):
        return f"The Job ID is {str(self.jobid)} with title {self.jobtitle} with candidate email {self.email} and name {self.name}"





