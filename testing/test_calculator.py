from app.calculator import suma, resta, multiplicacion, division
from app.validarNumero import obtener_numero_positivo

def test_suma_decimales():
    assert suma(24.30, 52.80) == 77.10
    assert suma(48.652, 24.3245) == 72.9765
    
def test_resta_enteros():
    assert resta(15, 7) == 8
    assert resta(24, 76) == -52

def test_division_por_cero():
    '''Prueba que la función division lance un ValueError al intentar dividir por cero.'''
    try:
        division(35, 0)
        assert False, "Expected ValueError"
    except ValueError:
        pass

    try:
        division(55.75, 0)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_validacion_numero_positivo():
    '''Prueba que la función obtener_numero_positivo lance un ValueError para números negativos.
    '''
    try:
        obtener_numero_positivo(-1)
        assert False, "Expected ValueError"
    except ValueError:
        pass

    try:
        obtener_numero_positivo(-0.1)
        assert False, "Expected ValueError"
    except ValueError:
        pass