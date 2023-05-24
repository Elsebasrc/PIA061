#!/bin/bash
#
#escanear de puertos usando archivo especial en /dev
#
#DEfiniciones de variables 
direccion_ip=$1
puertos="20,21,22,23,25,50,51,53,80,110,119,135,136,137,138,139,143,161,162,389,443,445,636,1025,1443,3389,5985,5986,8080,10000"
#Verificamos que arametro de ip no vengan vacio
`[ $# -eq 0] && {echo"Modo de uso : $0 <192.168.100.239>"; exit 1; }`
#
#Bucle for ara cada puerto en $ppuertos
#
IFS=,
for port in $puertos
 do
	timeout 1 bash -c "echo > /dev/tcp/$direccion_ip/$ort > /dev/null 2>&1" &&\
	echo $direccion_ip":"$port" is open"\
	||\
	echo $direccion_ip":"$port"is closed
 done

