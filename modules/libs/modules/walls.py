# Función para generar coordenadas de construcción de muros en un mapa
def get_coord_walls(rows, columns, widhts, longs, dim):
    '''
    Parameters:
    -----------
    rows: list
        Lista con filas
    columns: list
        Lista con columnas
    widht: list
        Lista con los anchos
    longs: list
        Lista con los largos
    dim: int
        La dimensión del tablero
    -----------
    Return:
    -----------
    coord_walls: list
        Lista con coordenadas
    '''
    coord_walls = []
    '''
        Según la información proporcionada: rows, columns, widhts y longs tienen la misma longitud (En la docu-
        mentación es 4). De modo que con saber la longitud de uno de ellos, se infiere la de los demás.
    '''
    for index in range(len(rows)):
        for i in range(rows[index],(rows[index] + longs[index])):
            for j in range(columns[index], (columns[index] + widhts[index])):
                coord_walls.append([i,j])
    
    '''
        El manejo de números aleatorios podría generar coordenadas que se exeden de las dimensiones
        Esas coordenadas no se dibujarán, pero generan basura en la lista a entregar, de modo que se purgan a continuación:
        1. Para ir eliminando objetos una lista a medida que la voy leyendo, debo hacerlo en forma inversa, ello porque, en este caso,
        voy a ir eliminando elementos y al hacerlo, la longitud de la lista cambiaría.
        2. También podrían haber duplicados; esos también se purgan
    '''
    # Limpiar listado
    for i in range((len(coord_walls)-1), -1, -1): 
        if coord_walls[i][0] > dim or coord_walls[i][1] > dim or count_duplicate_list(coord_walls[i], coord_walls) > 1:
            coord_walls.pop(i)
               
    return coord_walls

# Esta función depura coordenadas duplicadas
def count_duplicate_list(item, elements_list):
    '''
    Paremeters:
    ----------
    item: list
        Una lista para ser comparada
    elements_list: list
        Una lista con varias listas en su interior
    ----------
    Return
    ----------
    cont: int
        El número de veces en los que una lista está en otra lista
    '''
    cont=0
    for i in elements_list:
        if i[0] == item[0] and i[1] == item[1]:
            cont+=1
    return cont


# Función para construir mapas
def construct_walls(coord_walls, dim):
    '''
    Parameters:
    -----------
    coord_walls: lista
        Lista de coordenadas
    dim: int
        La dimensión del tablero
    -----------
    Return
    -----------
    '''
    BRICK = '#'
    SPACE = '_'
    # SPACE = ' ' # Puede ser un espacio
    
    for i in range(dim): # Dimensioń de ancho
        row='[|'
        for j in range(dim):  # Dimensioń de alto
            coord_exist = False # Se asume que la coordenada no Existe
            for coord in coord_walls:
                if coord[0] == i and coord[1]==j:
                    coord_exist = True # Si se encuentra la coordenada
            if coord_exist:
                row+=BRICK
            else:
                row+=SPACE 
        print(f'{row}|]')


    