import os, shutil, filecmp
numelement=0
numelement2=0

dirname1=input('Introduzca la ruta completa a su carpeta, un slash al final es importante :  ')
#dirname2=input('La otra carpeta?... : ')

navegadir = os.listdir(dirname1)

# print(curdir)
for elemento in navegadir:
    numelement=numelement+1
    #print (numelement) # <-- imprime el numero de elementos en el directorio raiz
    otrodir=dirname1+elemento
    navegadir2 = os.listdir(otrodir)
    #print (otrodir)
    for elemento2 in navegadir2:
        print (elemento2) # <-- imprime el nombre del archivo
        numelement2=numelement2+1
        print(numelement2) # <-- imprime el numero total
'''
filecmp.cmpfiles(dirname1, dirname2, common, shallow=True)
os.chdir(curdir) <-- cambia el directorio activo a curdir
'''
    
    
    
    
