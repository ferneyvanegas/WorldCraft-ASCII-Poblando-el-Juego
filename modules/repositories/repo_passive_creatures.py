import random

def get_passive_creatures(cant:int):
    '''
    Parameters:
    ----------
    cant: int
        La cantidad de criaturas pasivas que entregará del listado existente
    ----------
    Return:
    ----------
    : tuple
        Una tupla con el número de criaturas pasivas escogidas aleatoriamente
    '''
    p_creatures = [
                    "mariposa_humilde",
                    "mariposa_amable",
                    "mariposa_amigable",
                    "mariposa_cariñoso",
                    "mariposa_amorosa",
                    "mariposa_valiente",
                    "mariposa_feliz",
                    "mariposa_animada",
                    "mariposa_inmortal",
                    "mariposa_justa",
                    "pony_humilde",
                    "pony_amable",
                    "pony_amigable",
                    "pony_cariñoso",
                    "pony_amoroso",
                    "pony_valiente",
                    "pony_feliz",
                    "pony_animado",
                    "pony_inmortal",
                    "pony_disciplinado",
                    "unicornio_humilde",
                    "unicornio_amable",
                    "unicornio_amigable",
                    "unicornio_cariñoso",
                    "unicornio_amoroso",
                    "unicornio_valiente",
                    "unicornio_feliz",
                    "unicornio_animado",
                    "unicornio_inmortal",
                    "unicornio_justa",
                    "sirena_humilde",
                    "sirena_amable",
                    "sirena_amigable",
                    "sirena_cariñosa",
                    "sirena_amorosa",
                    "sirena_valiente",
                    "sirena_feliz",
                    "sirena_animada",
                    "sirena_inmortal",
                    "sirena_justa",
                    "cerdito_humilde",
                    "cerdito_amable",
                    "cerdito_amigable",
                    "cerdito_cariñoso",
                    "cerdito_amoroso",
                    "cerdito_valiente",
                    "cerdito_feliz",
                    "cerdito_animado",
                    "cerdito_inmortal",
                    "cerdito_disciplinado"                
    ]
    random.shuffle(p_creatures)
    return tuple(p_creatures[:cant])