from django.db import models
from datetime import datetime 
import json

# Create your models here. db schema here
class Job(models.Model):
    jobid = models.IntegerField(unique = True)
    jobtitle = models.CharField(max_length = 128, unique = False) 
    jobdescription = models.CharField(max_length = 512, unique = False)
    time = models.DateTimeField(default = datetime.now, blank = True)
    company = models.CharField(max_length = 64, default = 'Joogle, Inc', blank = True)


    # Repr is when you want the data
    def __repr__(self):
        jid = self.jobid
        jtl = self.jobtitle
        jd = self.jobdescription
        tm = self.time
        res = {
            "jobid": jid,
            "jobtitle": jtl,
            "jobdescription": jd,
        }
        return res

# To return this way when called; for printing
    def __str__(self):
        jid = self.jobid
        jtl = self.jobtitle
        jd = self.jobdescription
        tm = self.time
        res = {
            "jobid": jid,
            "jobtitle":jtl,
            "jobdescription": jd,
        }
        return f"{res}"



    # To check if the new tables are inserted in the db, go to shell (python manage.py shell) and rn the commands below
        # from jobs.models import Job
        # j.save()
        # j = Job(jobid = 12324, jobtitle = "Software Engineer", jobdescription = "Need to work hard")
        # Job.objects.all()
     