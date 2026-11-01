import logging

## logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger("ArtihmethicApp")


def add(a: float, b: float) -> float:
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result


def substract(a: float, b: float) -> float:
    result = a - b
    logger.debug(f"Substracting {a} - {b} = {result}")
    return result


def multiply(a: float, b: float) -> float:
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result


def divide(a: float, b: float) -> float | None:
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error.")
        return None


add(10, 15)
substract(15, 10)
multiply(10, 20)
divide(20, 10)
divide(20, 0)
