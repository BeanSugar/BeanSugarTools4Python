__author__ = 'archmagece'

import time
from functools import wraps


#def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None):
#    """Retry calling the decorated function using an exponential backoff.
#
#    http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
#    original from: http://wiki.python.org/moin/PythonDecoratorLibrary#Retry
#
#    :param ExceptionToCheck: the exception to check. may be a tuple of
#        exceptions to check
#    :type ExceptionToCheck: Exception or tuple
#    :param tries: number of times to try (not retry) before giving up
#    :type tries: int
#    :param delay: initial delay between retries in seconds
#    :type delay: int
#    :param backoff: backoff multiplier e.g. value of 2 will double the delay
#        each retry
#    :type backoff: int
#    :param logger: logger to use. If None, print
#    :type logger: logging.Logger instance
#    """
#    def deco_retry(f):
#        @wraps(f)
#        def f_retry(*args, **kwargs):
#            try_count, delay_time = tries, delay
#            while try_count > 1:
#                try:
#                    return f(*args, **kwargs)
#                except ExceptionToCheck, e:
#                    msg = "%s, Retrying in %d seconds..." % (str(e), delay_time)
#                    if logger:
#                        logger.warning(msg)
#                    else:
#                        print msg
#                    time.sleep(delay_time)
#                    try_count -= 1
#                    delay_time *= backoff
#            return f(*args, **kwargs)
#        return f_retry  # true decorator
#    return deco_retry


def retry(delay=1, backoff=2, maxdelay=300, maxtry=10, log=None):
    def decorator(fn):
        def retrier(*args, **kwargs):
            _delay = delay
            attempt = 0
            while attempt < maxtry:
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    msg = 'Houston, we have a problem [%s]; retrying in %d seconds...' % (str(e), _delay)
                    if log:
                        log.exception(msg)
                    else:
                        print msg
                    time.sleep(_delay)
                    _delay = maxdelay if _delay is maxdelay else min(maxdelay, _delay * backoff)
                    attempt += 1
            raise RuntimeError('ran out of retry count.')
        return retrier
    return decorator