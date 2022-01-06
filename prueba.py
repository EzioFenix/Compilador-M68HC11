import re
import typing

def precompilar(linea:str)-> typing.Tuple[str,int] : 
    # Los grupos son separados por ()
    pattern='\s+([a-z]{1,12})\s+equ\s+\$([a-f0-9]{1,4})'
    

    busqueda=re.search(pattern,linea,re.IGNORECASE)

    # Los grupos inician en 1
    nombreVariable=busqueda.group(1)
    valorVariable=busqueda.group(2)


    return [nombreVariable,valorVariable]

#print(compilar('  aaaaa equ $ff'))