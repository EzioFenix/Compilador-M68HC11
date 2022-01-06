import re
from Error import Error4,Error5,Error7,Error9
from DataBase import BaseDatos

def q0(linea:str)->str:
    # print(linea)
    resultado=''
    pattern='^\s+'
    busqueda=re.search(pattern,linea)
    
    if busqueda:
        inicioSiguiente =busqueda.end() #puede iniciar en 0 hasta indice final
        return q3(linea[inicioSiguiente:])
    else:
        if q3(linea)=='true':
            raise Error9.Error9('')
        else:
            return 'false'

    
def q3(linea:str)-> str:
    #print('q3 ' + linea)
    pattern='^org'
    busqueda=re.search(pattern, linea,re.IGNORECASE)
    
    if busqueda:
        finalActual=busqueda.end()
        return q4(linea[finalActual:])
    else:
        return 'false'


def q4(linea:str)-> str:
    #print('q4 ' + linea)
    pattern='^\s+'
    busqueda=re.search(pattern,linea)
    
    if busqueda:
        inicioSiguiente =busqueda.end()
        return q7(linea[inicioSiguiente:])
    else:
        raise Error5.Error5('')
    
def q7(linea:str) ->str:
    # print('q7 ' + linea)
    pattern1='^\$([0-9]|[a-f]|[A-F]){1,4}$' #Hex
    busqueda1=re.search(pattern1,linea)

    if busqueda1:
        return 'true'
    else:
        raise Error7.Error7('')
    
    
def detectar(linea:str)->str:
    try:
        resultado=q0(linea)
        #print(resultado)
        return resultado 
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