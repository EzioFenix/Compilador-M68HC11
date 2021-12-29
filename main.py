import os
import re
import Deteccion.inherente as deIh
import Deteccion.inmediato as deIn
import Deteccion.directo as deDi
import Deteccion.extendido as deEx
import Deteccion.indexadoX as deIndeX
import Deteccion.indexadoY as deIndeY
import Deteccion.org as deOrg
import Deteccion.end as deEnd
import Deteccion.relativo as deRelativo
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
    modo=''
    modoActual=1
    contadorError004=0
    for linea in programa_Paso1[0:1]:
        if modoActual==1:
            valor=deOrg.detectar(linea)
            if valor==True:
                print(valor)
                modo='d1'
                modoActual=-1
            ''' else:
                if valor[0]=='e':
                    modo=valor
                else:
                    modoActual=1 '''
        if modoActual==1:
            valor=deIh.detectar(linea)
            if valor=='e04':
                contadorError004+=1
                modoActual+=1
            elif valor==True:
                modo='m1'
            elif valor[0]=='e':
                modo=valor
            else:
                modoActual+=1
        elif deEnd.detectar(linea):
            modo='d2'
        else:
            contadorError004=0 
            patternEspacio='^\s+'
            busqueda=re.search(patternEspacio,linea)
            
            modoActual=1
            valor=''
            modo=''
            if modoActual==1:
                valor=deIh.detectar(linea)
                if valor=='e04':
                    contadorError004+=1
                    modoActual+=1
                elif valor==True:
                    modo='m1'
                elif valor[0]=='e':
                    modo=valor
                else:
                    modoActual+=1
            if modoActual==2:
                valor=deIn.detectar(linea)
                if valor=='e04':
                    contadorError004+=1
                    modoActual+=1
                elif valor==True:
                    modo='m2'
                elif valor[0]=='e':
                    modo=valor
                else:
                    modoActual+=1
            if modoActual==3:
                valor=deDi.detectar(linea)
                if valor=='e04':
                    contadorError004+=1
                    modoActual+=1
                elif valor==True:
                    modo='m3'
                elif valor[0]=='e':
                    modo=valor
                else:
                    modoActual+=1
            if modoActual==4:
                valor=deIndeX.detectar(linea)
                if valor=='e04':
                    contadorError004+=1
                    modoActual+=1
                elif valor==True:
                    modo='m4'
                elif valor[0]=='e':
                    modo=valor
                else:
                    modoActual+=1
            if modoActual==5:
                valor=deIndeY.detectar(linea)
                if valor=='e04':
                    contadorError004+=1
                    modoActual+=1
                elif valor==True:
                    modo='m5'
                elif valor[0]=='e':
                    modo=valor
                else:
                    modoActual+=1
            if modoActual==6:
                valor=deRelativo.detectar(linea)
                if valor=='e04':
                    contadorError004+=1
                    modoActual+=1
                elif valor==True:
                    modo='m6'
                elif valor[0]=='e':
                    modo=valor
                else:
                    modoActual+=1
            if modoActual==7:
                valor=deEx.detectar(linea)
                if valor=='e04':
                    contadorError004+=1
                    modoActual+=1
                elif valor==True:
                    modo='m7'
                elif valor[0]=='e':
                    modo=valor
                else:
                    modoActual+=1
        
        programa_Paso2.append(modo)
    print(programa_Paso2)
            
    #for i in range(0,1):
    #    print(programa_Paso1[i] + ' ' +programa_Paso2[i] )

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
    
    
    
    