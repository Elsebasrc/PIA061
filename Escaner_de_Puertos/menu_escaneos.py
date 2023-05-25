# Brian Sebastian  Reyna  Castillo 
import nmap
# Función para realizar un escaneo UDP
def escaneo_udp(ip, puerto):
    escaner = nmap.PortScanner()
    escaner.scan(ip, arguments='-sU -p {0}'.format(puerto))
    print(escaner.csv())

# Función para realizar un escaneo completo de puertos
def escaneo_completo(ip):
    escaner = nmap.PortScanner()
    escaner.scan(ip, arguments='-p-')
    print(escaner.csv())

# Función para detectar el sistema operativo
def deteccion_so():
    escaner  = nmap.PortScanner()
    escaner.scan(arguments='-O')
    print(escaner.csv())

# Función para realizar un escaneo de red con ping
def escaneo_ping(ip):
    escaner = nmap.PortScanner()
    escaner.scan(ip, arguments='-sP')
    print(escaner.csv())

while True:
    print("Menú ")
    print("1. Escaneo UDP")
    print("2. Escaneo completo")
    print("3. Detección de sistema operativo")
    print("4. Escaneo de red con ping")
    print("5. salir")
    
    opcion = input("Seleccione una opción indicando el numero : ")

    if opcion == "1":
        ip = input("Introduzca la dirección IP a escanear: ")
        puerto = input("Introduzca el número de puerto a escanear: ")
        escaneo_udp(ip, puerto)
    elif opcion == "2":
        ip = input("Introduzca la dirección IP a escanear: ")
        escaneo_completo(ip)
    elif opcion == "3":
        deteccion_so()
    elif opcion == "4":
        ip = input("Introduzca la dirección IP a escanear: ")
        escaneo_ping(ip)
    elif opcion== "5":
        exit()

    else:
        print("Opción inválida")