from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()  # Get our custom user model

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['matricNumber', 'fullName', 'course', 'gender', 'role']
    
    def validate_matricNumber(self, value):
        """ Ensure student ID is unique """
        if User.objects.filter(matricNumber=value).exists():
            raise serializers.ValidationError("A student with this matricNumber already exists.")
        return value
    
    def create(self, validated_data):
        """ Create and return a new user instance """
        return User.objects.create(**validated_data)
