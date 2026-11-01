from logger import logging


def add(a: int, b: int) -> int:
    logging.debug("The addition operation is taking place.")
    return a + b


logging.debug("The addition operation is called.")
add(10, 15)
