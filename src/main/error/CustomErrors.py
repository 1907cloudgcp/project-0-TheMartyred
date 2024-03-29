class DataAccessError(Exception):
    """raised when data could not be accessed
Likely the result of improperly formatted data"""
    pass

class UserNotFoundError(Exception):
    """raised if a user is searched for in the
data and not found"""
    pass

class InvalidMoneyError(Exception):
    """raised if a user attempts to deposit
or withdraw a negative or otherwise invalid amount"""
    pass

class NegativeBalanceError(Exception):
    """raised if a transaction would cause
a user to drop below 0 balance."""
    pass

class InvalidPasswordError(Exception):
    """raised if the provided password contains
characters that are reserved as delimiters for
saving data"""
    pass
