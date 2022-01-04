import os
import re
#---------------------------- importacioens deteccion paso 1----------------------------
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
#---------------------------- importacioens precompilar paso 2----------------------------
import Precompilar.inherente as preInherente
import Precompilar.org as preOrg
from Precompilar.precompilada import precompilada
import Precompilar.programCounter as prePc

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
    nombreSalida='output.html'
    programa_Paso1:list[str]=[] # programa leido en memoria ram
    programa_Paso2:list[str]=[] # almacena el modo en el que esta detectado
    programa_Paso3:list|str=[] # Almacena el tipo precompilado o 'null' en caso de directiva
    programa_Paso4_Humana:list[str]=[] # Almacena el tipo compilacion humana
    programa_Paso4_S19:list[str]=[] # Almacena la compilacion s19
    PC=prePc.programCounter()
    lista_errores=['001 CONSTANTE INEXISTENTE',
    '002 VARIABLE INEXISTENTE',
    '003 ETIQUETA INEXISTENTE',
    '004 MNEMÓNICO INEXISTENTE',
    '005 INSTRUCCIÓN CARECE DE  OPERANDO(S)',
    '006 INSTRUCCIÓN NO LLEVA OPERANDO(S)',
    '007 MAGNITUD DE  OPERANDO ERRONEA',
    '008 SALTO RELATIVO MUY LEJANO',
    '009 INSTRUCCIÓN CARECE DE ALMENOS UN ESPACIO RELATIVO AL MARGEN',
    '010 NO SE ENCUENTRA END',
    '011 VARIABLE REPETIDA']
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

    # Paso 3 Precompilar-----------------------------------------
    indice=0 # indice para recorrar las instruccioens precompiladas
    isEnd=False # Detecta si el end apareció en el programa
    numLinea=0 # Linea del programa a la izquierda del programa
    for linea in programa_Paso2:
        precompilacionValor=''
        if linea[0]=='d': #directiva
            if linea[1]=='0':
                pcAux=preOrg.precompilar(programa_Paso1[indice])
                PC.set(pcAux)
                precompilacionValor='null'
            if linea[1]=='1': # End
                isEnd=True
                precompilacionValor='null'
                programa_Paso3.append(precompilacionValor) # Como hay break, no se guarda el valor, por ello mejor directo
                break
            if linea[1]=='2': # variable
                pass
            if linea[1]=='3': # etiqueta
                pass
        elif linea[0]=='m': # Modo
            pcAux=PC.get()
            numLinea+=1
            if linea[1]=='0': #inherente
                precompilacionValor= preInherente.precompilar(numLinea,linea,programa_Paso1[indice],pcAux)
                pcAux=precompilacionValor.bytesOcupados
                print(pcAux)
                PC.incrementar(pcAux)
            if linea[1]=='1': #inmediato
                pass
            if linea[1]=='2':
                pass
            if linea[1]=='3':
                pass
            if linea[1]=='4':
                pass
            if linea[1]=='5':
                pass
            if linea[1]=='6':
                pass
        elif linea[0]=='e': # error
            numero=int(linea[1:])
            precompilacionValor=lista_errores[numero]

        # agregamos la intrucción y avanzamos a la sigueitne istrucción
        programa_Paso3.append(precompilacionValor)
        indice+=1 

            
    for i in range(0,len(programa_Paso2)):
        print(programa_Paso1[i] + ' ' +programa_Paso2[i] )
        print(programa_Paso3[i])


    ## Compilado humano---------------------------------------------

    # generamos la compilación humana
    for linea in programa_Paso3:
        linea:precompilada
        if linea!='null':
            programa_Paso4_Humana.append(linea.compilacionHumana())

    ## Creamos l archivo para guardar el html
    with open(nombreSalida, 'w') as f:
        # archivos de donde lee el inicio y final de archivo
        inicio='./compilar/inicio.html'
        fin='./compilar/fin.html'

        # Ejemplo de instrucción
        """
        <div id="input">
            
            <div class="instruccion">
                <div class="lineaCodigo">001</div>
                <div class="pc">8000</div> 
                <div class="opcode">4F</div>
                <div class="operador">FF</div>
                <div class="directiva">001</div>
                <div class="error">8000</div> 
                <div class="comentario">4F</div>
            </div>
        </div>
        """

        # Partes de html que se escribiran las instrucciónes no compiladas
        divInstruc='<div class="instruccion"><div class="pc">%s</div></div>\n'

        # escribimos el inicio del html-----------------
        with open (inicio) as r:
            f.writelines(r.readlines())

        # escribimos lo der achivo input------------------
        f.write('<div id="input">')   
        for linea in programa_Paso1:
            aux=divInstruc%(linea)
            f.write(aux)
        f.write('</div>\n')
        
        # escribimos la salida-----------------------------
        f.write('<div id="output">') 
        for linea in programa_Paso4_Humana:
            f.write(linea)
        f.write('</div>\n')

        # escribimos el inicio del html-----------------
        with open (fin) as r:
            f.writelines(r.readlines())


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
    
    