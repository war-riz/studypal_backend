from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    matricNumber = serializers.CharField(write_only=True)

    def validate(self, data):
        """ Check if the student_id exists """
        matricNumber = data.get("matricNumber")

        try:
            user = User.objects.get(matricNumber=matricNumber)
        except User.DoesNotExist:
            raise AuthenticationFailed("No account found with this matricNumber.")

        # Generate JWT token
        refresh = RefreshToken.for_user(user)

        return {
            "matricNumber": user.matricNumber,
            "fullName": user.fullName,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }
