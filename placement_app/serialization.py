from rest_framework import serializers
from .models import PlacementDetails, Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



class PlacementDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacementDetails
        fields = '__all__'

class applicationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacementDetails
        fields = '__all__'