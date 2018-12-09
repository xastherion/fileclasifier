# fileclasifier

Este es una coleccion de scripts en python que programé para organizar Fotos.
Yo sé que hay herramientas fantásticas como google-fotos o iPhotos, Picasa, etc, etc. Pero no me dan confianza.
No sólo porque repartan mis fotos en internet, sino también porque lo hacen tan automático que de pronto
ya no hay mas fotos.

El uso de este Script es un poco mas complicado, pero mucho más seguro. También es mas simple: no reconoce caras ni las clasifica por los lugares donde estuviste.

Para ver de que se trata, lo mejor es ver como se usa:

Conectas tu telefono con tu computadora y accedes a tu carpeta de Fotos (normalmente DCIM). Copias la carpeta con
TODAS las fotos de tu telefono manualmente con Copy&Paste o con arrastre en alguna carpeta local como 
/users/tunombre/escritorio o /MISFOTOS etc.

Corres el script fileclasifier y le das el camino a esa carpeta.

La magia del script es que creará carpetas según los meses de las fotos, así si la foto es 
23122017_142330.jpg creara una carpeta 2017-12 y meterá esta foto adentro. Si hay mil fotos en ese mes
la carpeta contendra despues también mil fotos.

Si hay fotos tomadas en meses diferentes, el script creara una carpeta para cada mes.
al final tendrás un directorio mas o menos asi:

escritorio/dcim/
escritorio/dcim/2017-11
escritorio/dcim/2017-12

y asi. Si tienes fotos de todo el año, tendras 12 carpetas.

======= SCRIPT COMPARAR =======
Como despues es dificil de comparar si todas las fotos estan donde debieran, he creado el script comparar,
que no hace mas que contar cuantos archivos (en este caso fotos) hay en todas las carpetas segun la raíz dada.

======= SCRIPT CAMBIAR_NOMBRE =======
Si como yo, tienes un servidor donde descargas las fotos de tu handy, de el de tu pareja, tus hijos, amigos, etc.
encontrarás otro problemilla: los nombres de fotos no son estandar, asi en Android nuevo son como arriba, pero tengo 
Un Android viejo y un WinPhone que agrega el prefijo IMG a todas las fotos y MOV a todos los videos. Personalmente
esto me disgusta y me parece inutil, ya que las fotos y videos tienen sus extensiones .jpg o .mp3 oder .avi. Por esto
he creado el script cambiar_nombre para trabajar esto. Pronto estare probando y adicionando la funcionalidad para iOS.

======= SCRIPT UNIFICADO ======= en projecto
Este script es para los flojos que quieren correr todo en uno al mejor estilo de los programas. Bueno, yo he creado estos
script para aprender un poco mas de python y cumplir un requerimiento propio. Si te sirve de algo me alegraria saberlo con
algun like o comentario, idea o crítica.

======= FIN =======
Cuando estas satisfecho con los resultados puedes borrar el origen en tu telefono. No olvides nunca tener copia doble de tus archivos importantes!
