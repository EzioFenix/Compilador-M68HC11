from os import error
from typing import List


class precompilada():
    
    def __init__(self,numLinea:int,modo:str,pcActual:str,opcode:str,operando:str,byte:int) -> None:
        
        self.pcActual=pcActual # Se almacena por ejmplo 0xff usas la funcion int para converitr
        self.opcode=opcode # el codigo traducido del mnemonico, por ejmplo FF
        self.operando=operando #El valor del operando, en el caso de inherente es vacio =''
        self.byte=byte # cuantos bytes puede ocupar la instrucción (int)
        self.bytesOcupados:byte=0 # cuantos bytes relamente ocupa la instrucción(int)
        self.error:str=''
        self.modo:str=modo
        self.numLinea:int=numLinea

    def setError(self,error:str)->None:
        """Establece un error por linea pre compilada, si se intenta agregar más de uno
        entonces lo deja fuera al último error

        Args:
            error (str): Nuevo error
        """
        if self.error=='':
            self.error=error

    def __str__(self) -> str:
        #return self.pcActual + ' ' + self.opcode + ' ' + self.operando + ' ' + self.byte

        if error=='':
            return self.pcActual[2:] + ' ' + self.opcode
        else:
            return self.error

    # Compilación humana ----------------

    def divInstruccion(self,texto:str)->str:
        textohtml="""               <div class="instruccion">
            %s
        </div>
        """%(texto)
        return textohtml


    def htmlDiv(self,texto:str,clase:str)->str:
        textoHtml='<div class="%s">%s</div>'%(clase,texto)
        return textoHtml


    def compilacionHumana(self)-> str:
        # Variables globales función
        resultado=''
        aux=[]

        # Si hay error sólo regresa el error
        if self.error!='':
            return 'error'
        else:
            pcImprimir=self.pcActual[2:] #0x01 => 01
            print(self.modo)
            if self.modo =='m0': #inherente
                numLinea=self.htmlDiv(str(self.numLinea),'lineaCodigo')
                pc=self.htmlDiv(pcImprimir,'pc')
                opcode= self.htmlDiv(self.opcode,'opcode')
                aux=[numLinea,pc,opcode]
                #print(aux)


            # Unimos todo el texto que se tiene que devolver
            for linea in aux:
                resultado+= '\n\t\t\t\t' + linea

            # Envolvemos en el div de instrucción
            resultado='\n\t\t\t' +self.htmlDiv(resultado,'instruccion')

            # Devolvemos convertido en html
            print(resultado + '\n')
            return resultado


    def compilacionS19(self)->str:
        pass

    # Compilación s19 -------------------