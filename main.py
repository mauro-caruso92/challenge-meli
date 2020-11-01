from __future__ import print_function
from database import *
from GoogleAPI import APIDriveConnect
from email.mime.text import MIMEText

import json
import mysql.connector
import smtplib
import sys
import base64

from email.mime.text import MIMEText as text

def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text, 'html')
    message['to'] = sender
    message['from'] = to
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def main():

    try:
        miBD = MySql('localhost','root','root')
        print(' "Conexion Exitosa"')
    except Exception:
        print("Error al iniciar la base de datos")
        sys.exit(1)

    try:
        service = APIDriveConnect()
        results = service.files().list(
            pageSize=1000, fields="nextPageToken, files(*)").execute()
        items = results.get('files', [])
    except Exception:
        print("Error al conectar con API de Google Drive")
        sys.exit(1)
    
    if not items:
        print('No se encontraron archivos en el drive')
    else:
        print('Listado de archivos encontrados:')

        for item in items:
            datos = [item['id'], item['name'], item['owners'][0]['emailAddress'], item['shared'], item['modifiedTime'], item['mimeType']]
            print("   - " + item['name'])
            miBD.sqldat(datos)
        print('Archivos modificados y guardados en Bitacora')
        
        for item in items:
            datoshist = (item['id'], item['name'], item['shared'])
            if ((item['shared'] == True)):
                miBD.sqlhist(datoshist)
                print("   - " + item['name'])
                
                service.permissions().delete(fileId=item['id'], permissionId='anyoneWithLink').execute()
                origen = 'Challenge.MELI.2020@gmail.com' 
                destino = '"'+item['owners'][0]['emailAddress']+'"' 
                msg= '\n Estimado, por cuestiones de seguridad, se modifico la visibilidad del archivo: "{0}" , para mayor informacion contacte con el Administrador.'.format(item['name']) #String que contiene el mensaje
                
                # Credenciales
                usuario = 'challenge.meli.2020@gmail.com'
                password = 'QWERT567zxc'
                
                # Envio del correo
                gmail = APIDriveConnect('gmail')
                asunto = 'Documento Drive - Cambio de visibilidad'
                send_message = create_message(origen, destino, asunto, msg)
                gmail.users().messages().send(userId=usuario, body=send_message).execute()

                resp = datos[0]
                miBD.sqlupdt(datos[0])
                print(" El usuario "+ destino + " fue notificado:")

        miBD.close_bd()
        return None
                

if __name__ == '__main__':
    main()

print("")
print(" Fin de la ejecucion")

