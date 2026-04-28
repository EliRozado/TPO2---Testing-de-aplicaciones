from app.calculator import division

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