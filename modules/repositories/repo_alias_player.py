import random

def emul_alias_player():
    '''
    Parameters:
    ----------
    Return:
    ----------
    : str
        Un String con un Alias escogido al Azar
    '''
    alias = [
                    "José",
                    "Nicolás",
                    "Elizabeth",
                    "Amy",
                    "María",
                    "Mery",
                    "Jhon",
                    "Wilmer",
                    "Oscar",
                    "Boris",
                    "Swan",
                    "Bryan",
                    "Moroni",
                    "Moises",
                    "Adán",
                    "Goku",
                    "Gohan",
                    "Naruto",
                    "Ferney",
                    "Seiya",
                    "Walter",            
    ]
    random.shuffle(alias)
    return alias[0]