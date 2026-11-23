# Custom Exception
class AgeTooSmallError(Exception):
    """Exception raised when the input age is below the allowed threshold"""
    def __init__(self, age, threshold=18):
        self.age = age
        self.threshold = threshold
        message = f"Age {age} is below the allowed threshold of {threshold}"
        super().__init__(message)

def check_age(age):
    """Checks if the age meets the minimum requirement"""
    if age < 18:
        raise AgeTooSmallError(age)
print("Access granted")

# Example usage
try:
    check_age(17)
except AgeTooSmallError as err:
    print(f"Custom exception caught {err}")