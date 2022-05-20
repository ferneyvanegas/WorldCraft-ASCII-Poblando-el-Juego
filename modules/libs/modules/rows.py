import random

def get_rows(dim, pos):
    '''
    Parameters:
    dim: int
        La dimensión del tablero
    pos: int
        La cantidad de posiciones(cantidad de muros)
    ----------
    Return:
    ----------
    rows: list
        Listado de referencias a filas
    '''
    rows = []
    for i in range(pos):
        rows.append(random.randint(0,dim))

    # Para probar el ejemplo, debes dimensionar en 32x32 al inicio del programa con 4 posiciones
    # Descomenta la línea siguiente para probar el ejemplo proporcionado en la documentación
    # rows = [0,3,5,6]
    return rows