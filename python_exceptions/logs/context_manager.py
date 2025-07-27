"""
- Con esta mejora y refactorizacion, podemos tener un codigo mas Pythonico
- Usamos contextlib para agregar contexto a las excepciones.
- Con esto no es necesario usar bloques de Try Catch cada que validemos
un bloque de codigo
"""

import logging
import traceback
import contextlib

logging.basicConfig(
    level=logging.ERROR,
    filename='errors_2.log',
    format='%(asctime)s:%(levelname)s:%(message)s'
)


@contextlib.contextmanager
def write_on_log_error():
    try:
        yield  # actua como placeholder para reemplazar lo del bloque with

    except Exception as error:
        exception_info = {
            "message": str(error),
            "detail": traceback.format_exc()
        }
        logging.error(exception_info)
        print("Ocurrio un error, revisa el LOG") # linea solo para test


with write_on_log_error():
    a = 10 / 0
    print(a)

with write_on_log_error():
    raise Exception("Se perdio la conexion a la Base de Datos")

with write_on_log_error():
    file = open('test.txt')


username: str = 'Fer'
format: bool = True