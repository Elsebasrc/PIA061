## Practica 11 Escaneo de Puertos

En la siguiente practica se realizaron 4 scripts en python y 1 de ellos en IDLE, todos fueron hechos con  el objetivo de realizar diferentes formas de  escaner puertos.

El primer script fue [SCAN_PORT1.py](./SCAN_PORTV1.py) el cual con el uso de la libria de sockets  consistian  en solicitar un direccion ip y el rango de puertos a escanear
enotonces dependiendo de los valores  que recibieramos  de esos puertos 0 o 1 se crearon 2 lista una para los puertos que esten abiertos y  otro para los puertos cerrados y mostraba solo los puertos que estuvieran abiertos.

En el segundo script que fue [SCAN_PORT2.py](./SCAN_PORTV2.py) se realizo un escaneo,pero ahora establecemos una lista con los  puertos que  nosotros establescamos en el script y el escaneo a la red host con un rango de ip.

En el tercer script  [SCAN_PORT3.py](./SCAN_PORTV3.py) realiza practicamente lo mismo que el primer script la  unica modificcion que se realizo fue la implementacion de los hilos para que al momento de realizar el escaneo se creara  un hilo por cada cada puerto.

Y en el IDLE [SCAN_PORT4.py](./SCAN_PORTV4.py)usando modulos de nmap que previamente se tiene que instalar en el equipo, simplemente se hizo escaneo dependiendo los puertos de niuestro interes.

Por  ultimo se realizo en [menu_escaneos.py](./menu_escaneos.py) la recopilacion de 4 formas de hacer escaneos desde puertos hasta un ping en una ip. se le dio un formato con un menu para hacer uso de 4 metos distintos de escaneo.