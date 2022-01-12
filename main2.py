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
import Deteccion.variable_constante as deVarConst
import Deteccion.etiqueta as deEtiqueta
#---------------------------- importacioens precompilar paso 2----------------------------
import Precompilar.inherente as preInherente
import Precompilar.inmediato as preInmediato
import Precompilar.directo as preDirecto
import Precompilar.extendido as preExtendido
import Precompilar.indexadoX as preIndeX
import Precompilar.indexadoY as preIndeY
import Precompilar.relativo as preRelativo
import Precompilar.variable_constante as preVarConst
import Precompilar.org as preOrg
import Precompilar.etiqueta as preEtiqueta
from Precompilar.precompilada import precompilada
import Precompilar.programCounter as prePc
import typing

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
    #programa_Paso1_Etiquetas:list[typing.Tuple[str,str]] # almacena tuplas de nombreEtiqueta,indiceEn el paso 2
    programa_Paso1_Etiquetas={}
    programa_Paso3:list|str=[] # Almacena el tipo precompilado o 'null' en caso de directiva
    programa_Paso3_Variables={}#typing.Dict[str,str] # Almacena las variables del programa {nombre(str)=valor(str)} {'nel': '50'}
    programa_Paso3_Etiquetas={}#typing.Dict[str,int] # almacena 
    programa_Paso4_Humana:list[str]=[] # Almacena el tipo compilacion humana
    programa_Paso4_S19:list[str]=[] # Almacena la compilacion s19
    programa_Paso4_Etiquetas={} #dict[clave:str]=valor:int
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
    '011 VARIABLE REPETIDA',
    '012 no me acuerdo',
    '013 Etiqueta con Pc inexistente']

    # Paso 1 Leer de memoria y limpiarlo---------------------------------------------
    programa_Paso1=leerProgramaRam()

    if programa_Paso1 ==None:
        exit()
    else:
        programa_Paso1=eliminarLineasVacias(programa_Paso1)
        print(programa_Paso1)

    # Paso 2 detectamos los modos de operación de cada instrucción---------------------
        # Variables globales
    modoActual=1
    contadorError004=0

        # Reccorremos la lineas del paso 1
    for linea in programa_Paso1:
        modo=''
        
        ## Detectar Directivas-------------------------------------------
        Directivas_Deteccion=[deOrg.detectar,deEnd.detectar,deVarConst.detectar,deEtiqueta.detectar]
        for detectarIndice in range(0,len(Directivas_Deteccion)):
            valor=Directivas_Deteccion[detectarIndice] (linea)

            """
            Valor puede tomar diferentes valores
            - valor='true' ==> significa que el modo actual es el correcto
                si por ejemplo esta en deOrg.detectar y true entoces es modo
            - valor='e09' ==> error 09
            """

            
            #print(valor)
            if valor[0]=='t':
                modo='d' + str(detectarIndice)
                if modo=='d3': # en caso de que sea etiqueta
                    etiqueta,valLinea=preEtiqueta.precompilar(linea)

                    # Verificamos si ya existe la etiqueta
                    if not etiqueta in programa_Paso1_Etiquetas:
                        indicePaso1=programa_Paso1.index(linea)
                        indicePaso1

                        # agregamos el valor
                        programa_Paso1_Etiquetas[etiqueta]=indicePaso1

                    # asignamos el nuevo valor de liena
                    linea=valLinea

                    # si la linea no esta vacia que siga buscando el modo
                    if linea!='':
                        modo=''
                break
            elif valor[0]=='e':
                modo=valor
                break
            
        if modo=='':
            ## Detectar mnemonicos---------------------------------------------
            Modos_Deteccion=[
            deIherente.detectar, #0
            deInmediato.detectar, #1
            deDirecto.detectar, #2
            deExtendido.detectar, #3
            deIndeX.detectar, #4
            deIndeY.detectar, #5
            deRelativo.detectar #6
            ]
            
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
    print(programa_Paso1_Etiquetas)

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
                claveVar,valorVar=preVarConst.precompilar(programa_Paso1[indice])

                # Verificamos si existe la etiqueta 
                if not claveVar in programa_Paso3_Variables:
                    programa_Paso3_Variables[claveVar:str]=valorVar
                    precompilacionValor='null'
                else:
                    precompilacionValor='e011' # Variable ya existente
            if linea[1]=='3': # etiqueta
                precompilacionValor='null'
        elif linea[0]=='m': # Modo
            pcAux=PC.get()
            modo=linea
            numLinea+=1
            if linea[1]=='0': #inherente
                precompilacionValor= preInherente.precompilar(numLinea,modo,programa_Paso1[indice],pcAux)
                pcAux=precompilacionValor.bytesOcupados
                PC.incrementar(pcAux)
            if linea[1]=='1': #inmediato
                precompilacionValor=preInmediato.precompilar(numLinea,modo,programa_Paso1[indice],pcAux)
                pcAux=precompilacionValor.bytesOcupados
                PC.incrementar(pcAux)
                print(precompilacionValor)
            if linea[1]=='2': # directo
                precompilacionValor=preDirecto.precompilar(numLinea,modo,programa_Paso1[indice],pcAux)
                pcAux=precompilacionValor.bytesOcupados
                PC.incrementar(pcAux)
                print(precompilacionValor)
            if linea[1]=='3': # extendido
                precompilacionValor=preExtendido.precompilar(numLinea,modo,programa_Paso1[indice],pcAux)
                pcAux=precompilacionValor.bytesOcupados
                PC.incrementar(pcAux)
                print(precompilacionValor)
            if linea[1]=='4': #indexadoX
                precompilacionValor=preIndeX.precompilar(numLinea,modo,programa_Paso1[indice],pcAux)
                pcAux=precompilacionValor.bytesOcupados
                PC.incrementar(pcAux)
                print(precompilacionValor)
            if linea[1]=='5': # IndexadoY
                precompilacionValor=preIndeY.precompilar(numLinea,modo,programa_Paso1[indice],pcAux)
                pcAux=precompilacionValor.bytesOcupados
                PC.incrementar(pcAux)
                print(precompilacionValor)
            if linea[1]=='6': # Relativo
                precompilacionValor=preRelativo.precompilarPasada1(numLinea,modo,programa_Paso1[indice],pcAux)
                etiquetaObtenida=   precompilacionValor.operando
                print('etiqueta ' + etiquetaObtenida)
                print(programa_Paso3_Etiquetas)
                # Si la etiqueta existe, obten su Pc

                pcAux=precompilacionValor.bytesOcupados
                PC.incrementar(pcAux)
                print(precompilacionValor)
        elif linea[0]=='e': # error
            numero=int(linea[1:])
            precompilacionValor=linea + ' '  + lista_errores[numero]

        # agregamos la intrucción y avanzamos a la sigueitne istrucción
        programa_Paso3.append(precompilacionValor)
        indice+=1 





    # Paso 3 etiquetas-- calcular etiquetas
    for etiqueta in programa_Paso1_Etiquetas:
        #indice es apartir de donde buscarará una instrucción compilada bien
        indiceInicioBusqueda=programa_Paso1_Etiquetas[etiqueta]
        for lineaPrecompilada in programa_Paso3[indiceInicioBusqueda:]:
            
            # si es str signficia, error, vacia
            # si no es, signfica que se compilo bien
            if not isinstance(lineaPrecompilada,str):
                lineaPrecompilada:precompilada
                if lineaPrecompilada.error=='':
                    indicePaso3=programa_Paso3.index(lineaPrecompilada)
                    nombreEtiqueta=etiqueta

                    # agregamos la etiqueta 
                    programa_Paso4_Etiquetas[nombreEtiqueta]=indicePaso3
                    break
        
        # si la etiqueta no se agrego al paso 2, es porque no hay instruccion siguiente
        if not etiqueta in programa_Paso4_Etiquetas:
            ErrorEtiqueta=precompilada(numLinea+1,'','','','',0)
            ErrorEtiqueta.error='e13'
            programa_Paso3.append(ErrorEtiqueta)
            
            
    """ for i in range(0,len(programa_Paso2)):
        print(programa_Paso1[i] + ' ' +programa_Paso2[i] )
        print(programa_Paso3[i]) """


    # Segunda pasada precompilar
    for indice in range(0,len(programa_Paso2)):
        if programa_Paso2[indice]=='m6':
            lineaPrecompilada=programa_Paso3[indice]
            
            # obtenemos la etiqueta
            nombreEtiqueta=lineaPrecompilada.operando

            #buscamos la etiqueta
            if nombreEtiqueta in programa_Paso4_Etiquetas:
                indiceEtiqueta=programa_Paso4_Etiquetas[nombreEtiqueta]

                #obtenemos el valor de pc etiqueta
                etiquetaPrecompilada:precompilada=programa_Paso3[indiceEtiqueta]

                #obtenemos los pc's
                pcEtiqueta=etiquetaPrecompilada.pcActual

                # se tiene que copiar el resultado en la el programa paso 3
                lineaPrecompilada=preRelativo.precompilarPasada2(lineaPrecompilada,pcEtiqueta)
                programa_Paso3[indice]=lineaPrecompilada

                """ print('jeje ' + lineaPrecompilada.operando)
                print('jeje ' + programa_Paso3[indice].operando) """


            else:
                lineaPrecompilada.error='e03'

    # Error 10 no tiene final
    if isEnd==False:
        ErrorEtiqueta=precompilada(numLinea+1,'','','','',0)
        ErrorEtiqueta.error='e10'
        programa_Paso3.append(ErrorEtiqueta)

    ## Compilado humano---------------------------------------------

    # generamos la compilación humana
    for linea in programa_Paso3:
        linea:precompilada|str
        if isinstance(linea,str):
            pass
            # linea!='null' and linea[0]!='e':
        else:
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
        divInstruc='\n\t\t\t<div class="instruccion">\n\t\t\t\t<div class="pc">%s</div>\n\t\t\t</div>'

        # escribimos el inicio del html-----------------
        with open (inicio) as r:
            f.writelines(r.readlines())

        # escribimos lo der achivo input------------------
        f.write('\n\t\t<div id="input">')   
        for linea in programa_Paso1:
            aux=divInstruc%(linea.strip())
            f.write(aux)
        f.write('\n\t\t</div>')
        
        # escribimos la salida-----------------------------
        f.write('\n\t\t<div id="output">') 
        for linea in programa_Paso4_Humana:
            f.write(linea)
        f.write('</div>\n')

        # escribimos el inicio del html-----------------
        with open (fin) as r:
            f.writelines(r.readlines())

        print(programa_Paso3_Variables)


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
    
    