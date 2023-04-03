from rest_framework.authtoken.models import Token
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from flight.models import Flight
from flight.views import FlightView
from datetime import datetime, date

class FlightTestCase(APITestCase):
    today = date.today()
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')

    def setUp(self):
        self.factory = APIRequestFactory()
        self.flight = Flight.objects.create(
            flight_number='123ABC',
            operation_airlines='THY',
            departure_city='ADANA',
            arrival_city='ANKARA',
            date_of_departure=f'{self.today}',
            etd=f'{self.current_time}'
        )
        self.user = User.objects.create_user(
            username='admin',
            password='Aa654321*'
        )
        self.token = Token.objects.get(user=self.user)

    def test_flight_lis_as_non_auth_user(self):
        request = self.factory.get('/flight/flights/')
        response = FlightView.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'reservation')
        self.assertEqual(len(response.data), 0)


    def test_flight_list_as_staff_user(self):
        request = self.factory.get('/flight/flights/', HTTP_AUTHORİZATİON=f'Token {self.token}')
        self.user.is_staff = True
        self.user.save()
        force_authenticate(request, user=self.user)
        request.user = self.user
        response = FlightView.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'reservation')
        self.assertEqual(len(response.data), 1)