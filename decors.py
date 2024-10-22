def handle_value_error(datatype):
    """Decorator to handle ValueError by attempting to convert args to the specified datatype."""
    def decorator(f):
        def wrapper(args):
            try:
                return f(args)
            except ValueError:
                try:
                    args = datatype(args)
                except ValueError:
                    args = None  # Handle non-convertible strings and return None
                return f(args)
        return wrapper
    return decorator

def handle_overflow_error(operation):
    """Decorator to handle OverflowError by printing a message and returning None."""
    def decorator(f):
        def wrapper(args):
            try:
                return f(args)
            except OverflowError:
                print("Number too large.")
                return None
        return wrapper
    return decorator

def handle_zerodiv_error(operation):
    """Decorator to handle ZeroDivisionError by checking for division by zero in the operation."""
    def decorator(f):
        def wrapper(args):
            if "/0" in operation:
                try:
                    eval(operation)
                except ZeroDivisionError:
                    print("Zero Division Error")
                    return None
            return f(args)
        return wrapper
    return decorator

def handle_type_error(operation):
    """Decorator to handle TypeError by evaluating the operation and printing a message if a TypeError occurs."""
    def decorator(f):
        def wrapper(args):
            try:
                eval(operation)
            except TypeError:
                print("Type error: An object of an inappropriate type has been passed in the operation.")
                return None
            return f(args)
        return wrapper
    return decorator

def handle_reference_error(var):
    """Decorator to handle ReferenceError by checking if 'var' is defined in the local context of 'f'."""
    def decorator(f):
        def wrapper(*args, **kwargs):
            local_vars = f.__code__.co_varnames  # Get local variable names
            if var not in local_vars:
                print(f"Error: '{var}' is not defined in the function.")
                return None
            return f(*args, **kwargs)
        return wrapper
    return decorator

def handle_index_error():
    """Decorator to handle IndexError by checking if each list is paired with an index and printing a message if an IndexError occurs."""
    def decorator(f):
        def wrapper(*args):
            if len(args) % 2 != 0:
                raise ValueError("Each list must be paired with an index.")
            try:
                f(*args)
            except IndexError:
                print("Index Error: Index number is out of range.")
        return wrapper
    return decorator

def handle_runtime_error():
    """Decorator to handle RuntimeError and print a detailed message."""
    def decorator(f):
        def wrapper(*args):
            try:
                f(*args)
            except RuntimeError:
                print("""
                Runtime Error:
                A runtime error is raised when an error has occurred and
                doesn't fall under any other category of errors.
                """)
        return wrapper
    return decorator

def handle_key_error():
    """Decorator to handle KeyError by checking if each dictionary is paired with a key and printing a message if a KeyError occurs."""
    def decorator(f):
        def wrapper(*args):
            if len(args) % 2 != 0:
                raise InterruptedError("Each dictionary must be accompanied by its key indexation value.")
            try:
                f(*args)
            except KeyError:
                print("Key Error: Key value in dictionary not found.")
        return wrapper
    return decorator

def handle_nameError():
    """Decorator to handle NameError by checking if a variable is defined in the local context of 'f' and printing a message if a NameError occurs."""
    def decorator(f):
        def wrapper(*args):
            try : 
                f(*args)
            except NameError:
                print("Name Error : a variable in your code is not defined , to fix this you can either create a variable with the same name or , call a variable from outside the fuction , or name it as an argument in your function.")
        return wrapper
    return decorator