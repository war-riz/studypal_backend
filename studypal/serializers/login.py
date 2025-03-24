from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    student_id = serializers.CharField(write_only=True)

    def validate(self, data):
        """ Check if the student_id exists """
        student_id = data.get("student_id")

        try:
            user = User.objects.get(student_id=student_id)
        except User.DoesNotExist:
            raise AuthenticationFailed("No account found with this Student ID.")

        # Generate JWT token
        refresh = RefreshToken.for_user(user)

        return {
            "student_id": user.student_id,
            "full_name": user.full_name,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }
