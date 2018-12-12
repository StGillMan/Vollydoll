import time

def timeInfo(func):
    """Decorator to track the time 

    Args: func: [function for decorate]
    Returns: [funch]
    """
    def timeRun(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()

        print 'Time: {}'.format(end - start)

        return result

    return timeRun

