
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_signup_success(self):
        data = {
            "email": "test@example.com",
            "password": "securepassword123"
        }

        response = self.client.post("/user/signup/", data, format='json')

        # Check response status
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["message"], "User created and logged in successfully")

        # Check user created
        self.assertTrue(User.objects.filter(email="test@example.com").exists())

        # Check cookie is set
        self.assertIn("csrftoken", response.cookies)

        # Check user is authenticated in session
        user_id = self.client.session.get('_auth_user_id')
        self.assertIsNotNone(user_id)

# Create your tests here.
class SignInViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="aa@aa.aa", password="password123")
    def test_signin_success(self):
        data = {
            "email": "aa@aa.aa",
            "password": "password123"
        }
        response = self.client.post("/user/signin/", data, format='json')
        # Check response status
        self.assertEqual(response.status_code, 200)
        self.assertIn("csrftoken", response.cookies)
        # Check user is authenticated in session
        user_id = self.client.session.get('_auth_user_id')
        self.assertIsNotNone(user_id)
    def test_signin_failure(self):
        data = {
            "email": "sdc@as.aa",
            "password": "wrongpassword"
        }
        response = self.client.post("/user/signin/", data, format='json')
        # Check response status
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data["detail"], "Invalid credentials")
class SignOutViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="aa@aa.aa", password="password123")
    def test_signout_success(self):
        # First, log in the user
        self.client.login(email="aa@aa.aa", password="password123")
        response = self.client.post("/user/signout/", format='json')
        # Check response status
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "Logged out successfully.")
        # Check user is logged out
        user_id = self.client.session.get('_auth_user_id')
        self.assertIsNone(user_id)
        # Check CSRF token is cleared
        self.assertNotIn("csrftoken", response.cookies)
        # Check session is cleared
        self.assertEqual(self.client.session.keys(), set())




