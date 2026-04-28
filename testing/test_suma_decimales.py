from app.calculator import suma

def test_suma_decimales():
    assert suma(24.30, 52.80) == 77.10
    assert suma(48.652, 24.3245) == 72.9765
 