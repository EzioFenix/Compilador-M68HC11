import re
from Error import Error4,Error5,Error7,Error9
from DataBase import BaseDatos

def q0(linea:str)->str:
    print(linea)
    pattern='^[a-z]{1,24}$'
    pattern2='^[a-z]{1,24}'
    busqueda=re.search(pattern,linea,re.IGNORECASE)
    busqueda2=re.search(pattern2,linea,re.IGNORECASE)

    # unicamente etiqueta
    if busqueda:  
        return q3(linea)
    #etiqueta y otro modo
    elif busqueda2:
        inicioSiguiente =busqueda.end() #puede iniciar en 0 hasta indice final
        return q1(linea[:inicioSiguiente],linea[inicioSiguiente:])
    else:
        return 'false'


def  q1(mnemonico:str,linea:str)->str:
    print(q1 + ' ' + mnemonico +    linea)
    pattern='^\s+'
    busqueda=re.search(pattern, linea)
    isInstruct=BaseDatos.bdIsIntruct(mnemonico.lower())
    isDir=BaseDatos.bdIsIntruct(mnemonico.lower())
    
    # tiene espacio y no es intrucción
    if busqueda and not( isInstruct or isDir):
        inicioSiguiente=busqueda.end()
        return q2(linea[inicioSiguiente:])
    else:
        return 'false'


def q2(linea:str)->str:
    print(linea)
    pattern='^equ'
    pattern2='(^[a-z]{3,5})'
    busqueda=re.search(pattern, linea,re.IGNORECASE)
    busqueda2=re.search(pattern2,linea,re.IGNORECASE)

    if busqueda:
        return 'false 2'
    elif busqueda2:
        instruccionDirectiva=busqueda2.group(1)

        # qr
        if q3(instruccionDirectiva)[0]=='f':
            return 'true'
        else:
            return 'false'
    else: 
        return 'false 2'



def q3(instruccion:str)->str:
    print('q3 ' + instruccion)

    isInstruct=BaseDatos.bdIsIntruct(instruccion.lower())
    if BaseDatos.bdSearchDirectiva(instruccion.lower())==None:
        isDirectiva= False

    if isInstruct or isDirectiva:
        return 'false 3'
    else:
        return 'true'
        



def detectar(linea:str):
    try:
        resultado=q0(linea)
        #print(resultado)
        return resultado
    except Error4.Error4:
        return 'e04'
        #print('004  MNEMÓNICO INEXISTENTE')
    except Error5.Error5:
        return 'e05'
        #print('005  INSTRUCCIÓN CARECE DE OPERANDO(S)')
    except Error7.Error7:
        return 'e07'
        #print('007  MAGNITUD DE OPERANDO ERRONEA')
    except Error9.Error9:
        return 'e09'
        #print ('009  INSTRUCCIÓN CARECE DE ALMENOS UN ESPACIO RELATIVO AL MARGEN')
    except Exception as e: 
        print ("This is an error message!{}".format(e))
        