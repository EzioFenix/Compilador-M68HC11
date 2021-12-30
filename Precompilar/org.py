from typing import Pattern


import re
def precompilar(linea:str)->str:
    """Regresa el operando de la directiva ORG

    Example:
    

    Args:
        linea (str): linea donde se encuentra el org

        example= '\t org $8020'

    Returns:
        str: 0x8020
    """
    pattern='([0-9]|[a-f]|[A-F]){1,4}'
    busqueda=re.search(pattern,linea)

    # Buscamos el valor del operando
    indicieIncio=busqueda.start()
    indiceFinal=busqueda.end()

    operando=linea[indicieIncio:indiceFinal]

    return '0x' + operando

