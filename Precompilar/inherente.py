import re
from Error import Error4,Error6,Error9
from DataBase import BaseDatos,BdRow
from .precompilada import precompilada
from typing import Pattern

def precompilar(numLinea:int,modo:str,linea: str,pc:str)-> precompilada:
    pattern='[a-zA-Z]+'
    mnemonicoBusqueda=re.search(pattern,linea,re.IGNORECASE)

    # Obtenemos el mnemonico-------------------------------
    mnemonicoInicio=mnemonicoBusqueda.start()
    mnemonicoFin=mnemonicoBusqueda.end()
    mnemonico =linea[mnemonicoInicio:mnemonicoFin]

    # Consulta a la base de datos-------------------------------
    consultaBd:BdRow = BaseDatos.bdSearch(mnemonico,1)

    # Datos directos--------------------------------------
    lineaPrecompilada=precompilada(numLinea,modo,pc,consultaBd.opcode,'',consultaBd.byte)

    # Datos detivados-----------------------------------
    lineaPrecompilada.bytesOcupados=consultaBd.byte

    # Establecemso el modo
    

    return lineaPrecompilada


