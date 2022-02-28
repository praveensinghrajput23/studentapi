from django.db.models import fields
from rest_framework import serializers
from .models import ScoreList, StudentDetails
  
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = ('full_name', 'address', 'email', 'guardian_name')

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreList
        fields = ('full_name', 'course_name', 'year', 'score')