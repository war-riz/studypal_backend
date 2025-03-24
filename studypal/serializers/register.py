from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()  # Get our custom user model

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['student_id', 'full_name', 'course_of_study', 'gender', 'user_type']
    
    def validate_student_id(self, value):
        """ Ensure student ID is unique """
        if User.objects.filter(student_id=value).exists():
            raise serializers.ValidationError("A user with this Student ID already exists.")
        return value
    
    def create(self, validated_data):
        """ Create and return a new user instance """
        return User.objects.create(**validated_data)
