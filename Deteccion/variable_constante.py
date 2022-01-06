import re
from Error import Error4,Error5,Error7,Error9,Error12
from DataBase import BaseDatos

def q0(linea:str)->str:
    #print('q0 ' + linea)
    resultado=''
    pattern='^\s+'
    busqueda=re.search(pattern,linea)
    
    if busqueda:
        inicioSiguiente =busqueda.end() #puede iniciar en 0 hasta indice final
        return q2(linea[inicioSiguiente:])
    else:
        # estas parado en caracter , si es verdadero es que le faltaba espacio relativo
        if q2(linea) == 'true':
            raise Error9.Error9('')
        else:
            return 'false'


def q2(linea:str)->str:
    #print('q2 ' +linea)
    pattern='^[a-zA-Z]{1,12}'
    pattern2='^[a-zA-Z]+' # por si existe un nombre más largo
    busqueda=re.search(pattern, linea,re.IGNORECASE)
    busqueda2=re.search(pattern2, linea,re.IGNORECASE)

    
    finalActual =busqueda.end()
    finalActual2=busqueda2.end()

    # Si regresa instrucción en ese modo
    if busqueda:
        return q3(linea[finalActual:])
    else:
        if busqueda2:
            if q3(linea[finalActual2:])=='true':
                raise Error12.Error12('')
            else :
                return 'false'
        else:
            return 'false'
    

def q3(linea:str)->str:
    #print('q3 ' + linea)
    pattern='^\s+equ\s+'
    busqueda=re.search(pattern,linea,re.IGNORECASE)
    
    if busqueda:
        inicioSiguiente =busqueda.end()
        return q5(linea[inicioSiguiente:])
    else:
        return 'false'


def q5(linea:str)->str:
    #print('q5 ' + linea)
    pattern='^\$' # tiene operando correcto
    pattern2='\S+' # tiene operandos
    busqueda=re.search(pattern,linea)
    busqueda2=re.search(pattern2,linea)


    if busqueda:
        inicioSiguiente =busqueda.end()
        return q6(linea[inicioSiguiente:])
    else:
        if busqueda2: #tiene operando
            return 'false'
        else:
            raise Error5.Error5('')



def q6(linea:str)->str:
    #print('q6 ' + linea)
    pattern='^([0-9]|[a-f]|[A-F]){1,4}$' #Hex
    busqueda=re.search(pattern,linea)

    if busqueda:
        return 'true'
    else:
        raise Error7.Error7('')
    

def detectar(linea:str)->str:
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
    except Error12.Error12:
        return 'e12'
    except Exception as e: 
        print ("This is an error message!{}".format(e))