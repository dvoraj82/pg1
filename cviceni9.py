def nejvetsi(seznam_cisel):
    if not seznam_cisel:
        return None
    return max(seznam_cisel)

def test_nejvetsi():
    assert nejvetsi([1, 2, 3, 4, 5]) == 5
    assert nejvetsi([-1, -2, -3, -4, -5]) == -1
    assert nejvetsi([0]) == 0
    assert nejvetsi([]) == None
