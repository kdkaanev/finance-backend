from django.urls import path, include
from rest_framework.routers import DefaultRouter


from backend.user.views import SignInView, SignOutView, SignUpView

router = DefaultRouter()

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path("signin/", SignInView.as_view(), name="signin"),
    path('signout/', SignOutView.as_view(), name="signout"),
    path("", include(router.urls)),
]