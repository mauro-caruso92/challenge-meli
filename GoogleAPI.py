from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def APIDriveConnect(prog='drive'):

    SCOPES =  ['https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/drive']
    creds = None
    
    # El archivo token.pickle almacena los tokens de acceso y actualización del usuario,
    # y se crea automáticamente cuando el flujo de autorización se completa por primera vez.
    
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            
    # Si no hay credenciales (válidas) disponibles, permite que el usuario inicie sesión.

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Guarda las credenciales para la próxima ejecución.
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)


     # Llamada a la API v3 de Drive.
    if prog == 'drive':
        service = build(prog, 'v3', credentials=creds)
        return service
    
    service = build(prog, 'v1', credentials=creds)
    return service
