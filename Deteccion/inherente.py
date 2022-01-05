import re
from Error import Error4,Error6,Error9
from DataBase import BaseDatos

def q0(linea:str):
    #print('q0' + linea)
    pattern='^\s+'
    busqueda=re.search(pattern,linea)
    
    if busqueda:
        inicioSiguiente =busqueda.end() #puede iniciar en 0 hasta indice final
        return q1(linea[inicioSiguiente:])
    else:
        # Es este modo y le falto espacio al inicio
        busqueda=re.search(pattern,' '+linea)
        if busqueda:
            inicioSiguiente =busqueda.end()-1 #puede iniciar en 0 hasta indice final
            if q1(linea[inicioSiguiente:]) =='true':
                raise Error9.Error9('') # Espacio en el margen
            else:
                return 'false'
        else:
            return 'false'

def  q1(linea:str):
    # print('q1 ' + linea)
    pattern='^[a-zA-Z]+'
    busqueda=re.search(pattern, linea)
    
    if busqueda:
        return q2(linea)
    else:
        return 'false'
    
def q2(linea:str):
    # print('q2 ' + linea)
    pattern='^[a-zA-Z]+'
    busqueda=re.search(pattern, linea)
    
    if busqueda:
        finalActual =busqueda.end()
        inicioActual=busqueda.start()
        instruccion=linea[inicioActual:finalActual]
        instruccion=instruccion.lower()
        
        if BaseDatos.bdSearch(instruccion,1)!=None:
            return q5(linea[finalActual:])
        else:
            raise Error4.Error4('')
    else:
        raise Error4.Error4('')
    
def q5(linea:str):
    # print('q5' + linea)
    pattern='$'
    busqueda=re.search(pattern,linea)
    
    if busqueda:
        return 'true'
    else:
        raise Error6.Error6('')
    
    
def detectar(linea:str):
    try:
        resultado=q0(linea)
        #print(resultado)
        return resultado 
    except Error4.Error4:
        return 'e04'
        #print('004  MNEMÓNICO INEXISTENTE')
    except Error6.Error6:
        return 'e06'
        #print('006  INSTRUCCIÓN NO LLEVA OPERANDO(S)')
    except Error9.Error9:
        return 'e09'
        #print ('009  INSTRUCCIÓN CARECE DE ALMENOS UN ESPACIO RELATIVO AL MARGEN')
    except Exception as e: 
        print ("This is an error message!{}".format(e))
        