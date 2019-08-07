from . import wraps

class R:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


def trampoline(f):
    @wraps(f)
    def inner(*args, **kwargs):
        res = R(*args, **kwargs) 
        while True:
            res = f(*res.args, **res.kwargs)
            if type(res) != R:
                return res

    return inner
