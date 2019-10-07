# import these two
from django.urls import path
from . import views

urlpatterns = [
    path('view', views.view_candidates, name = 'viewCandidates'),
    path('post', views.post_candidates, name = "postCandidates")
]

