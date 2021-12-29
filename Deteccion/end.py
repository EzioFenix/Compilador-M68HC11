import re
from Error import Error4,Error5,Error7,Error9
from DataBase import BaseDatos

def q0(linea:str)->str:
    #print('q0 ' +linea)
    resultado=''
    pattern='^\s+'
    busqueda=re.search(pattern,linea)
    
    if busqueda:
        inicioSiguiente =busqueda.end() #puede iniciar en 0 hasta indice final
        return q2(linea[inicioSiguiente:])
    else:
        busqueda=re.search(pattern,' '+linea)
        if busqueda:
            inicioSiguiente =busqueda.end()-1 #puede iniciar en 0 hasta indice final
        if q2(linea[inicioSiguiente:]) == 'true':
            raise Error9.Error9('')

def  q2(linea:str)-> str:
    #print('q2 ' + linea)
    pattern='^end'

    busqueda=re.search(pattern, linea,re.IGNORECASE)
    
    if busqueda:
        return q3(linea)
    else:
        return 'false'
    
def q3(linea:str)-> str:
    #print('q3 ' + linea)
    pattern1='$'
    pattern2='\S+'
    
    busqueda1=re.search(pattern1, linea)
    busqueda2=re.search(pattern2, linea)
    
    # Si regresa instrucción en ese modo
    if busqueda1:
        return 'true'
    elif busqueda2:
        finalActual =busqueda2.end()
        return q5(linea[finalActual:])
    else:
        raise Error5.Error5('')
    
def q5(linea:str)-> str:
    #print('q5 ' + linea)
    pattern='^\$'
    busqueda=re.search(pattern,linea)
    
    if busqueda:
        inicioSiguiente =busqueda.end()
        return q6(linea[inicioSiguiente:])
    else:
        raise Error5.Error5('')
    
def q6(linea:str)-> str:
    #print('q6 ' + linea)
    pattern1='^\$([0-9]|[a-f]|[A-F]){1,4}$' #Hex
    busqueda1=re.search(pattern1,linea)

    if busqueda1:
        return 'true'
    else:
        raise Error7.Error7('')
    


def detectar(linea:str)->str:
    try:
        resultado=q0(linea)
        # print(resultado)
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
        