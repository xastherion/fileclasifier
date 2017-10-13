import os, shutil

print ("--- Explicación ---")
print ('Este Script fue concebido para lograr un consenso en el nombre de las fotos')
print ('Algunos dispositivos nombran sus fotos con el prefijo IMG_ antes de la fecha')
print ('ya que nuestro objetivo es clasificar las fotos de todos los dispositivos por fechas (meses) ')
print ('entonces esta nominacion no nos favorece. ')
print ('') 
       
dirname=input('Introduzca la ruta completa a su carpeta, un slash al final es importante  :  ')

# dirname = "D:\\FREIGABE\\MEDIA\\FOTOS\\08.05.2017\\" 

navegadir = os.listdir(dirname)

for elemento in navegadir:
    print ('-------------------------------------')
    print (elemento)
    rutayarchivo = dirname + elemento
    print (rutayarchivo)
    esdir = os.path.isfile(rutayarchivo) #<-- respuesta booleana true is file, false es directorio
    print (esdir)
    nombrearchivo = elemento[3:] # <-- cambie el numero despues de los dos puntos a 8 si desea clasificar por dias
    print (nombrearchivo)
    nuevodir = dirname + nombrearchivo
    print (nuevodir)
    shutil.move(rutayarchivo, nuevodir) # <-- renombra el archivo quitandole el IMG_ ó el VID_

""" como encontrar la fecha en las fotos?
algunas fotos son renombradas automaticamente

Android:
20170701_141404.jpg
20170701_164008.mp4

WinMo :
IMG_20160524_115305.jpg
VID_20160524_115128.mp4

como aqui no nos interesa el prefijo IMG_ o VID_ queremos eliminarlo.
la opcion mas sencilla seria, contar [4:]  Pero la mas útil seria descubrir la
fecha puesto que contar 4 no se podría aplicar en una carpeta con nombres
correctos

una opcion que seria valida para estos dos nombres sería contar 8+1+6 desde la izq
a partir del punto

el 20 del anno 2017 y posteriores tambien podria ser un comienzo, aunque combinado
con otro metodo ya que podria encontrarse otro 20 en el nombre.

"""



        


    
    
    
    
