from toolzEx import trampoline, R

import sys

@trampoline
def fac(n, acc=1):
    if n == 0:
        return acc
    else:
        return R(n - 1, acc * n)


def test_trampline():
    fac(sys.getrecursionlimit() + 1)
