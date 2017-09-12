# fileclasifier

Este es un script que programe para organizar las fotos.
Yo se que hay herramientas fantasticas como google-fotos o iPhotos, Picasa, etc, etc. Pero no me dan confianza.
No porque repartan mis fotos en internet (aunque eso tambien) sino porque lo hacen todo automatico y de pronto
ya no hay mas fotos.
Es uso de este Script es un poco mas complicado, pero seguro. Tambien es mas simple: no reconoce caras ni las
clasifica por los lugares donde estuviste.

Para ver de que se trata, lo mejor es ver de que se trata:

Conectas tu telefono con tu computadora y accedes a tu carpeta de Fotos (normalmente DCIM). Copias la carpeta con
TODAS las fotos de tu telefono manualmente con Copy&Paste o con arrastre en alguna carpeta local como 
/users/tunombre/escritorio o /MISFOTOS etc.

Corres el script fileclasifier y le das el camino a esa carpeta.

La magia del script es que creara carpetas segun los meses de las fotos, asi si la foto es 
23122017_142330.jpg creara una carpeta 2017-12 y meterá esta foto adentro. Si hay mil fotos en ese mes
la carpeta contendra despues tambien mil fotos.

Si hay fotos tomadas en meses diferentes, el script creara una carpeta para cada mes.
al final tendras un directorio mas o menos asi:

escritorio/dcim/
escritorio/dcim/2017-11
escritorio/dcim/2017-12

y asi. Si tienes fotos de todo el año, tendras 12 carpetas.

======= SCRIPT COMPARAR =======
Como despues es dificil de comparar si todas las fotos estan donde debieran, he creado el script comparar,
que no hace mas que contar cuantos archivos (en este caso fotos) hay en todas las carpetas segun la raíz dada

======= SCRIPT CAMBIAR_NOMBRE =======
Si, como yo, tienes un servidor donde descargas las fotos de tu handy, de el de tu pareja, tus hijos, amigos, etc.
encontrarás otro problemilla: los nombres de fotos no son estandar, asi en Android nuevo son como arriba, pero tengo 
Un Android viejo y un WinPhone que agrega el prefijo IMG a todas las fotos y MOV a todos los videos. Personalmente
esto me disgusta y me parece inutil, ya que las fotos y videos tienen sus extensiones .jpg o .mp3 oder .avi. Por esto
he creado el script cambiar_nombre para trabajar esto

======= SCRIPT UNIFICADO ======= en projecto
Este script es para los flojos que quieren correr todo en uno al mejor estilo de los programas. Bueno, yo he creado estos
script para aprender un poco mas de python y cumplir un requerimiento propio. Si te sirve de algo me alegraria saberlo con
algun like o comentario

======= FIN =======
Cuando estas satisfecho con los resultados puedes borrar el origen en tu telefono. No olvides nunca tener copia doble de tus archivos importantes!
