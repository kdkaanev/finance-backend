from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from backend.user.models import FinanceUser


def get_csrf_token(request):
    return JsonResponse({"csrfToken": get_token(request)})

# Create your views here.
class SignUpView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        password = request.data.get("password")
        email = request.data.get("email")

        user = FinanceUser.objects.create_user(password=password, email=email)
        login(request, user)
        # Create a token for the user
        csrf_token = get_token(request)
        response = Response({
            "message": "User created and logged in successfully"
        }, status=status.HTTP_201_CREATED)

        # Set CSRF cookie
        response.set_cookie(
            key="csrftoken",
            value=csrf_token,
            httponly=False,  # Allow frontend JS to read the CSRF token
            secure=False,  # Set to True in production with HTTPS
            samesite="Lax"
        )

        return response
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

class SignOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return self.perform_logout(request)

    def delete(self, request):
        return self.perform_logout(request)

    @staticmethod
    def perform_logout(request):
        logout(request)
        response = Response({"message": "Logged out successfully."}, status=200)
        response.delete_cookie("sessionid", path="/", domain=None)
        response.delete_cookie("csrftoken", path="/", domain=None)
        return response