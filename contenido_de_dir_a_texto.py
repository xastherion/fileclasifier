import os
elemento = ""
dirname = "D:\\FREIGABE\\MEDIA\\FOTOS\\08.05.2017" # <-- Aceptar parametros
mitexto = os.listdir(dirname)
 
f = open("fichero.txt", 'w')
for elemento in mitexto:
    print (elemento + ', ')
    f.write(elemento + ', ')

f.close()
 

