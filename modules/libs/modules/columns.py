import random

def get_columns(dim, pos):
    '''
    Parameters:
    dim: int
        La dimensión del tablero
    pos: int
        La cantidad de posiciones(cantidad de muros)
    ----------
    Return:
    ----------
    columns: list
        Listado de referencias a columnas
    '''
    columns = []
    for i in range(pos):
        columns.append(random.randint(0,dim))

    # Para probar el ejemplo, debes dimensionar en 32x32 al inicio del programa con 4 posiciones
    # Descomenta la línea siguiente para probar el ejemplo proporcionado en la documentación
    # columns = [1,3,11,12]
    return columns