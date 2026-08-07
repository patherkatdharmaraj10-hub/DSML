from abc import ABC, abstractmethod
from exceptions import InvalidRatingError


class Vehicle(ABC):

    def __init__(self, driver_name, rating):
        self.driver_name = driver_name
        self.rating = rating

# property
    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value < 1 or value > 5:
            raise InvalidRatingError("Rating must be between 1 and 5.")
        self.__rating = value


    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bike(Vehicle):
    BASE_FARE = 20
    PER_KM = 10

    def calculate_fare(self, distance):
        return self.BASE_FARE + (distance * self.PER_KM)


class Car(Vehicle):
    BASE_FARE = 60
    PER_KM = 20


    def calculate_fare(self, distance):
        return self.BASE_FARE + (distance * self.PER_KM)
        
        