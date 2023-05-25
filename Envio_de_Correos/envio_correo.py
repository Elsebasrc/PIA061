#Brian Sebastian Reyna Castillo 2127309     
#importammos las llibrerias necesarias ppara establlecer la conexion conn gmail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
#establecemos de donde y a quien se ennviara el correo
origen='brianrc94@gmail.com'
destino=' gerardo.bernal@uanl.edu.mx '
#hacemos la ppeticion de acceso de conexion a SMTP para poder connectarnos y enviar correos
conn=smtplib.SMTP('smtp.gmail.com',  587)
conn.starttls()
conn.login(origen,'ingrese password')#debe ingresar el password y correo de aplicacion para que funcionne
#hacemos la creacion del mensaje a enviar en formato html
mensaje= MIMEMultipart()
mensaje['From']=origen
mensaje['To']= destino
mensaje['Subject']='Prueba de envio (script python)-2127309'

html="""
        <html>
            <head>
            </head>        
            <body>
                <p> 
                    <img src='https://plataformanexus.uanl.mx/Contenedores%20L%2FContenedor_6629%2F2696_30-01-2023_02-52-19_1511055692.png' height="250" <br><br><br>
                    <strong>Practica 12</strong> <br><br>
                    Ejercicio de la practica 12 para envio de correos<br><br>
                    <strong>Alumno:</strong> Brian Sebastian Reyna Castillo'<br><br>
                    <strong>Matricula:</strong> 2127309
                </p>    
        </html>"""

#inndicammos que el formato que se envia es un htmml y lo adjuntammos ya en un archivo listo para enviar 
mensaje.attach(MIMEText(html,'html'))
#ennviammos el mensaje elaborado
conn.sendmail(origen,destino,mensaje.as_string())
#salimos de la conexion SMTP
conn.quit()
