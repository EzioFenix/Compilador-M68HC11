class BdRow:
  """
  Respuesta consulta en BD meidante bdSearch
  """
  def __init__(self,lista:list) -> None:
      self.byte:int
      self.ciclo:int
      self.id:str
      self.mod:int
      self.no:int
      self.mnemonico:str
      self.opcode:str
      self.id=''
      self.id,self.no,self.mnemonico,self.opcode,self.ciclo,self.byte,self.mod=lista
      #--------
      aux=self.opcode.split(' ')
      aux=''.join(aux)
      self.opcode=aux.upper()
      #--------
      self.mnemonico=self.mnemonico.upper()
      