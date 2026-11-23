# Built-In ExceptionGroup
def wrapping():
    errs = [OSError("oserror occurred"), SystemError("system error occurred")]
    raise ExceptionGroup("There were problems", errs)

# Using it
try:
    wrapping()
except Exception as err:
    print(f"Caught {type(err)} due to err")
except* SystemError as eg:
    print("Handing SystemError only", eg.exceptions)