# import these two
from django.urls import path
from . import views

urlpatterns = [
    # the path we need to go is jobs/get; since jobs is the main url defined at projects main url.py
    # then we concat weith get here in this urls.py, thereofe we need to go /jobs/get
    path('view', views.get_jobs, name = 'getJobs'),
    # now link this to main projects urls
    path('post', views.post_jobs, name = 'postJobs')
]