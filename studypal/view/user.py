from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from ..serializers.user import UserSerializer

class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            # Get the access token from Authorization header
            auth_header = request.headers.get('Authorization')
            if not auth_header or not auth_header.startswith('Bearer '):
                return Response({"detail": "Authorization header with access token is required"}, status=status.HTTP_401_UNAUTHORIZED)
            
            access_token = auth_header.split(' ')[1]
            
            # Get the refresh token from request body
            refresh_token = request.data.get('refresh_token')
            if not refresh_token:
                return Response({"detail": "Refresh token is required in request body"}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                # Blacklist the refresh token
                refresh = RefreshToken(refresh_token)
                refresh.blacklist()
                
                # Blacklist the access token
                try:
                    access = AccessToken(access_token)
                    access.blacklist()
                except Exception:
                    # If access token is invalid or already expired, we can ignore it
                    pass
                
                return Response({"detail": "Successfully logged out"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"detail": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"detail": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST) 