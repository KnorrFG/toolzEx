from toolzEx import F, _

def test_f():
    assert F('len(%1)')(1, [1, 2, 3]) == 3
    assert F('15 %% %')(4) == 3


def test_underscore():
    assert (_ + 3)(4) == 7
    assert (_ < 5)(4) == True
