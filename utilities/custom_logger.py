import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.info("root")
        logging.basicConfig(
            level=logging.INFO,
            filename=".//logs//automation.log",
            filemode="w",
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def loggen_error():
        logging.info("root")
        logging.basicConfig(
            level=logging.ERROR,
            filename=".//logs//automation.log",
            filemode="w",
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.ERROR)
        return logger
