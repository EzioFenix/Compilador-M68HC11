class programCounter():
    def __init__(self) -> None:
        self.pcDec:int=0

    def incrementar(self,incremento: int)->str:
        """Incrementa el contador de Program Counter

        Args:
            incremento (int): El número de incremento

        Returns:
            str: El nuevo número del Pc counter
        """
        self.pcDec+=incremento
        return hex(self.pcDec)

    def set(self,pc:str)->None:
        """Establece el pc del

        Args:
            pc (str): Program Counter
        """
        self.pcDec=int(pc,16)

    def get(self)->str:
        return hex(self.pcDec)