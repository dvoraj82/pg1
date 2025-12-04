from muj_modul import fibonaci



def test_fibonaci():
    assert fibonaci(2) == [1, 1, 2]
    assert fibonaci(10) == [1, 1, 2, 3, 5, 8]