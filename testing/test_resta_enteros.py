from app.calculator import resta

def test_resta_enteros():
    assert resta(15, 7) == 8
    assert resta(24, 76) == -52