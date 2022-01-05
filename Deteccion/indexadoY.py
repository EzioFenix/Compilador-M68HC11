import re
from Error import Error4,Error5,Error7,Error9
from DataBase import BaseDatos

def q0(linea:str)->str:
    #print('q0 ' +linea)
    resultado='false'
    pattern='^\s+'
    busqueda=re.search(pattern,linea)
    
    if busqueda:
        inicioSiguiente =busqueda.end() #puede iniciar en 0 hasta indice final
        return q1(linea[inicioSiguiente:])
    else:
        # estas parado en caracter , si es verdadero es que le faltaba espacio relativo
        if q1(linea) == 'true':
            raise Error9.Error9('')


def  q1(linea:str)->str:
    #print('q1 ' +linea)
    pattern='^[a-zA-Z]+'
    busqueda=re.search(pattern, linea)
    
    if busqueda:
        return q3(linea)
    else:
        return 'false'


def q3(linea:str)->str:
    #print('q3 ' +linea)
    pattern='^[a-zA-Z]+'
    busqueda=re.search(pattern, linea)

    if busqueda:
        finalActual =busqueda.end()
        inicioActual=busqueda.start()
        
        instruccion=linea[inicioActual:finalActual]
        instruccion=instruccion.lower()

        # Si regresa instrucción en ese modo
        if BaseDatos.bdSearch(instruccion,5)!=None:
            return q4(linea[finalActual:])
        else:
            raise Error4.Error4('')
    else:
        return 'false'

      
def q4(linea:str)->str:
    #print('q4 ' + linea)
    pattern='^\s+'
    busqueda=re.search(pattern,linea)
    
    if busqueda:
        inicioSiguiente =busqueda.end()
        return q5(linea[inicioSiguiente:])
    else:
        raise Error5.Error5('')


def q5(linea:str)-> str:
    #print('q5 ' + linea)
    pattern='^\$([0-9]|[a-f]|[A-F]){1,2}' #Hex
    pattern2='\S+'
    busqueda=re.search(pattern,linea)
    busqueda2=re.search(pattern2,linea)
    finalActual =busqueda.end()

    if busqueda:
        return q8(linea[finalActual:])
    else:
        if busqueda2:
            return 'false'
        else:
            raise Error7.Error7('')


def q8(linea:str)-> str:
    #print('q7 '+ linea)
    pattern='^,(y|Y)$'
    pattern2='^,(x|X)$'
    busqueda=re.search(pattern, linea)
    busqueda2=re.search(pattern2,linea)
    
    if busqueda:
        return 'true'
    else:
        if busqueda2:
            return 'false'
        else:
            raise Error7.Error7('')


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
        