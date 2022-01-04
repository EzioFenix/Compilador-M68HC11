import re
from Error import Error4,Error6,Error9
from DataBase import BaseDatos,BdRow
from .precompilada import precompilada
from typing import Pattern

def precompilar(numLinea:int,linea: str,pc:str)-> precompilada:
    # variables globales funcion
    error=''
    operandoPrecompilado=''

    # Buscamos el mnemonico
    pattern='[a-zA-Z]+'     
    mnemonicoBusqueda=re.search(pattern,linea,re.IGNORECASE)

    # Obtenemos el mnemonico-------------------------------
    mnemonicoInicio=mnemonicoBusqueda.start()
    mnemonicoFin=mnemonicoBusqueda.end()
    mnemonico =linea[mnemonicoInicio:mnemonicoFin]

    # Consulta a la base de datos-------------------------------
    consultaBd:BdRow = BaseDatos.bdSearch(mnemonico,2)

    # Detectamos el tipo de operando
    pattern='#'
    pattern1='^\$([0-9]|[a-f]|[A-F]){1,4}$' #Hex
    pattern2='^[0-9]{1,5}$' # Dec
    pattern3='^’(\S| ){1}$' #un caracter o un espacio
    busqueda=re.search(pattern,linea)
    inicioHastag=busqueda.start()

    # A partir del hashtrag buscamos el operando
    busqueda1=re.search(pattern1,linea[inicioHastag:])
    busqueda2=re.search(pattern2,linea[inicioHastag:])
    busqueda3=re.search(pattern3,linea[inicioHastag:])

    if busqueda1: #Hex
        inicio=busqueda1.start()
        fin=busqueda1.end()

        #--- Parece tonto,pero elimina los ceros de más, si conviertes 2 veces
        operando:str='0x' + linea[inicio:fin]
        operando:int=int(operando,16)
        operando:str=hex(operando)

        # Calculamos  los bytes de cada cosa
        bytesOperando=int(round((len(operando)-2)/2)) # le menos 2 es por 0x, el round es porque 3 digitos son 2 bytes
        bytesOpcode=int(round( len(consultaBd.opcode)/2))
        bytesOcupados= bytesOperando+ bytesOpcode
        bytesRestantes=consultaBd.bytes- bytesOcupados

        # Comprobamos si el operando es correcto
        if 0<=bytesRestantes: # Queda espacio o no
            operandoPrecompilado= linea[inicio:fin]
        else:
            error='e07'
    elif busqueda2: # Dec
        inicio=busqueda2.start()
        fin=busqueda2.end()
        operando=int(linea[inicio:fin])

        # Compilamos el operando a hex
        operando:str=hex(operando)
        
        #--- Parece tonto pero elimina los ceros de más, si conviertes 2 veces
        operando:str='0x' + linea[inicio:fin]
        operando:int=int(operando,16)
        operando:str=hex(operando)

        # Calculamos  los bytes de cada cosa
        bytesOperando=int(round((len(operando)-2)/2)) # le menos 2 es por 0x, el round es porque 3 digitos son 2 bytes
        bytesOpcode=int(round( len(consultaBd.opcode)/2))
        bytesOcupados= bytesOperando+ bytesOpcode
        bytesRestantes=consultaBd.bytes- bytesOcupados

        # Comprobamos si el operando es correcto
        if 0<=bytesRestantes:
            operandoPrecompilado= linea[inicio:fin]
        else:
            error='e07'

    elif busqueda3: # Ascii
        inicio=busqueda3.start()
        fin=busqueda3.end()
        operando=ord(linea[inicio:fin]) # traduce a su valor en numerico
        if ord<128:
            operando=hex(operando)
            operandoPrecompilado=operando[2:]
        else:
            error='e07'


    # Datos directos--------------------------------------
    lineaPrecompilada=precompilada(numLinea,pc,consultaBd.opcode,operando,consultaBd.byte)

    # Datos detivados-----------------------------------
    lineaPrecompilada.bytesOcupados=consultaBd.byte

    return lineaPrecompilada