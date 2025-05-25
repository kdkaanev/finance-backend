from django.urls import path, include
from rest_framework.routers import DefaultRouter


from backend.user.views import SignInView



router = DefaultRouter()

urlpatterns = [
    path("auth/signin/", SignInView.as_view(), name="signin"),
    path("", include(router.urls)),
]