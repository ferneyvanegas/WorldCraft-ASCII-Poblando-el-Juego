def construct_game(game_params):
    '''
    Parameters:
    -----------
    game_params: dict
        Diccionario con:
            dim: la dimensión del mundo
            walls: lista de las coordenadas de los muros
            creatures: lista de los diccionarios de las criaturas
            player: diccionario del jugador
            coords: el listado de todas las coordenadas de las murallas, criaturas y jugador

    -----------
    Return
    -----------
    '''

    # Colores
    '''
        OK = '\033[92m' #GREEN
        WARNING = '\033[93m' #YELLOW
        FAIL = '\033[91m' #RED
        RESET = '\033[0m' #RESET COLOR
        Fuente: https://www.delftstack.com/es/howto/python/python-print-colored-text/
    '''
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'\033[93m                |-|WORLD CRAFT ASCCI|-|\033[0m')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    BRICK = f'\033[0m▀' # Sin color
    # SPACE = f'\033[0m_'
    SPACE = '\033[0m ' # Sin color
    PLAYER=f"\033[0m\033[93m{game_params['player']['symbol']}" # El jugador es de color amarillo
    for i in range(game_params['dim']): # Dimensioń de ancho
        row=f'\033[0m╬'
        for j in range(game_params['dim']):  # Dimensioń de alto
            creature=''

            # Banderas
            # ================================
            wall_exists = False # Se asume que la muralla no Existe
            creature_exists = False # Se asume que la criatura no Existe
            player_exists = False # Se asume que el jugador no Existe
            # ================================

            for coord in game_params['walls']:
                if coord[0] == i and coord[1]==j:
                    wall_exists = True # Si se encuentra la muralla
            
            for coord in game_params['creatures']:
                if coord['row'] == i and coord['col']==j:
                    if coord['typ'] == 'passive':
                        # Criaturas pasivas de color verde
                        creature = f"\033[0m\033[92m{coord['symbol']}"
                    else:
                        # Criaturas hostiles de color rojo
                        creature = f"\033[0m\033[91m{coord['symbol']}"
                    creature_exists = True # Si se encuentra una criatura
            
            if game_params['player']['row'] == i and game_params['player']['col']==j:
                player_exists = True # Si se encuentra el jugador

            if wall_exists == True:
                row+=BRICK
            elif creature_exists == True:
                row+=creature
            elif player_exists == True:
                row+=PLAYER
            else:
                row+=SPACE 

        print(f'\033[0m{row}\033[0m╬')

def info_panel(number_walls, game_params):
    '''
    Parameters:
    -----------
    number_walls: int
        El número de muros creados
    game_params: dict
        Diccionario con:
            dim: la dimensión del mundo
            walls: lista de las coordenadas de los muros
            creatures: lista de los diccionarios de las criaturas
            player: diccionario del jugador
            coords: el listado de todas las coordenadas de las murallas, criaturas y jugador
    -----------
    Return:
    -----------    
    '''
    # Calcular criaturas pasivas y hostiles
    p_creatures = 0
    for creature in game_params['creatures']:
        if creature['typ'] == 'passive':
            p_creatures+=1

    PLAYER=f"\033[0m\033[93m{game_params['player']['symbol']}" # El jugador es de color amarillo
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('====================================================')
    print(f'* Total de muros: {number_walls}')
    print(f'* Vidas de \033[93m{game_params["player"]["alias"]} {PLAYER}\033[0m: {game_params["player"]["hearts"]}')
    print(f'* Total Criaturas: {len(game_params["creatures"])}')
    print(f'** \033[0m\033[92mPasivas: {p_creatures}')
    print(f'\033[0m** \033[91mHostiles: {len(game_params["creatures"]) - p_creatures}')
    print('\033[0m====================================================')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')