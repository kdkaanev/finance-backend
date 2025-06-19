from django.urls import path, include
from rest_framework.routers import DefaultRouter


from backend.user.views import SignInView, SignOutView, SignUpView, get_csrf_token, CurrentUserView

router = DefaultRouter()
# Registering the viewsets with the router


urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path("signin/", SignInView.as_view(), name="signin"),
    path('signout/', SignOutView.as_view(), name="signout"),
    path('csrf/', get_csrf_token, name='csrf'),
    path('me/', CurrentUserView.as_view(), name='me'),  # Assuming you want to keep this for user info
    path("", include(router.urls)),
]