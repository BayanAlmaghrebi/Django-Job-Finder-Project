from django.urls import path
from .views import JobList , JobDetail 
from .api import  JobListAPI, JobDetailAPI, CompanyListAPI, CompanyDetailAPI

urlpatterns = [
    path('', JobList.as_view()),
    path('<slug:slug>' , JobDetail.as_view()),
   

        # api
  
    path('api/list2',JobListAPI.as_view()),
    path('api/list2/<int:pk>' , JobDetailAPI.as_view()),
    path('api/list/company',CompanyListAPI.as_view()),
    path('api/list/company/<int:pk>' , CompanyDetailAPI.as_view())
]
