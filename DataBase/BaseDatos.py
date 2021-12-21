import sqlite3
from . import BdRow

CONEXION=sqlite3.connect('Database/data.db')

def bdSearch(mnemonico:str,modo:int)->BdRow:
  """
  Test: True
  Return: 
    Si existe el mnemonico regresa objeto:
      BdRow[id,no,mnemonico,opcode,ciclo,byte,mod]
    Si no existe regresa:
      None
  NoOperacion ='es el numero de operacion'
  """
  mnemonico=mnemonico.lower()
  buscado=mnemonico + str(modo)
  cursor=CONEXION.execute("select * from INSTRUCCIONES WHERE id=?",(buscado,))
  fila= cursor.fetchone()
  if fila!=None:
      return BdRow.BdRow(fila)
  else:
    return None

def bdIsIntruct(mnemonico:str)->bool:
  """
  Test: True
  Return: 
    True: Existe la instruccion
  """
  mnemonico=mnemonico.lower()
  cursor=CONEXION.execute("select * from INSTRUCCIONES WHERE mnemonico=?",(mnemonico,))
  fila= cursor.fetchone()
  if fila!=None:
    return True
  else:
    return False

def bdSearchDirectiva(mnemonico:str)->list:
  """
  Test: 
  Return: 
    Si existe la directiva regresa una lista:
      [mnemonico(pk),opcode(string),accion(num),operando(num):bytes]
    Si no existe regresa lista vacia:
      []
    Si existe y algo no esta definido regresa
      [memonico,"",-1,0]
  NoOperacion ='es el numero de operacion'
  """
  #return ['opcode',2]
  buscado=mnemonico.lower()
  cursor=CONEXION.execute("select * from DIRECTIVA WHERE mnemonico=?",(mnemonico,))
  fila= cursor.fetchone()
  if fila!=None:
    return fila
  else:
    return None
