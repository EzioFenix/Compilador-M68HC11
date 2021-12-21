import re
from Error import Error4,Error6,Error9
from DataBase import BaseDatos

def q0(linea:str):
    print(linea)
    resultado=False
    pattern='^\s+'
    busqueda=re.search(pattern,linea)
    
    if busqueda:
        inicioSiguiente =busqueda.end() #puede iniciar en 0 hasta indice final
        return q1(linea[inicioSiguiente:])
    else:
        busqueda=re.search(pattern,' '+linea)
        if busqueda:
            inicioSiguiente =busqueda.end()-1 #puede iniciar en 0 hasta indice final
        if q1(linea[inicioSiguiente:]) == True:
            raise Error9.Error9('')

def  q1(linea:str):
    print(linea)
    pattern='^[a-zA-Z]+'
    busqueda=re.search(pattern, linea)
    
    if busqueda:
        return q2(linea)
    else:
        return False
    
def q2(linea:str):
    print(linea)
    pattern='^[a-zA-Z]+'
    busqueda=re.search(pattern, linea)
    
    finalActual =busqueda.end()
    inicioActual=busqueda.start()
    
    
    instruccion=linea[inicioActual:finalActual]
    instruccion=instruccion.lower()
    print(instruccion)

    
    if BaseDatos.bdIsIntruct(instruccion):
        return q5(linea[finalActual:])
    else:
        raise Error4.Error4('')
    
def q5(linea:str):
    print('q5')
    print(linea)
    pattern='^\s+'
    busqueda=re.search(pattern,linea)
    
    if busqueda:
        raise Error6.Error6('')
    else:
        return True
    
    
def detectar(linea:str):
    try:
        print(q0(linea)) 
    except Error4.Error4:
        print('004  MNEMÓNICO INEXISTENTE')
    except Error6.Error6:
        print('006  INSTRUCCIÓN NO LLEVA OPERANDO(S)')
    except Error9.Error9:
        print ('009  INSTRUCCIÓN CARECE DE ALMENOS UN ESPACIO RELATIVO AL MARGEN')
    except Exception as e: 
        print ("This is an error message!{}".format(e))
        