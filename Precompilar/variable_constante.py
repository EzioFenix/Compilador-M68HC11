import re
import typing


def precompilar(linea:str)-> typing.Tuple[str,str] :
    """Regresa la variable o constante una tupla para que la agreges
    a un diccionario

    Args:
        linea (str): linea de programa leido

    Returns:
        typing.Tuple[str,int]: [nombreEtiqueta,valorint]
    """
    # Los grupos son separados por ()
    pattern='\s+([a-z]{1,12})\s+equ\s+\$([a-f0-9]{1,4})'
    

    busqueda=re.search(pattern,linea,re.IGNORECASE)

    # Los grupos inician en 1
    nombreVariable=busqueda.group(1)
    operando=busqueda.group(2)

    # Convertimos el valor de la etiqueta a hexadecimal quitando 0's

    #--- Parece tonto,pero elimina los ceros de más, si conviertes 2 veces
    operando:str='0x' + operando
    operando:int=int(operando,16)
    operando:str=hex(operando)
    operando=operando[2:]

    return [nombreVariable,operando]