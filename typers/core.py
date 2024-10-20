from .Exceptions.validate_error import ValidateError

class Valid:
    # Not none
    @staticmethod
    def _not_none(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if value is None:
            raise ValueError(f"The '{name}' argument cannot be None.")

    # String
    @staticmethod
    def _string(value, name: str = None):
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, str):
            raise ValueError(f"The '{name}' argument must be a string.")

    # Integers
    @staticmethod
    def _integer(value, name: str = None):
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, int):
            raise ValueError(f"The '{name}' argument must be an integer.")

    @staticmethod
    def _positive_int_in(value, name: str = None):
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"The '{name}' argument must be a positive integer.")

    @staticmethod
    def _positive_int_out(value, name: str = None):
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"The '{name}' argument must be a positive integer excluding 0.")


    @staticmethod
    def _negative_int_in(value, name: str = None):
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, int) or value >= 0:
            raise ValueError(f"The '{name}' argument must be a negative integer.")

    @staticmethod
    def _negative_int_out(value, name: str = None):
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, int) or value > 0:
            raise ValueError(f"The '{name}' argument must be a negative integer excluding 0.")

    # Floats
    @staticmethod
    def _float(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float):
            raise ValueError(f"The '{name}' argument must be a float.")

    @staticmethod
    def _positive_float_in(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float) or value <= 0:
            raise ValueError(f"The '{name}' argument must be a positive float.")

    @staticmethod
    def _positive_float_out(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float) or value < 0:
            raise ValueError(f"The '{name}' argument must be a positive float excluding 0.")

    @staticmethod
    def _negative_float_in(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float) or value >= 0:
            raise ValueError(f"The '{name}' argument must be a negative float.")

    @staticmethod
    def _negative_float_out(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float) or value > 0:
            raise ValueError(f"The '{name}' argument must be a negative float excluding 0.")

    # Booleans
    @staticmethod
    def _boolean(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, bool):
            raise ValueError(f"The '{name}' argument must be a boolean.")

    # Lists
    @staticmethod
    def _list(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list):
            raise ValueError(f"The '{name}' argument must be a list.")

    @staticmethod
    def _list_of_strings(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            raise ValueError(f"The '{name}' argument must be a list of strings.")
    
    @staticmethod
    def _list_of_ints(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list) or not all(isinstance(item, int) for item in value):
            raise ValueError(f"The '{name}' argument must be a list of integers.")

    @staticmethod
    def _list_of_floats(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list) or not all(isinstance(item, float) for item in value):
            raise ValueError(f"The '{name}' argument must be a list of floats.")

    @staticmethod
    def _list_of_bools(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list) or not all(isinstance(item, bool) for item in value):
            raise ValueError(f"The '{name}' argument must be a list of booleans.")
    
    # Ranges
    @staticmethod
    def _in_range(value, min_val, max_val, name: str = None):
        if min_val >= max_val:
            raise ValidateError("The 'min_val' argument cannot be bigger or equal to the 'max_val' argument.")
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, (int, float)) or not (min_val <= value <= max_val):
            raise ValueError(f"The '{name}' argument must be between {min_val} and {max_val}.")

    # Tuples
    @staticmethod
    def _tuple(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, tuple):
            raise ValueError(f"The '{name}' argument must be a tuple.")

    @staticmethod
    def _tuple_of_strings(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, tuple) or not all(isinstance(item, str) for item in value):
            raise ValueError(f"The '{name}' argument must be a tuple of strings.")

    @staticmethod
    def _tuple_of_ints(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, tuple) or not all(isinstance(item, int) for item in value):
            raise ValueError(f"The '{name}' argument must be a tuple of integers.")

    @staticmethod
    def _tuple_of_floats(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, tuple) or not all(isinstance(item, float) for item in value):
            raise ValueError(f"The '{name}' argument must be a tuple of floats.")

    @staticmethod
    def _tuple_of_bools(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, tuple) or not all(isinstance(item, bool) for item in value):
            raise ValueError(f"The '{name}' argument must be a tuple of booleans.")

    # Sets
    @staticmethod
    def _set(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, set):
            raise ValueError(f"The '{name}' argument must be a set.")
    
    @staticmethod
    def _set_of_strings(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, set) or not all(isinstance(item, string) for item in value):
            raise ValueError(f"The '{name}' argument must be a set of strings.")

    @staticmethod
    def _set_of_ints(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, set) or not all(isinstance(item, int) for item in value):
            raise ValueError(f"The '{name}' argument must be a set of integers.")

    @staticmethod
    def _set_of_floats(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, set) or not all(isinstance(item, float) for item in value):
            raise ValueError(f"The '{name}' argument must be a set of floats.")

    @staticmethod
    def _set_of_bools(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, set) or not all(isinstance(item, bool) for item in value):
            raise ValueError(f"The '{name}' argument must be a set of booleans.")

    # Dictionary
    @staticmethod
    def _dict(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, dict):
            raise ValueError(f"The '{name}' argument must be a dictionary.")

    @staticmethod
    def _dict_of_strings(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in value.items()):
            raise ValueError(f"The '{name}' argument must be a dictionary of string keys and values.")
  
    # Length
    @staticmethod
    def _length(value, expected_length, name: str = None):
        if excepted_length < 0:
            raise ValidateError("The 'excepted_length' argument must be a positive integer.")
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not hasattr(value, '__len__') or len(value) != expected_length:
            raise ValueError(f"The '{name}' argument must have a length of {expected_length}.")

    # Types (custom)
    @staticmethod
    def _type(value, expected_type, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, expected_type):
            raise ValueError(f"The '{name}' argument must be of type {expected_type.__name__}.")

    # Optional
    @staticmethod
    def _optional(value, expected_type, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if value is not None and not isinstance(value, expected_type):
            raise ValueError(f"The '{name}' argument must be None or of type {expected_type.__name__}.")

    # Enum
    @staticmethod
    def _enum(value, options, name: str = None):
        if not isinstance(options, list) or len(options) == 0:
            raise ValidateError("The 'options' argument must be a list.")
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if value not in options:
            raise ValueError(f"The '{name}' argument must be one of {options}.")

    # Non-empty string
    @staticmethod
    def _non_empty_string(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"The '{name}' argument must be a non-empty string.")

    # Non-empty list
    @staticmethod
    def _non_empty_list(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, list) or len(value) == 0:
            raise ValueError(f"The '{name}' argument must be a non-empty list.")
