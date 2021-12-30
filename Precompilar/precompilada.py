class precompilada():
    
    def __init__(self,pcActual:str,opcode:str,operando:str,byte:int) -> None:
        
        self.pcActual=pcActual # Se almacena por ejmplo 0xff usas la funcion int para converitr
        self.opcode=opcode # el codigo traducido del mnemonico, por ejmplo FF
        self.operando=operando #El valor del operando, en el caso de inherente es vacio =''
        self.byte=byte # cuantos bytes puede ocupar la instrucción (int)
        self.bytesOcupados:byte=0 # cuantos bytes relamente ocupa la instrucción(int)

    def __str__(self) -> str:
        #return self.pcActual + ' ' + self.opcode + ' ' + self.operando + ' ' + self.byte
        return self.pcActual[2:] + ' ' + self.opcode