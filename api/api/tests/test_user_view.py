from django.contrib.auth.models import User
from rest_framework import test, status
from django.urls import reverse
from rest_framework.authtoken.models import Token


class UserTest(test.APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='test_username', email='test_email', first_name='test_first_name', last_name='test_last_name', password='test_password')
        
        self.signup_url = reverse('user-create')
        self.login_url = reverse('user-login')
    
    def test_create_user(self):
        """
            Test user creation with valid inputs.
        """
        data = {
            'username': 'usertest',
            'email': 'djangotest@test.com',
            'first_name': 'User',
            'last_name': 'Test',
            'password': 'djangousertest'
        }

        response = self.client.post(self.signup_url, data, format='json')
        user = User.objects.latest('id')
        user_token = Token.objects.get(user=user)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse('password' in response.data)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.data['token'], user_token.key)

    def test_create_user_with_existing_username(self):
        """
            Test user creation endpoint with pre-existing username.
        """
        data = {
            'username': 'test_username',
            'email': 'djangotest@test.com',
            'first_name': 'User',
            'last_name': 'Test',
        }

        response = self.client.post(self.signup_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_create_user_with_existing_email(self):
        """
            Test user creation endpoint with pre-existing username.
        """
        data = {
            'username': 'usertest',
            'email': 'test_email',
            'first_name': 'User',
            'last_name': 'Test',
        }

        response = self.client.post(self.signup_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_create_user_without_password(self):
        """
            Test user creation endpoint without password.
        """
        data = {
            'username': 'usertest',
            'email': 'djangotest@test.com',
            'first_name': 'User',
            'last_name': 'Test',
        }

        response = self.client.post(self.signup_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_login_user(self):
        """
            Test user login.
        """
        create_data = {
            'username': 'usertest',
            'email': 'djangotest@test.com',
            'first_name': 'User',
            'last_name': 'Test',
            'password': 'djangousertest'
        }

        self.client.post(self.signup_url, create_data, format='json')
        self.assertEqual(User.objects.count(), 2)
        login_data = {
            'username': 'usertest',
            'password': 'djangousertest'
        }

        response = self.client.post(self.login_url, login_data, format='json')
        user = User.objects.latest('id')
        user_token = Token.objects.get(user=user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['token'], user_token.key)

    def test_faulty_login_user(self):
        """
            Test faulty user login.
        """
        create_data = {
            'username': 'usertest',
            'email': 'djangotest@test.com',
            'first_name': 'User',
            'last_name': 'Test',
            'password': 'djangousertest'
        }

        self.client.post(self.signup_url, create_data, format='json')
        self.assertEqual(User.objects.count(), 2)
        
        login_data = {
            'username': 'wrong_user_name',
            'password': 'djangousertest'
        }

        response = self.client.post(self.login_url, login_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(response.data['error'], "Please make sure the credentials are correct, or try signing-up!")
