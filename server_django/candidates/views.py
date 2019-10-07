from django.shortcuts import render
from .models import Candidate
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import django.db.utils
import json

# Create your views here.
def view_candidates(requests):
    context = {
        "candidates" : Candidate.objects.all()
    }
    myData = {
        "candidates": []
    }
    for job in context['candidates']:
        myData["candidates"].append(str(job))
    return HttpResponse(json.dumps(myData), status=200)


# pot new job
@csrf_exempt  #need to remove this fr postman to work
def post_candidates(requests):
    if requests.method == "POST":
        try:
            job_id = int(requests.POST['jobid'])
            job_title = requests.POST['jobtitle']
            email = requests.POST['email']
            name = requests.POST['name']
            j = Candidate(jobid = job_id, jobtitle = job_title, email = email, name = name)
            j.save()
        except django.db.utils.IntegrityError:
            return HttpResponse(json.dumps({"status": "email needs to unique"}), status=409)
        return HttpResponse(json.dumps({"status":"success"}), status=200)
    else:
        return HttpResponse(json.dumps({"status":"Not valid method"}), status=400)