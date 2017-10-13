'''
EXPLICACION

Este script fue concebido para clasificar todas las fotos que se encuentren en una carpeta segun sus fechas por mes.
El script creará carpetas según los meses que las fotos tienen y luego copiara las fotos dentro de estas carpetas.
Al terminar el proceso todas las fotos estaran organizadas por meses.
También es posible organizar cualquier otra carpeta de esta manera. Copie la carpeta de fotos de su celular o
camara en una carpeta local el su computadora (por velocidad y compatibilidad) y luego asígnele al script el camino correcto
de la forma: C:\\\\user\\username\\fotos\\08.05.2017\\ el último slash es importante

Variables:
dirname     = es la entrada del camino y directorio a clasificar
navegadir   = tendra los directorios que hay en dirname
elemento    = es un contador de elementos
rutayarchivo= es la ruta dirname mas el nombre de archivo
esdir       = contendra el resultado booleano del analisis si rutayarchivo es un archivo o un directorio
fecha       = sera el nombre del archivo restando la hora en su nombre
nuevodir    = sera el nuevo directorio donde se guardaran los archivos segun YYYYmm
'''
import os, shutil

dirname=input('Introduzca la ruta completa a su carpeta, un slash al final es importante :  ')

navegadir = os.listdir(dirname)

for elemento in navegadir:
    rutayarchivo = dirname + elemento
    esdir = os.path.isfile(rutayarchivo) #<-- respuesta booleana true is file, false es directorio
    fecha = elemento[:6]                 #<-- cambie el numero despues de los dos puntos a 8 si desea clasificar por dias
    nuevodir = dirname + fecha
    if not os.path.exists(nuevodir):
        os.makedirs(nuevodir)
    else:
        shutil.move(rutayarchivo, nuevodir)

        


    
    
    
    
