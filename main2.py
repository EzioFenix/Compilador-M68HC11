import os
import re
import Deteccion.inherente as deIherente #m1
import Deteccion.inmediato as deInmediato #m2
import Deteccion.directo as deDirecto #m3
import Deteccion.indexadoX as deIndeX #m4
import Deteccion.indexadoY as deIndeY #m5
import Deteccion.relativo as deRelativo #m6
import Deteccion.extendido as deExtendido #m7
import Deteccion.org as deOrg
import Deteccion.end as deEnd
import Deteccion.variable_constante as deVariable

def leerProgramaRam()-> list:
    nombreArchivo='./input.asc'
    if os.path.exists(nombreArchivo):
        with open(nombreArchivo) as f:
            leido=f.readlines()
            resultado=[]
            for linea in leido:
                resultado.append(linea.rstrip())
            return resultado
    else:
        f = open(nombreArchivo, "x")
        f.close()
        return None

def eliminarLineasVacias(programa_Paso1:list)->list:
    pattern='^\s+$'
    resultado=[]
    for linea in programa_Paso1:
        if not (re.search(pattern, linea) or linea==''):
            resultado.append(linea)
    return resultado


def main():
    programa_Paso1=[] # programa leido en memoria ram
    programa_Paso2=[] # almacena el modo en el que esta detectado
    programa_Paso1=leerProgramaRam()

    if programa_Paso1 ==None:
        exit()
    else:
        programa_Paso1=eliminarLineasVacias(programa_Paso1)
        print(programa_Paso1)
        
    # Detectamos el tipo de instrucción
    
    modoActual=1
    contadorError004=0
    for linea in programa_Paso1:
        modo=''
        
        ## Detectar Directivas-------------------------------------------
        Directivas_Deteccion=[deOrg.detectar,deEnd.detectar,deVariable.detectar]
        for detectarIndice in range(0,len(Directivas_Deteccion)):
            valor=Directivas_Deteccion[detectarIndice] (linea)
            
            #print(valor)
            if valor[0]=='t':
                modo='d' + str(detectarIndice)
                break
            elif valor[0]=='e':
                modo=valor
                break
            
        if modo=='':
            ## Detectar mnemonicos---------------------------------------------
            Modos_Deteccion=[deIherente.detectar,deInmediato.detectar,deDirecto.detectar,deIndeX.detectar,deIndeY.detectar,
                            deRelativo.detectar,deExtendido.detectar]
            
            for detectarIndice in range(0,len(Modos_Deteccion)):
                
                valor=Modos_Deteccion[detectarIndice] (linea)
                contadorError004=0
                
                if valor[0]=='t':
                    modo='m' + str(detectarIndice)
                    break
                elif valor=='e04':
                    contadorError004+=1
                elif valor[0]=='e':
                    modo=valor
                    break
            
            if contadorError004==7:
                modo='e04'
        
        programa_Paso2.append(modo)
    #print(programa_Paso2)
            
    for i in range(0,len(programa_Paso2)):
        print(programa_Paso1[i] + ' ' +programa_Paso2[i] )

if __name__== "__main__":
    main()
    #deOrg.detectar('\tORG  $8000')
    #deIh.detectar(' nop')
    #deIn.detectar(' ldaa  #65535')
    #deDi.detectar(' ldaa 055')
    #deEx.detectar(' bclr 055')
    #deIndeX.detectar(' ldaa   $4500,x')
    #deIndeY.detectar(' ldaa   $1,y')
    #deRelativo.detectar(' bvs ss')
    #deOrg.detectar(' orG $400F')
    #deVariable.detectar(' PACTL equ $1000')
    
    