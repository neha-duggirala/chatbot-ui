import logging

def configure_logger(log_filename):
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    logger = logging.getLogger()

    # Create a file handler
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))

    # Add handlers to the logger
    logger.addHandler(file_handler)

    return logger