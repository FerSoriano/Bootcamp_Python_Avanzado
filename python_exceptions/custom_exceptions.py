
from exceptions import UsernameException, UsernameLenException


def valid_username(user):
    if user == 'admin':
        raise UsernameException()

    if len(user) < 6:
        raise UsernameLenException(user)

    print("Funcion ejecutada con exito")


try:
    user = 'adn'
    valid_username(user)
except UsernameException as error:
    print(error)
except UsernameLenException as error:
    print(error)
else:
    print(f'Usuario Correcto: {user}')
finally:
    print('Fin del programa')
