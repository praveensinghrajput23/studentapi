from django.shortcuts import render, get_object_or_404
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ScoreList, StudentDetails
from .serializer import StudentSerializer, ScoreSerializer
  
@api_view(['GET'])
def ApiOverview(request):
    student_api_urls = {
        'all_items': '/',
        'Search by Name': '/?full_name=full_name',
        'Search by guardian_name': '/?guardian_name=guardian_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/details/pk/delete'
    }
  
    return Response(student_api_urls)



  
@api_view(['POST'])
def add_student_details(request):
    details = StudentSerializer(data=request.data)
  
    
    if StudentDetails.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if details.is_valid():
        details.save()
        return Response(details.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def view_student_details(request):
   
    items = StudentDetails.objects.all()
    serializer = StudentSerializer(items, many=True)

    
    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_details(request, pk):
    item = StudentDetails.objects.get(pk=pk)
    data = StudentSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_details(request, pk):
    item = get_object_or_404(StudentDetails, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)



#student_score_list

@api_view(['GET'])
def ScoreApiOverview(request):
    student_api_urls = {
        'all_items': '/',
        'Search by Name': '/?full_name=full_name',
        'Add': '/create-scorelist',
        'Update': '/update-scorelist/pk',
        'Delete': '/delete-scorelist/pk/delete'
    }
  
    return Response(student_api_urls)



  
@api_view(['POST'])
def add_scorelist(request):
    details = ScoreSerializer(data=request.data)
  
    
    if ScoreList.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if details.is_valid():
        details.save()
        return Response(details.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def view_student_scorelist(request):
   
    items = ScoreList.objects.all()
    serializer = ScoreSerializer(items, many=True)

    
    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_scorelist(request, pk):
    item = ScoreList.objects.get(pk=pk)
    data = ScoreSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_scorelist(request, pk):
    item = get_object_or_404(ScoreList, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)