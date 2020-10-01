from api.models import Item
from django.contrib.auth.models import User
from rest_framework import test, status
from django.urls import reverse
from rest_framework.authtoken.models import Token


class ItemTest(test.APITestCase):
    def setUp(self):
        self.test_item = Item.objects.create(name="Test Item 1", quantity=1)
        
        self.test_user = User.objects.create_user(username='test_username', email='test_email', first_name='test_first_name', last_name='test_last_name', password='test_password')
        self.client.force_authenticate(user=self.test_user)

        self.items_list_url = reverse('items-list')
        # self.items_detail_url = reverse('items-detail')

    def test_authentication_enforced(self):
        """
            Test requirement of authentication.
        """
        new_client = test.APIClient()

        response = new_client.get(self.items_list_url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_items(self):
        """
            Test item retrieval.
        """
        item = Item.objects.latest('id')

        response = self.client.get(self.items_list_url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Item.objects.count(), 1)
    
    def test_create_item(self):
        """
            Test adding an item.
        """
        data = {
            "name": "Test Item 2",
            "quantity": 2
        }

        response = self.client.post(self.items_list_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_update_item(self):
        """
            Test updating an item.
        """
        change_data = {
            "name": "Changed Name"
        }

        item = Item.objects.get()

        response = self.client.put(
            reverse('items-detail', kwargs={'pk': item.id}),
            change_data,
            format='json'
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['name'], change_data['name'])

    def test_delete_item(self):
        """
            Test deleting an item.
        """
        item = Item.objects.get()

        response = self.client.delete(
            reverse('items-detail', kwargs={'pk': item.id}),
            format='json'
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
