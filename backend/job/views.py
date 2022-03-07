from webbrowser import get
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Min, Max, Count
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated

from .serializers import CandidatesAppliedSerializer, JobSerializer
from .models import CandidatesApplied, Job
from django.shortcuts import get_object_or_404
from .filters import JobsFilter
from django.utils import timezone

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
@permission_classes([IsAuthenticated])
def newJob(request):
    request.data['user'] = request.user
    data = request.data
    
    job = Job.objects.create(**data)
    
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)

# Update Job
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    
    if job.user != request.user:
        return Response({ 'message': 'You Cannot Update This Job!' }, status=status.HTTP_403_FORBIDDEN)
    
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
@permission_classes([IsAuthenticated])
def deleteJob(request, pk):
    job = get_object_or_404(Job, id=pk)
    
    if job.user != request.user:
        return Response({ 'message': 'You Cannot Delete This Job!' }, status=status.HTTP_403_FORBIDDEN)    
    
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



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def applyToJob(request, pk):
    
    user = request.user
    job = get_object_or_404(Job, id=pk)
    
    if user.userprofile.resume == '':
        return Response({ 'error': 'Please Upload Your Resume First!' }, 
                        status=status.HTTP_400_BAD_REQUEST)
    
    
    if job.lastDate < timezone.now():
        return Response({ 'error': 'You Cannot Apply To This Job Anymore. This Job Offer Has Expired!'}, 
                        status=status.HTTP_400_BAD_REQUEST)
        
        
    alreadyApplied = job.candidatesapplied_set.filter(user=user).exists()
    
    
    if alreadyApplied:
        return Response({ 'error': 'You Have Already Applied To This Job!'}, 
                        status=status.HTTP_400_BAD_REQUEST)
        
        
    jobApplied = CandidatesApplied.objects.create(
        job = job,
        user = user,
        resume = user.userprofile.resume
    )
    
    return Response({
        'applied': True,
        'job_id': jobApplied.id
    }, 
    status=status.HTTP_200_OK
    )
    
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCurrentUserAppliedJobs(request, pk):
    
    args = { 'user.id': request.user.id }
    
    jobs = CandidatesApplied.objects.filter(**args)
    
    serializer = CandidatesAppliedSerializer(jobs, many=True)
    
    return Response(serializer.data)