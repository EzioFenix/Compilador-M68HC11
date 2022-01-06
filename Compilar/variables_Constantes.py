import typing
import re


def compilar(linea:str)-> typing.Tuple[str,int] : 
    
    # ejemplo  \s+ variable equ $1000
    pattern='^[a-zA-Z]{1,12}'
    pattern2='equ'
    pattern3='([0-9]|[a-f]|[A-F]){1,4}$' #Hex
    
    # Buscamos los patrones
    busqueda=re.search(pattern,linea,re.IGNORECASE)
    busqueda2=re.search(pattern2,linea,re.IGNORECASE)
    busqueda3=re.search(pattern3.linea,re.IGNORECASE)

    # 


    