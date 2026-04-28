from app.resources import obtener_numero_positivo

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