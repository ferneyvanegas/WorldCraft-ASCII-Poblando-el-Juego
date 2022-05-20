import random

def get_hostile_creatures(cant:int):
    '''
    Parameters:
    ----------
    cant: int
        La cantidad de criaturas hostiles que entregará del listado existente
    ----------
    Return:
    ----------
    : tuple
        Una tupla con el número de criaturas hostiles escogidas aleatoriamente
    '''
    h_creatures = [
                    "oso_vampiro",
                    "oso_zombie",
                    "oso_hechicero",
                    "oso_momia",
                    "oso_duende",
                    "oso_mounstro",
                    "oso_sayayin",
                    "oso_fantasma",
                    "oso_pirata",
                    "oso_diablo",
                    "perro_vampiro",
                    "perro_zombie",
                    "perro_hechicero",
                    "perro_momia",
                    "perro_duende",
                    "perro_mounstro",
                    "perro_sayayin",
                    "perro_fantasma",
                    "perro_pirata",
                    "perro_diablo", 
                    "gato_vampiro",
                    "gato_zombie",
                    "gato_hechicero",
                    "gato_momia",
                    "gato_duende",
                    "gato_mounstro",
                    "gato_sayayin",
                    "gato_fantasma",
                    "gato_pirata",
                    "gato_diablo",
                    "pajarraco_vampiro",
                    "pajarraco_zombie",
                    "pajarraco_hechicero",
                    "pajarraco_momia",
                    "pajarraco_duende",
                    "pajarraco_mounstro",
                    "pajarraco_sayayin",
                    "pajarraco_fantasma",
                    "pajarraco_pirata",
                    "pajarraco_diablo",  
                    "pato_vampiro",
                    "pato_zombie",
                    "pato_hechicero",
                    "pato_momia",
                    "pato_duende",
                    "pato_mounstro",
                    "pato_sayayin",
                    "pato_fantasma",
                    "pato_pirata",
                    "pato_diablo"
    ]
    random.shuffle(h_creatures)
    return tuple(h_creatures[:cant])