
'''
    Desarrollado por: Ferney Vanegas Hernández
    Misión TIC 2022
    Versión : 1.0.2
    Título: Reto 5
'''
import modules.libs.game_walls as w
import modules.creatures as c
import modules.repositories.repo_alias_player as alias
import modules.player as p
import modules.render as r

def main():
    # Se obtienen:
    # dim: dimensión del tablero
    # pos: cantidad de muros
    # walls: las coordenadas de las murallas
    dim, pos, walls = w.get_walls()

    # Diccionario general de todas las coordenadas del juego ocupadas
    general_coords={
        'dim' : dim,
        'walls' : walls,
        'coords' : walls.copy()
    } 
    creatures = c.creatures() # Lista con critaturas y símbolos

    dim_creatures, general_coords = c.dim_creatures(creatures, general_coords)

    player, general_coords = p.dim_player(alias.emul_alias_player(), general_coords)
    
    # print(walls)
    # print(creatures)
    # print(dim_creatures)
    # print(general_coords)
    # print(player)

    game_params = general_coords
    game_params['creatures'] = dim_creatures
    game_params['player'] = player

    # Renderizar el juego
    r.construct_game(game_params)

    # Renderizar estadísticas de juego
    r.info_panel(pos, game_params)


main()
