
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import django.db.utils
from functools import singledispatch
# Import the models and the classes implemented there( indirectly means the table)
from .models import Job
# Create your views here.


# # index page
# def index(requests):
#     return render(requests, 'index.html')


# Need this inorder to serialize the data;
@singledispatch
def to_serializable(val):
    """Used by default."""
    return str(val)


# get all posted jobs
def get_jobs(requests):
    context = {
        "jobs": Job.objects.all()
    }
    # print(context)
    myData = {
        "jobs": []
    }
    for job in context['jobs']:
        myData["jobs"].append(str(job))
    return JsonResponse(myData, status=200)
    # return render(requests, 'get_jobs.html', context)


# pot new job
@csrf_exempt  #need to remove this fr postman to work
def post_jobs(requests):
    if requests.method == "POST":
        print(requests.POST)
        print(type(requests.POST))
        try:
            job_id = int(requests.POST['jobid'])
            job_title = requests.POST['jobtitle']
            job_desscription = requests.POST['jobdescription']
            j = Job(jobid = job_id, jobtitle = job_title, jobdescription = job_desscription)
            j.save()
        except django.db.utils.IntegrityError:
            return HttpResponse(json.dumps({"status":"Job ID needs to be unique"}))
        res = {
            "status":"success"
        }
        return JsonResponse(res,status=200 )
    else:
        res ={
            "status":"Not valid method"
        }
        return JsonResponse(res, status= 400 )
        # return render(requests, "succes.html")
