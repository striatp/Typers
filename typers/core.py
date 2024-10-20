from .Exceptions.validate_error import ValidateError

class Valid:
    @staticmethod
    def _string(value, name: str = None):
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, str):
            raise ValueError(f"The '{name}' argument must be a string.")

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
    @staticmethod
    def _float(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float):
            raise ValueError(f"The '{name}' argument must be a float.")

    @staticmethod
    def _positive_float(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float) or value <= 0:
            raise ValueError(f"The '{name}' argument must be a positive float.")

    @staticmethod
    def _negative_float(value, name: str = None):
        if name is None:
            raise ValidateError("The 'name' argument must be a string.")
        if not isinstance(value, float) or value >= 0:
            raise ValueError(f"The '{name}' argument must be a negative float.")
