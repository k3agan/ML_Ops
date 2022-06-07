from hello import add


def test_add():
    assert add(2, 3) == 5
    assert add(5, 3) == 8
    assert add(2, 2) == 4
    assert add(5, 5) == 10
    assert add(2, -1) == 1
    assert add(-1, 2) == 1
    assert add(-1, -1) == -2
    assert add(-1, -2) == -3
    assert add(-2, -1) == -3
    assert add(-2, -2) == -4
    assert add(-2, -3) == -5
    assert add(-3, -2) == -5
    assert add(-3, -3) == -6
    assert add(-3, -4) == -7
    assert add(-4, -3) == -7
    assert add(-4, -4) == -8
    assert add(-4, -5) == -9
    assert add(-5, -4) == -9
    assert add(-5, -5) == -10
    assert add(-5, -6) == -11
    assert add(-6, -5) == -11
    assert add(-6, -6) == -12
    assert add(-6, -7) == -13
    assert add(-7, -6) == -13
    assert add(-7, -7) == -14
    assert add(-7, -8) == -15
    assert add(-8, -7) == -15
    assert add(-8, -8) == -16
    assert add(-8, -9) == -17
    assert add(-9, -8) == -17
    assert add(-9, -9) == -18
    assert add(-9, -10) == -19
    assert add(-10, -9) == -19
    assert add(-10, -10) == -20
    assert add(-10, -11) == -21
    assert add(-11, -10) == -21
    assert add(-11, -11) == -22
    assert add(-11, -12) == -23
    assert add(-12, -11) == -23
    assert add
