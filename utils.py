import logging
import os

def _get_debug_level(level: str):
    level = level.lower()
    if level == "debug":
        return logging.DEBUG
    elif level == "info":
        return logging.INFO
    elif level == "warn":
        return logging.WARN
    elif level == "error":
        return logging.ERROR
    elif level == "crit":
        return logging.CRITICAL

def init_logger(name: str, log_dir = "logs", level="info"):
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)
    
    format_str = "%(asctime)s : %(name)-10s : %(levelname)-8s : %(message)s"
    logging.basicConfig(level=_get_debug_level(level), format=format_str)
    logger = logging.getLogger(name)
    format = logging.Formatter("%(asctime)s : %(name)-10s : %(levelname)-8s : %(message)s")
    
    error_handler = logging.FileHandler(os.path.join(log_dir, "errors.log"))
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(format)
    logger.addHandler(error_handler)
    
    return logger