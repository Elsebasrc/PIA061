#Brian Sebastian  Reyna Castillo 2127309 
#Parte 1
import socket
#Parte 2
#se define lafuncionscan con la cual  
#seutilizan sockets ppara probar los diferentes puertos
def scan(addr, port):
    #Creando un  nuevo socket
    socket_obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #Establecemos el timeout  para  el  nuevo  objeto tipo socket 
    socket.setdefaulttimeout(1)
    #Conecion exitosa devuelve , Devuelve error  en  caso contrario        
    result= socket_obj.connect_ex((addr,port)) 
     #Direccion y puertos en  tupla
    #se  cierra el objeto
    socket_obj.close()
    return  result
#Parte 3
#lista de  puertos a escanear
ports=[21,22,25,80]
#Parte 4
#Bucle por  todas las ipp del rango 192.168.0.*
for i in range(1,255):
    addr="192.168.0.{}".format(i)
    for port in ports:
        result=scan(addr, port)
        if result==0:
            print (addr, port,"OK")
        else:
            print(addr,port, "Failed")
