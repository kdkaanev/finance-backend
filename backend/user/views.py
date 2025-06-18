from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
from backend.user.models import FinanceUser
from backend.user.serializers import ProfileSerializer


def get_csrf_token(request):
    return JsonResponse({"csrfToken": get_token(request)})

# Create your views here.
class SignUpView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        password = request.data.get("password")
        email = request.data.get("email")

        if not email or not password:
            return Response(
                {"error": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if FinanceUser.objects.filter(email=email).exists():
            return Response(
                {"email": ["Email is already in use."]},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = FinanceUser.objects.create_user(email=email, password=password)
        except IntegrityError:
            return Response(
                {"error": "Could not create user due to a database error."},
                status=status.HTTP_400_BAD_REQUEST
            )

        login(request, user)

        csrf_token = get_token(request)
        response = Response(
            {"message": "User created and logged in successfully"},
            status=status.HTTP_201_CREATED
        )

        response.set_cookie(
            key="csrftoken",
            value=csrf_token,
            httponly=False,
            secure=False,  # Set to True with HTTPS
            samesite="Lax"
        )

        return response
class SignInView(APIView):
    permission_classes = [AllowAny]


    def post( self,request):
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

        profile = getattr(user, "profile", None)
        finance_user_data = ProfileSerializer(profile).data if profile else None
        if profile:
            finance_user_data = {

                "first_name": profile.first_name,
                "last_name": profile.last_name,

            }
        else:
            finance_user_data = None
        # Return response
        response = Response({
            "id": user.id,
            "email": user.email,
            "message": "Login successful",
            "profile": finance_user_data

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


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]



    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

        profile = getattr(user, "profile", None)
        finance_user_data = ProfileSerializer(profile).data if profile else None
        response_data = {
            "id": user.id,
            "email": user.email,
            "profile": finance_user_data
        }
        return Response(response_data, status=status.HTTP_200_OK)


    def patch(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ProfileSerializer(user.profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


