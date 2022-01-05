import re
from Error import Error4,Error6,Error9
from DataBase import BaseDatos,BdRow
from .precompilada import precompilada
from typing import Pattern

def precompilar(numLinea:int,modo:str,linea: str,pc:str)-> precompilada:
    # variables globales funcion
    error=''
    operandoPrecompilado:str=''

    # Buscamos el mnemonico
    pattern='[a-zA-Z]+'     
    mnemonicoBusqueda=re.search(pattern,linea,re.IGNORECASE)

    # Obtenemos el mnemonico-------------------------------
    mnemonicoInicio=mnemonicoBusqueda.start()
    mnemonicoFin=mnemonicoBusqueda.end()
    mnemonico =linea[mnemonicoInicio:mnemonicoFin]

    # Consulta a la base de datos-------------------------------
    consultaBd:BdRow = BaseDatos.bdSearch(mnemonico,3)

    # Detectamos el tipo de operando
    pattern1='\$([0-9]|[a-f]|[A-F]){1,2}$' #Hex
    pattern2='[0-9]{1,3}$' # Dec
    busqueda=re.search(pattern,linea)
    inicioHastag=busqueda.end()

    # A partir del hashtrag buscamos el operando
    busqueda1=re.search(pattern1,linea)
    busqueda2=re.search(pattern2,linea)

    if busqueda1: #Hex
        inicio=busqueda1.start()+1 # el más uno es para omitir el $
        fin=busqueda1.end()

        #--- Parece tonto,pero elimina los ceros de más, si conviertes 2 veces
        #print(linea)
        print(linea[inicio:])
        operando:str='0x' + linea[inicio:fin]
        operando:int=int(operando,16)
        operando:str=hex(operando)

        # Calculamos  los bytes de cada cosa
        bytesOperando=int(round((len(operando)-2)/2)) # le menos 2 es por 0x, el round es porque 3 digitos son 2 bytes
        bytesOpcode=int(round( len(consultaBd.opcode)/2))
        bytesOcupados= bytesOperando+ bytesOpcode
        bytesRestantes=consultaBd.byte- bytesOcupados

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
        operando:int=int(operando,16)
        operando:str=hex(operando)
        

        # Calculamos  los bytes de cada cosa
        bytesOperando=int(round((len(operando)-2)/2)) # le menos 2 es por 0x, el round es porque 3 digitos son 2 bytes
        bytesOpcode=int(round( len(consultaBd.opcode)/2))
        bytesOcupados= bytesOperando+ bytesOpcode
        bytesRestantes=consultaBd.byte- bytesOcupados


        # Comprobamos si el operando es correcto
        if 0<=bytesRestantes:
            operandoPrecompilado= operando[2:]
        else:
            error='e07'

    print(operandoPrecompilado)


    # Datos directos--------------------------------------
    lineaPrecompilada=precompilada(numLinea,modo,pc,consultaBd.opcode,operandoPrecompilado,consultaBd.byte)

    # Datos detivados-----------------------------------
    lineaPrecompilada.bytesOcupados=consultaBd.byte

    return lineaPrecompilada