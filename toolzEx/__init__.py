from itertools import (
    compress,
    starmap,
    tee,
    product,
    combinations)

from functools import (
    reduce,
    wraps)

from collections import namedtuple

from toolz.sandbox.core import unzip

from .trampolin import trampoline, R

from toolz import *

from overload import overload

from pyrsistent import (
        v, pvector, m, pmap, s, pset, 
        PRecord, field, pset_field, pmap_field, pvector_field,
        PClass, freeze, thaw, ny, discard, inc, rex)
 

class LazyList:
    """Returns elements from the iterator and stores them, so they can be
    reused without using the iterator. """
    __slots__ = ("_buffer", "_iter")
    def __init__(self, seq):
        self._buffer = []
        self._iter = iter(seq)

    def __getitem__(self, idx):
        if len(self._buffer) <= idx:
            self._buffer.extend(take(idx - len(self._buffer) + 1, self._iter))
        return self._buffer[idx]


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


def breaker(func):
    @wraps
    def inner(*args, **kwargs):
        breakpoint()
        return func(*args, **kwargs)
    return inner


lmap = compose(list, map)
lfilter = compose(list, filter)
lconcat = compose(list, concat)
ltake = compose(list, take)
lpluck = compose(list, pluck)
lcompress = compose(list, compress)
lmapcat = compose(list, mapcat)
lstarmap = compose(list, starmap)
