from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.serializers import MenuSerializer
from rest_framework.authtoken.models import Token


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title='Spaghetti Carbonara', Price=18, Inventory=50)
        Menu.objects.create(Title='Lemon Risotto', Price=12, Inventory=30)
        Menu.objects.create(Title='Linguini and Clam Sauce', Price=21, Inventory=15)

    def test_getall(self):
        url = reverse('menu')
        client = APIClient()
        user = Token.objects.get(key='your_token_key').user
        print(f"User: {user.username}, Permissions: {user.get_all_permissions()}")
        token= 'eca4e010c2928c0352d5b84780e86e47fce4fa95'
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = client.get(url)

        if response.status_code == status.HTTP_200_OK:
            expected_data = MenuSerializer(Menu.objects.all(), many=True).data
            self.assertEqual(response.data, expected_data)
        else:
            self.assertEqual(response.data, {'detail': 'Authenticated'})





