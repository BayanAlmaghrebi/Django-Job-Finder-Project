from django.shortcuts import render
from django .views import generic
from .models import Jobs , Company


class JobList(generic.ListView):
    model = Jobs

class JobDetail(generic.DetailView):
    model = Jobs