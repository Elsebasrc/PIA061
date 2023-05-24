## Practica 05 Scripting en Powershell

En  esta practica  se hizo el uso de  powershell para  obtener los datos de  tu gatway , asi como  tambien el  escaneo de puertos  para verificar si estan abiertos o  cerrados.

En  [scan_alivev](./scan_alivev.ps1) podemos observar que este script se encarga de obtener la direccion de enlace  de  nuestra maquina (gateway).

En [scan_alivev2](./scan_alivev2.ps1) en este script podemos observar que  primero  recibiremos nuestra direccion de gateway  y una  ves obtenida comienza a buscar el rango  de subret que tenemos y nos la muestra.

En[scan_portv](./scan_portv1.ps1) en este esscrip  al igual que el [scan_alivev2](scan_alivev2.ps1) al inicio obtenemos los mismos resultaados, solo que ahora se ingreso una lista de puertos a escanear por lo que nos solicita una ip para verificar si esos puertos estan  abiertos.