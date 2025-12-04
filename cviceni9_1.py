def prevod_c_na_f(stupne):
    return stupne * 9 / 5 + 32


def test_prevoc_c_na_f():
    assert prevod_c_na_f(0) == 32
    assert prevod_c_na_f(100) == 212