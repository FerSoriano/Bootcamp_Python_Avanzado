import logging

"""
INFO        10
DEBUG       20
WARNING     30
ERROR       40
CRITICAL    50
"""

logging.basicConfig(level=logging.ERROR)

logging.info('Mensaje Informativo')
logging.debug('Mensaje Informativo')
logging.warning('Mensaje Informativo')
logging.error('Mensaje Informativo')
logging.critical('Mensaje CRITICO')
