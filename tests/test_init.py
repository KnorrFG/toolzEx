from toolzEx import is_a, all_fn, any_fn, _, F, iif

def test_all_fn():
    less_than_ten = all_fn(is_a(int), _ < 10)
    assert less_than_ten(9)
    assert not less_than_ten("9")
    assert not less_than_ten(10)


def test_any_fn():
    port_or_str = any_fn(is_a(str), all_fn(is_a(int), F('len(str(%)) == 5')))
    assert port_or_str(45345)
    assert port_or_str('foobarbar')
    assert not port_or_str(4.5)


def test_iif():
    x = iif(10 < 3,
            None,
            '10 is smaller than 3')
    assert type(x) == str
