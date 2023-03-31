from django.db import models

# Create your models here.


class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    operation_airlines = models.CharField(max_length=15)
    departure_city = models.CharField(max_length=30)
    arrival_city = models.CharField(max_length=30)
    date_of_deparature = models.DateField()
    etd = models.TimeField

    def __str__(self):
        return f'{self.flight_number} - {self.departure_city} - {self.arrival_city}'
    
class Passenger(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
