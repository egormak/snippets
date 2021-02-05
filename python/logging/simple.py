# Log.py
import logging

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    # 'root': {"level": "INFO", "handlers": ["stream_console"]},

    'loggers': {
        'own_logger': {
            'level': 'INFO',
            'handlers': ['stream_console'],
            'propagate': False,
            'qualname': "own_logger_logs"
        }
    },
    'handlers': {
        'stream_console': {
            'class': 'logging.StreamHandler',
            'formatter': 'logger_formatter',
            "stream": "ext://sys.stdout"
        },
    },
    'formatters': {
        'logger_formatter': {
            'format': '{ '
                      '"time": "%(asctime)s", '
                      '"level": "%(levelname)s", '
                      '"data": {%(message)s} }',
            "datefmt": "%Y-%m-%d %H:%M:%S %z",
            "class": "logging.Formatter"
        },
    }
}

logging.config.dictConfig(LOGGING_CONFIG)

# Main.py
logs = logging.getLogger('own_logger')
