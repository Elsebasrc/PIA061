#Brian Sebastian  Reyna Castillo 2127309 
#Parte 1 importar  librerias
import sys
import  threading
from socket  import *
#Parte 2 creamos funcion  tcp_test
def tcp_test(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip,port))
    if result == 0: 
        print('opened port :', port)
#Parte 3 establecemos el main del  script
if  __name__=='__main__':
    host = sys.argv[1]
    portstrs=  sys.argv[2].split('-')
#parte 4
start_port= int(portstrs[0])
end_port= int(portstrs[1])
#Parte 5
target_ip= gethostbyname(host)
#Parte 6
#Se inicia bucle para probar puertos
hilos=[]
for port in range(start_port, end_port):
    hilo=threading.Thread(target=tcp_test, args=(port,))
    hilos.append(hilo)
    hilo.start()
