from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['matricNumber', 'fullName', 'course', 'gender', 'role']
        read_only_fields = fields  # Make all fields read-only 