from functools import wraps

def ride_logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("\nRide booked successfully!")
        return result

    return wrapper
