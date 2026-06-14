#The logger utility centralizes logging configuration for the framework. Instead of configuring logging in every test file, I created a reusable logger that records execution details to both the console and log files, making debugging and test analysis easier.
import logging #used for logging
import os #used for path and folder creation
from logging.handlers import RotatingFileHandler
#RotatingFileHandler-Automatically creates new files. because huge files not practical
def get_logger(name= __name__):
    logger = logging.getLogger(name) #create logger (give me a logger with this name)

    if not logger.handlers: #prevents duplicate logs, only configure login once
        logger.setLevel(logging.DEBUG)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_dir = os.path.join(project_root, "reports", "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_file_path = os.path.join(log_dir, "test_log.log")
    #handlers
        console_handler = logging.StreamHandler()
        file_handler = RotatingFileHandler(log_file_path, maxBytes=3000000, backupCount=3)
    #formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(message)s')

        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

    #adding handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger