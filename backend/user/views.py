from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView



# Create your views here.
class SignInView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        email = request.data.get("email")
        password = request.data.get("password")

        # Authenticate user
        user = authenticate(email=email, password=password)

        # Check if authentication failed
        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        # Log in user
        login(request, user)


        csrf_token = get_token(request)

        # Get related DogUser instance (if exists)


        # Return response
        response = Response({
            "id": user.id,
            "email": user.email,
            "message": "Login successful"
        }, status=status.HTTP_200_OK)

        # Set CSRF token as a cookie
        response.set_cookie(
            key="csrftoken",
            value=csrf_token,
            httponly=False,  # Allow frontend to access it
            secure=False,  # TODO Set to False in local dev (use True for HTTPS)

            samesite="Lax"
        )

        return response