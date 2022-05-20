import random

def get_longs(dim, pos):
    '''
    Parameters:
    dim: int
        La dimensión del tablero
    pos: int
        La cantidad de posiciones(cantidad de muros)
    ----------
    Return:
    ----------
    longs: list
        Listado de referencias a largos de fila
    '''
    longs = []
    for i in range(pos):
        longs.append(random.randint(0,dim))

    # Para probar el ejemplo, debes dimensionar en 32x32 al inicio del programa con 4 posiciones
    # Descomenta la línea siguiente para probar el ejemplo proporcionado en la documentación
    # longs = [5,2,2,1]
    return longs