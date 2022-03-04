from webbrowser import get
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count
from rest_framework.pagination import PageNumberPagination

from .serializers import JobSerializer
from .models import Job
from django.shortcuts import get_object_or_404
from .filters import JobsFilter

# Create your views here.

# Get all jobs
@api_view(['GET'])
def getAllJobs(request):
    
    # Filter jobs
    filterset = JobsFilter(request.GET, queryset=Job.objects.all().order_by('id'))
    count = filterset.qs.count()
    
    # Pagination
    resultsPerPage = 3
    paginator = PageNumberPagination()
    paginator.page_size = resultsPerPage
    queryset = paginator.paginate_queryset(filterset.qs, request)
    
    serializer = JobSerializer(queryset, many=True)
    return Response({
        'count': count,
        'resultsPerPage': resultsPerPage,
        'jobs': serializer.data
        })

# Get job by ID
@api_view(['GET'])
def getJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    
    serializer = JobSerializer(job, many=False)
    
    return Response(serializer.data)

# Create a new job
@api_view(['POST'])
def newJob(request):
    data = request.data
    
    job = Job.objects.create(**data)
    
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)

# Update Job
@api_view(['PUT'])
def updateJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    
    job.title = request.data['title']
    job.description = request.data['description']
    job.email = request.data['email']
    job.address = request.data['address']
    job.jobType = request.data['jobType']
    job.experience = request.data['experience']
    job.field = request.data['field']
    job.salary = request.data['salary']
    job.positions = request.data['positions']
    job.company = request.data['company']
    
    job.save()
    
    serializer = JobSerializer(job, many=False)
    
    return Response(serializer.data)


# Delete a job
@api_view(['DELETE'])
def deleteJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    
    job.delete()
    
    return Response({ 'message': 'The Job Has Been Deleted!'}, status=status.HTTP_200_OK)


# Stats
@api_view(['GET'])
def getTopicStats(request, topic):
    
    args = { 'title__icontains': topic }
    jobs = Job.objects.filter(**args)
    
    if len(jobs) == 0:
        return Response({ 'message': 'There are no stats available for {topic}'.format(topic=topic) })
    
    
    stats = jobs.aggregate(
        total_jobs = Count('title'),
        avg_positions = Avg('positions'),
        avg_salary = Avg('salary'),
        min_salary = Min('salary'),
        max_salary = Max('salary')
    )
    
    return Response(stats)
    

    