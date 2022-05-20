import random

def get_widths(dim, pos):
    '''
    Parameters:
    dim: int
        La dimensión del tablero
    pos: int
        La cantidad de posiciones(cantidad de muros)
    ----------
    Return:
    ----------
    widths: list
        Listado de referencias a anchos de fila
    '''
    widths = []
    for i in range(pos):
        widths.append(random.randint(0,dim))

    # Para probar el ejemplo, debes dimensionar en 32x32 al inicio del programa con 4 posiciones
    # Descomenta la línea siguiente para probar el ejemplo proporcionado en la documentación
    # widths = [2,9,1,4]
    return widths