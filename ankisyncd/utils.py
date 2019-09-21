import logging


def get_logger():
    logger = logging.getLogger("ankisyncd")
    logging.basicConfig(level=logging.INFO, format="[%(asctime)s]:%(levelname)s:%(name)s:%(message)s")
    return logger
