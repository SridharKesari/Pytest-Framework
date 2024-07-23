def test_a1():
    assert 5 < 6
    assert 50 > 20
    assert 100 >= 99
    assert 3 != 9


def test_a2():
    assert 1


def test_a3():
    assert 'abc' == 'abcd'


def test_a4():
    assert (3 - 1) * 4 / 2 == 4.0


def test_a5():
    assert 8 in divmod(60, 7)
    assert 'po' not in 'pytest'
    assert [1, 2] in [[1, 2], 4]
    assert [1, 2] < [1, 2, 3]
