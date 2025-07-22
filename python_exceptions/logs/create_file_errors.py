import logging
import traceback

logging.basicConfig(
    level=logging.ERROR,
    filename='errors.log',
    format='%(asctime)s:%(levelname)s:%(message)s'
)


def write_on_log_error(error, type_error):
    exception_info = {
        "message": str(error),
        "detail": traceback.format_exc()
    }
    if type_error == 'error':
        logging.error(exception_info)
    if type_error == 'critical':
        logging.critical(exception_info)

    print("Ocurrio un error, revisa el LOG")


try:
    a = 10 / 1
except Exception as error:
    write_on_log_error(error, "error")

try:
    raise Exception("Se perdio la conexion a la Base de Datos")
except Exception as error:
    write_on_log_error(error, "critical")
