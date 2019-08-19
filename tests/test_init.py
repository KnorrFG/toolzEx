from toolzEx import is_a, all_fn, any_fn, X, F, LazyList
import time

def test_all_fn():
    less_than_ten = all_fn(is_a(int), X < 10)
    assert less_than_ten(9)
    assert not less_than_ten("9")
    assert not less_than_ten(10)


def test_any_fn():
    port_or_str = any_fn(is_a(str), all_fn(is_a(int), F('len(str(%)) == 5')))
    assert port_or_str(45345)
    assert port_or_str('foobarbar')
    assert not port_or_str(4.5)


def test_lazy_list():
    def slow_count():
        n = 0
        while True:
            time.sleep(1)
            yield n
            n += 1

    seq = LazyList(slow_count())
    start = time.time()
    n = seq[2]
    tp1 = time.time()
    assert tp1 - start >= 3
    assert n == 2
    n = seq[2]
    assert time.time() - tp1 < 0.5


    
            
