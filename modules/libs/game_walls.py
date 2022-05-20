'''
    Desarrollado por: Ferney Vanegas Hernández
    Misión TIC 2022
    Versión : 1.0.2
'''

import modules.libs.modules.rows as r
import modules.libs.modules.columns as c
import modules.libs.modules.widhts as w
import modules.libs.modules.longs as l
import modules.libs.modules.walls as wall

def get_walls():
    '''
        En la versión anterior se solicitaba un número de 
        dimensiones para el juego. En esta versión asigna el
        número 50 (50 x 50) en forma predeterminada, para
        que puedan caber el tope de criaturas.

        Sin embargo, si se desea maniobrar con dimensiones diferentes, sírvase descomentar la línea 23 y comentar
        la línea 24
    '''
    # dim = int(input('Ingresa un número para dimensionar el tablero (cuadrado Dim x Dim).Ej:2 (Para crear un tablero de 2x2\n'))
    dim = 50
    pos = int(input('Ingresa por favor las posiciones (ó cantidad de muros) que deseas implementar(Ej: 4)\n'))
    # OBTENCIÓN DE LISTAS BASE
    # ============================
    # Cuando paso a dim como parámetros, le resto uno por la forma en la que se generan aleatorios en las funciones
    rows = r.get_rows(dim - 1, pos)
    columns = c.get_columns(dim - 1, pos)
    widths = w.get_widths(dim - 1, pos)
    longs = l.get_longs(dim - 1, pos)
    # ============================

    # OBTENCIÓN DE COORDENADAS
    coord_walls = wall.get_coord_walls(rows,columns, widths, longs, dim - 1)

    return dim, pos, coord_walls