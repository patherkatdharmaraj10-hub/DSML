class InvalidRatingError(Exception):
    """Raised error when rating is not between 1 and 5"""
    pass

class NegativeDistanceError(Exception):
    """Raised error when distance is negative"""
    pass

class RideHistoryError(Exception):
    """Raised error when ride history is empty"""
    pass
