from itertools import (
    compress,
    starmap,
    tee,
    product)

from functools import (
    reduce,
    wraps)

from toolz.sandbox.core import unzip

from .trampolin import trampoline, R
from .lambdas import F, shortcut as _

from toolz import *


def iif(true_or_false, if_true, if_false):
    ''' I really dont like pythons inline if syntax'''
    return if_true if true_or_false else if_false


@curry
def is_a(type_name, obj):
    return type(obj) == type_name


def all_fn(*funcs):
    def inner(*args, **kwargs):
        return all(f(*args, **kwargs) for f in funcs)
    
    return inner


def any_fn(*funcs):
    def inner(*args, **kwargs):
        return any(f(*args, **kwargs) for f in funcs)

    return inner
