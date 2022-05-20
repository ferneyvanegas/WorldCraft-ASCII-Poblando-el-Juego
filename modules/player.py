# Importaciones de Python
from datetime import datetime
import random
# Importaciones locales
from modules.libs.modules.walls import count_duplicate_list

def dim_player(alias, general_coords):
    '''
    Parameters:
    ----------
    alias: str
        Un String con un Alias
    general_coords: dict
        Un diccionario con todas las coordenadas de juego usadas al momento. 
        Se precisa para no asignar al jugador en coordenadas ya ocupadas
    ----------
    Return:
    ----------
    data_player: dict
        Un Diccionario de datos especificos del jugador
    general_coords: list
        Un diccionario con todas las coordenadas de juego actualizadas con la posición del jugador
    '''
    player_hearts = 10
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
    
    data_player = {
        'typ' : 'player',
        'alias' : alias,
        'symbol' : chr(169),
        'row' : coord[0],
        'col' : coord[1],
        'date' : datetime.today().strftime('%d/%m/%Y'),
        'hearts' : player_hearts
    }
    
            
    return data_player, general_coords