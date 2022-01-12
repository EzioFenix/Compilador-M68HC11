import re
import typing
from DataBase import BaseDatos

def precompilar(linea:str)-> typing.Tuple[str,str] : 
    """Regresa la etiqueta, acompañada el texto que le sigue  depués

    Args:
        linea (str): [description]

    Returns:
        typing.Tuple[str,int]: [etiqueta,resto de linea]
    """
    # Los grupos son separados por ()
    pattern='^([a-z]{1,24})\s+([a-z]{3,5})' # tiene mnemonico despues
    pattern2='^([a-z]{1,24})' # no tiene mnemonico despues

    # Realizamos las busquedas
    busqueda=re.search(pattern,linea,re.IGNORECASE)
    busqueda2=re.search(pattern2,linea,re.IGNORECASE)

    # Declaramos
    etiqueta=str
    mnemonico=str
    
    # Si es etiqueta + modo
    if busqueda:
        etiqueta=busqueda.group(1)

        # caluculamos el mnemonico
        fin=busqueda2.end()
        mnemonico=linea[fin:]

        # condiciones para que sea cierto
    elif busqueda2:
        etiqueta=busqueda2.group(1)
        mnemonico=''

    return [etiqueta,mnemonico]

print(precompilar('etiqueta aba'))
print(precompilar('etiqueta '))