
class UsernameException(Exception):
    def __init__(self):
        super().__init__('Error al crear el usuario')

    def is_valid_to_raise(self):
        return len(self.__notes__) > 0

    def show_notes(self):
        for note in self.__notes__:
            print('>>> ', note)


def valid_username(user: str) -> bool:

    username_error = UsernameException()

    if len(user) < 8:
        username_error.add_note(f'Usuario {user} invalido. La longitud debe ser mayor a 8')  # noqa

    if user.lower() == 'admin':
        username_error.add_note(f'Usuario {user} invalido. No puede llamarse "admin"')  # noqa

    if '@' in user:
        username_error.add_note(f'Usuario {user} invalido. No puede contener el signo "@"')  # noqa

    if username_error.is_valid_to_raise():
        raise username_error

    return True


try:
    username = '@dmin'
    valid_username(username)

except UsernameException as error:
    print(error)
    error.show_notes()
