from .Exceptions.validate_error import ValidateError

class Validate:

    @staticmethod
    def _string(value, name: str = None):
        if name == None:
            raise ValidateError("The 'name' argument must be a string : preferably the name of the relative function.")
        if not isinstance(value, str):
            raise ValueError(f"The '{name}' argument must be a string.)
