# Compilador-M68HC11
Es un compilador para la materia de Estructura y programación de computadoras implementado en python.

## Compilación explicada en pasos

### Paso 1 Leer el archivo

- Donde se ejecute el programa tiene que existir el archivo, si este no existe , lo crea y termina su ejecución.

  Caso contrario si existe pasa al paso 2.

### Paso 2  Leer archivo y pasarlo a RAM(arreglo)

- Usando el archivo lo pasamos a un arreglo con cada una de las líneas leídas.
- Eliminamos el `\n` al final de cada línea de instrucciones.
- Eliminamos las líneas que están vacías.

### Paso 3 Detectar ¿Qué es?

Cada línea de código tiene que caer en las siguientes categorias:

- Variable o constante =V
- Directiva =D
  - org D1
  - end D2
- Modo operación
  - Inherente =M1
  - Inmediato =M2

En caso de que no tenga la forma deseada de la instrucción, tendrá  que regresar que tipo de error es.

- Errores
  - 

## Ejemplo

``````python
linea='  ORG  $8000'

``````

#### Errores de acuerdo al modo

##### Indexado

- 

## Detección

### Inherente

![Detecccion_Inherente](Documentacion/Detecccion_Inherente.png)

**Errores detectado**

- 004  MNEMÓNICO INEXISTENTE
- 006  INSTRUCCIÓN NO LLEVA OPERANDO(S)
- 009  INSTRUCCIÓN CARECE DE ALMENOS UN ESPACIO RELATIVO AL MARGEN

### Inmediato

![Deteccion_Inmediato](Documentacion/Deteccion_Inmediato.png)

- Si llega a `q12` es éxito.

**Errores detectados**

- 004  MNEMÓNICO INEXISTENTE
- 005  INSTRUCCIÓN CARECE DE OPERANDO(S)
- 007  MAGNITUD DE OPERANDO ERRONEA (Detección,Pre-compilación)
- 009  INSTRUCCIÓN CARECE DE ALMENOS UN ESPACIO RELATIVO AL MARGEN
- 011 MÁS OPERANDOS DE LOS NECESARIOS (EXTRA).

### Directo

![Deteccion_Directo](Documentacion/Deteccion_Directo.png)

#### Errores detectados

- 004  MNEMÓNICO INEXISTENTE
- 005  INSTRUCCIÓN CARECE DE OPERANDO(S)
- 007  MAGNITUD DE OPERANDO ERRONEA (Detección,Pre-compilación)
- 009  INSTRUCCIÓN CARECE DE ALMENOS UN ESPACIO RELATIVO AL MARGEN

# Base de datos

Modos:

1. Inherente
2. Inmediato
3. directo
4. x
5. x
6. x
   1. Extendido


# Uso

1. Busca si existe un archivo llamado `input.asc` con codificación ANSI lo lee en caso de que no exista, le crea un archivo con el nombre y se cierra.