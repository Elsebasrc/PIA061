import requests
import json
if __name__== '__main__':
    url='http://httpbin.org/post'
    argumentos= {'nombre':'Brian Sebastian','matricula':'2127309','curso':'Progamacion para ciberseguridad'}

    response = requests.post(url, params=argumentos)

    if response.status_code==200:
        print(response.content)


#Nombre:Brian Sebastian Reyna Castillo
#Matricula: 2127309