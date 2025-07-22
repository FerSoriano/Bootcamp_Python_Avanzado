
"""Creamos excepcines personalizadas"""


class UsernameException(Exception):
    """El usuario no debe de ser 'admin'"""
    def __init__(self):
        self.message = "El usuario no debe de ser 'admin'"
        super().__init__(self.message)


class UsernameLenException(Exception):
    """El usuario debe ser mayor a 6 caracteres"""
    def __init__(self, username):
        self.message = f'El usuario: {username} debe ser mayor a 6 caracteres.'
        super().__init__(self.message)
