import re
from typing import Pattern
from Error import Error4,Error5,Error7,Error9
from DataBase import BaseDatos

def q0(linea:str)-> str:
    #print(linea)
    resultado=''
    pattern='^\s+'
    busqueda=re.search(pattern,linea)
    
    if busqueda:
        inicioSiguiente =busqueda.end() #puede iniciar en 0 hasta indice final
        return q1(linea[inicioSiguiente:])
    else:
        # El actual es un caracter, si acepta de aquí hacia adelante, entonces
        # le faltaba salto relativo al inicio
        if q1(linea) == 'true':
            raise Error9.Error9('')

def  q1(linea:str)-> str:
    #print(linea)
    pattern='^[a-zA-Z]+'
    busqueda=re.search(pattern, linea)
    
    if busqueda:
        return q3(linea)
    else:
        return 'false'
    
def q3(linea:str)-> str:
    #print(linea)
    pattern='^[a-zA-Z]+'
    busqueda=re.search(pattern, linea)

    if busqueda:
        finalActual =busqueda.end()
        inicioActual=busqueda.start()
        
        instruccion=linea[inicioActual:finalActual]
        instruccion=instruccion.lower()
    
        if BaseDatos.bdSearch(instruccion,4)!=None:
            return q5(linea[finalActual:])
        else:
            raise Error4.Error4('')
    else:
        return 'false'
    
def q5(linea:str)->str:
    #print('q5 ' + linea)
    pattern='^\s+'
    busqueda=re.search(pattern,linea)
    
    if busqueda:
        inicioSiguiente =busqueda.end()
        return q7(linea[inicioSiguiente:])
    else:
        raise Error5.Error5('')
    
def q7(linea:str)-> str:
    #print('q7 ' + linea)
    pattern1='^\$([0-9]|[a-f]|[A-F]){1,4}$' #Hex
    pattern2='^[0-9]{1,5}$' # Dec
    pattern3='\S+' # cualquier caracter
    busqueda1=re.search(pattern1,linea)
    busqueda2=re.search(pattern2,linea)
    busqueda3=re.search(pattern3,linea)


    if busqueda1 or busqueda2:
        return 'true'
    elif busqueda3:
        return 'false'
    else:
        raise Error7.Error7('')
    
    
def detectar(linea:str)-> str:
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
        