## Practica 06 Scripting en Bash.

En esta praactica realizamos diferentes codigos en bash para visualizar su funcionamiento como el recibir datos de entrada y mostrarlos en variables y tambien un escaneo de puertos y por ultimo realizamos un menu que nos desplegara diferentes opciones.

Realizamos 3 scripts en bash basicos:
El primero de ellos fue [bro.sh](./bro.sh) que  simplemente nos pedia ingresar nuestro nombre y  nos  devolvia un saludo con el respectivo nombre.

El segundo fue [welcome.sh](./welcome.sh)  simplemente con  el nombre de usuario que se almacena en laa variable de $LOGNAME nos genera un saludo  y  la  fecha.despues nos despleglaba los  usuarios que estaban  conectados  y los  procesos que se realizan.

El tercero fue [number.sh](./number.sh) simplemente le pedia al usuario 3 numeros y los mostaba en pantalla 

Despues se realizaron 3 scripts para hacer escaneos de puertos

El primero fue  [netdiscover.sh](./netdiscover.sh) el cual lo usamos para verificar y saber cual es nuestra subred devolviendonos una ip.

Despues en [portsca.sh](./portscanv1.sh) se escanaba la ip para verificar que puertos se encontraban abiertos o cerrados.

Y por ultimo hicimos un script llamado [superscan.sh](./superscan.sh) que lo que hace es desplegar  un menu con  diferentes funciones, en este caso incluimos cuatro, que son [netdiscover.sh](./netdiscover.sh),[portsca.sh](./portscanv1.sh) ,  [welcome.sh](./welcome.sh) y por ultimo una salida del  script [exit].