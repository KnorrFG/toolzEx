from collections import namedtuple
from functools import reduce, wraps
from itertools import combinations, compress, product, starmap, tee
from typing import Iterable as _Iterable

from overload import overload
from pyrsistent import (PClass, PRecord, discard, field, freeze, inc, m, ny,
                        pmap, pmap_field, pset, pset_field, pvector,
                        pvector_field, rex, s, thaw, v)
from toolz import *
from toolz.curried import get as cget
from toolz.curried import map as cmap
from toolz.curried import pluck as cpluck
from toolz.curried import valmap as cvalmap
from toolz.curried import do as cdo
from toolz.sandbox.core import unzip

from .trampolin import R, trampoline


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


def all_same(c: _Iterable) -> bool:
    f = first(c)
    return all(x == f for x in c)


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
lunique = compose(list, unique)


clmap = curry(lmap)
clpluck = curry(lpluck)
