from vehicles import Bike, Car
from decorators import ride_logger
from exceptions import (
    InvalidRatingError,
    NegativeDistanceError, 
    RideHistoryError
)

@ride_logger
def book_ride(vehicle, distance):
    fare  = vehicle.calculate_fare(distance)

    try:

        with open("ride_history.txt", "a") as file:
            file.write(
                f"Driver: {vehicle.driver_name},"
                f"Vehicle: {vehicle.__class__.__name__},"
                f"Distance: {distance} km,"
                f"Fare:{fare}\n"

                       )

    except Exception as e:
        raise RideHistoryError("Unable to write history to history file")

    print("\nDriver :", vehicle.driver_name)
    print("Vehicle :", vehicle.__class__.__name__)
    print("Distance:", distance, "km")  
    print("Fare: Rs.", fare)                 



def main():

    try:
        vehicle_type = input("Enter vehicle type (Bike/Car):").strip().lower()
        driver = input("Enter Driver name:")
        rating = float(input("Enter Driver rating: "))
        distance = float(input("Enter distance in km:"))

        if distance < 0:
            raise NegativeDistanceError("Distance cannot be negative.")

        if vehicle_type == "bike":
            vehicle = Bike(driver, rating)

        elif vehicle_type == "car":
            vehicle = Car(driver, rating)
        else:
            print("Invalid vehicle type. Please choose either 'Bike' or 'Car'.")
            return
        book_ride(vehicle, distance)

    except InvalidRatingError as e:
        print("Error:", e)

    except NegativeDistanceError as e:
        print("Error:", e)  

    except RideHistoryError as e:
        print("Error:", e)

    except ValueError:
        print("Error: Invalid input. Please enter numeric values for rating and distance.")

    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
        main()

