class AgeTooSmallError(Exception):
    def __init__(self, age, threshold=18):
        self.age = age
        self.threshold = threshold
        message = f"Age {age} is below the allowed threshold of {threshold}"
        super().__init__(message)

class AgeTooLargeError(Exception):
    def __init__(self, age, threshold=120):
        self.age = age
        self.threshold = threshold
        message = f"Age {age} is above the allowed threshold of {threshold}"
        super().__init__(message)

def check_age(age):
    if age < 18:
        raise AgeTooSmallError(age)
    if age > 120:
        raise AgeTooLargeError(age)
    print("Access granted")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except AgeTooSmallError as err:
    print(f"Custom exception caught {err}")
except AgeTooLargeError as err:
    print(f"Custom exception caught {err}")
except ValueError:
    print("Error, you have to enter a number")
finally:
    print("Code processing finished!")