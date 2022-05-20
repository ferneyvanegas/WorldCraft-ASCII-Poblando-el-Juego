# Importaciones de Python
from collections import deque
from datetime import datetime
import random
# Importaciones locales
import modules.repositories.repo_hostile_creatures as hostile
import modules.repositories.repo_passive_creatures as passive
from modules.libs.modules.walls import count_duplicate_list


def create_creatures(cant_p:int, cant_h:int):
    '''
    Parameters:
    -----------
    cant_p: int
        La cantidad de criaturas pasivas a obtener
    cant_h: int
        La cantidad de criaturas hostiles a obtener
    -----------
    Return:
    p_creatures: queue
        Cola con criaturas pasivas
    h_creatures: queue
        Cola con criaturas hostiles
    -----------
    '''
    p_creatures = deque(passive.get_passive_creatures(cant_p))
    h_creatures = deque(hostile.get_hostile_creatures(cant_h))
    return p_creatures, h_creatures

def get_symbols_creatures(cant_p:int, cant_h:int):
    '''
    Parameters:
    -----------
    cant_p: int
        La cantidad de criaturas pasivas a obtener
    cant_h: int
        La cantidad de criaturas hostiles a obtener
    -----------
    Return:
    p_symbols: queue
        Cola con simbolos de criaturas pasivas
    h_symbols: queue
        Cola con simbolos de criaturas hostiles
    -----------
    '''
    
    # =========================================
    '''
        Los primeros 50 códigos ascii, desde el 33 serán
        para criaturas pasivas. 
        Del 84 en adelante para criaturas hostiles
    '''
    ascii = 33 # Código ASCII

    p_symbols = []
    h_symbols = []

    for i in range(cant_p):
        p_symbols.append(chr(ascii))
        ascii+=1
    
    ascii = 84
    for i in range(cant_h):
        h_symbols.append(chr(ascii))
        ascii+=1

    return deque(p_symbols), deque(h_symbols)

def creatures():
    '''
    Parameters:
    -----------
    Return:
    -----------
    : file
        Una Fila con 4 colas.
            Cola 1: cantidad x de criaturas pasivas
            Cola 2: cantidad x de criaturas hotiles
            Cola 3: cantidad x de symbolos para criaturas pasivas
            Cola 4: cantidad x de symbolos para criaturas hotiles
    '''
    # El valor inicial es 50 apropósito para cumplir la condición de entrar al while
    cant_p = '50'
    cant_h = '50'
    while not cant_p.isdigit() or not cant_h.isdigit() or int(cant_p) + int(cant_h) > 50 or int(cant_p) <= 0 or int(cant_h) <= 0:
        print('*********CREACION DE CRIATURAS*********\n')
        print('(No pueden ser más de 50 en total)\n')
        cant_p = input('Ingresa el número de criaturas pasivas(Mayor que cero)\n->')
        cant_h = input('Ingresa el número de criaturas hostiles(Mayor que cero)\n->')
        print('***************************************\n')
    # Se obtienen las colas con las criaturas
    p_creatures, h_creatures = create_creatures(int(cant_p), int(cant_h))
    # Ahora se deben obtener los símbolos de las criaturas
    p_symbols, h_symbols = get_symbols_creatures(int(cant_p), int(cant_h))
    return [p_creatures, h_creatures, p_symbols, h_symbols]

def dim_creatures(creatures, general_coords):
    '''
    Parameters:
    ----------
    creatures: list
        Un listado con todas las criaturas pasivas, hostiles y sus respectivos símbolos
    general_coords: dict
        Un diccionario con todas las coordenadas de juego usadas al momento. 
        Se precisa para no asignar criaturas en coordenadas ya ocupadas
    ----------
    Return:
    ----------
    dim_creatures: list
        Un listado con Diccionarios de datos especificos por criatura
    general_coords: list
        Un diccionario con todas las coordenadas de juego actualizadas con las posiciones de las criaturas. 
    '''
    dim_creatures = []
    for i in range(2):
        cant_creatures = len(creatures[i])
        # i = 0 : Criaturas Pasivas
        # i = 1 : Criaturas Hostiles
        if i == 0:
            typ = 'passive'
        else:
            typ = 'hostile'

        # Revisión de criatura por criatura
        for j in range(cant_creatures):
            coord = [0,0]
            coord_inserted = False # Bandera
            # Selección de una coordenada correcta, en los rangos y no existente
            while coord_inserted == False:
                coord[0] = random.randint(0,general_coords['dim'] - 1)
                coord[1] = random.randint(0,general_coords['dim'] - 1)
                # count_duplicate_list es una función que se usó en el taller anterior
                # Basicamente indica si una coordenada ya está usada
                if count_duplicate_list(coord, general_coords['coords']) == 0:
                    general_coords['coords'].append(coord)
                    coord_inserted = True
            
            creature_data = {
                'typ' : typ,
                'name' : creatures[i][0],
                'symbol' : creatures[i+2][0],
                'row' : coord[0],
                'col' : coord[1],
                'date' : datetime.today().strftime('%d/%m/%Y')
            }
            
            '''
                En medida que se van revisando la primer criatura ingresada, se va
                retirando de la cola (FIFO)
            '''
            creatures[i].popleft() 
            creatures[i+2].popleft() 

            # Se agrega diccionario de criatura a listado
            dim_creatures.append(creature_data)
            
    return dim_creatures, general_coords