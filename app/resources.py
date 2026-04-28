def obtener_numero_positivo(numero):
    """Valida que el usuario ingrese un número positivo."""
    if numero < 0:
        raise ValueError("Error: Solo se aceptan números positivos.")   
    return numero
