import logging
import sys

import flask
from pythonjsonlogger import jsonlogger
import six

LOGGER = logging.getLogger()


def log_init():
    formatter = jsonlogger.JsonFormatter(
        '{"timestamp":%(asctime),"message":%(message),'
        '"function_name":%(funcName),"logger_name":%(name),'
        '"logger_level":%(levelname),"filename":%(filename),'
        '"line_number":%(lineno)'
    )

    logHandler = logging.StreamHandler(sys.stdout)

    logHandler.setFormatter(formatter)

    LOGGER.addHandler(logHandler)
    LOGGER.setLevel(logging.DEBUG)


def logged(func):
    @six.wraps(func)
    def do_logged(*args, **kwargs):
        x_forwarded_for = ""
        if flask.request.headers.getlist("X-Forwarded-For"):
            x_forwarded_for = (
                flask.request.headers.getlist("X-Forwarded-For")[0]
            )
        LOGGER.info(
            "function:%s method:%s remote_addr:%s x-forwarded-for:%s "
            "url:%s" % (
                func.__name__, flask.request.method,
                flask.request.remote_addr, x_forwarded_for, flask.request.url
            )
        )
        return func(*args, **kwargs)
    do_logged.__doc__ = func.__doc__
    do_logged.__name__ = func.__name__
    return do_logged
