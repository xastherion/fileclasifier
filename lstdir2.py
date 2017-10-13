import os, shutil
dirname = "D:\\FREIGABE\\MEDIA\\FOTOS\\08.05.2017\\" 
navegadir = os.listdir(dirname)

for elemento in navegadir:
    rutayarchivo = dirname + elemento
    print (rutayarchivo)
    esdir = os.path.isfile(rutayarchivo) #<-- respuesta booleana true is file, false es directorio
    print (esdir)
    fecha = elemento[:8]
    print (fecha)
    nuevodir = dirname + fecha
    print (nuevodir)
    if not os.path.exists(nuevodir):
        os.makedirs(nuevodir)
    else:
        shutil.move(rutayarchivo, nuevodir)
    
    
    
    
