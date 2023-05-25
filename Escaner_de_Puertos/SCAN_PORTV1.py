#Brian Sebastian  Reyna Castillo 2127309 
#UDP
#!/usser/bin/python
#-*- coding: utf-8 -*-

#Parte1
#importamos libreiras necesarias
import sys
from socket import *
#Parte 2 ejecucion del script 
#port_scan/py<host> <start_port>-<end__port>
#Primer arumento se guarde en variables  host
#Segundo argumento se guarda en variable portstrs
host = sys.argv[1]
portstrs= sys.argv[2].split('-')
#Parte 3
#portstrs contiene dos valores de  inicio
#en end_port el valor fin
start_port = int(portstrs[0])
end_port= int(portstrs[1])
#Parte 4
#Para  usar en el  socket  asignados lo de la  
# variable hosst  a target_ip
# Definimos  una lista  de  puertos open_ports
target_ip= gethostbyname(host)
opend_ports = []
#Parte 5 
#Iniciamos bucle for para probar ppuertos
for port in  range(start_port, end_port):
    sock= socket(AF_INET,  SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        opend_ports.append(port)
#Parte 6
print(' Opened ports :')
for i in opend_ports:
    print(i)
