import DataBase.BaseDatos as bd
import DataBase.BdRow as bdRow


valor:bdRow.BdRow= bd.bdSearch('aba',1)
print(type(valor.byte))
print(str(valor.byte))
print(type(valor.ciclo))
print(valor.ciclo)
print(type(valor.id))
print(valor.id)
print(type(valor.mod))
print(valor.mod)
print(type(valor.no))
print(valor.no)
print(type(valor.opcode))
print(valor.opcode)
print(type(valor.mnemonico))
print(valor.mnemonico)
print(valor)