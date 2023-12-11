from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobListSerializer,JobDetailSerializer, CompanyListSerializer,CompanyDetailSerializer
from .models import Jobs , Company
from rest_framework import generics
from .mypagination import MyPagination

class JobListAPI(generics.ListAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobListSerializer


class JobDetailAPI(generics.RetrieveAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobDetailSerializer


class CompanyListAPI(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer
    pagination_class = MyPagination 



class CompanyDetailAPI(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer