# Challenge MercadoLibre!
## Consigna
Desarrollar una aplicación para inventariar en una Base de Datos todos los archivos pertenecientes a la unidad de Drive de un usuario. La base de datos debe ser creada desde la aplicación, pudiéndose utilizar cualquier motor (por ejemplo MySQL o Redis). Dicha base deberá almacenar el nombre del archivo, la extensión, el owner del archivo, la visibilidad (público o privado) y la fecha de última modificación.

En el caso de encontrar archivos que estén configurados como públicos y puedan ser accedidos por cualquier persona, deberá modificar dicha configuración para establecer el archivo como privado y enviar un e-mail al owner notificando el cambio realizado.

La aplicación deberá tener la lógica necesaria para guardar en la base sólo aquellos archivos que no hayan sido almacenados en alguna corrida anterior o actualizar la fecha de modificación o cualquier otro dato en caso de corresponder. Asimismo, deberá mantener un inventario histórico de todos los archivos que fueron en algún momento públicos.

Esta aplicación debe ser desarrollada en Python y deberá contar con tests que verifiquen su buen funcionamiento.

**Bonús:**

 - Aplicar buenas prácticas de programación. 
 - Documentación y bibliografía consultada. 
 - Tratamiento seguro de las credenciales utilizadas. 
 - Dockerizar la aplicación.

Cuanto más fácil sea reproducir el challenge, mejor :)

# Pasos para la ejecución

 1. Descargar los archivos del siguiente link https://github.com/mauro-caruso92/challenge-meli 
 2. Previo a la ejecución se deberá contar con MySQL Server instalado.
 3. En la consola, ingresar al directorio donde se alojan los archivos e instalar las librerías que utiliza la aplicación. Para ello se deberá escribir la siguiente línea de comando: **pip install -r requirements.txt**
 4. Luego de la instalación del requirements.txt, se deberá proceder a ejecutar el comando **python main.py**


# Código fuente
## Base de datos

El archivo database.py contiene la creación de la base de datos **bbdd_docsdrive** utilizada en la aplicación, en la cual se generan 2 tablas:

 - tabla docsdrive con los siguientes campos
|id|name|owners|shared|modifiedTime|mimeType|
 - tabla log con los siguientes campos
|id|name|shared|

Adicionalmente, se utilizaron las funciones:

 - crearDB: se ejecuta en caso que la base de datos no se encuentre creada.
 - crearDrive: se ejecuta en caso que no se encuentre creada la tabla de docsdrive
 - crearBitacora: se ejecuta en caso que no se encuentre creada la tabla de logs
 - sqldat: se ejecuta y genera registros de aquellos documentos que no fueron localizados previamente en el google drive.
 - sqlhist: se ejecuta cada vez que se realiza una actualización en los permisos de los documentos, con la posibilidad de trazear los cambios realizados en los documentos. 
 - sqlupdt: actualiza el valor de visibilidad de cada documento.
 - close_bd: cierre de base de datos

## GoogleAPI

Se definió la función APIDriveConnect la cual es necesaria para la conexión con Google Drive. Genera el archivo token.pickle el cual almacena los tokens de acceso. El archivo se crea automáticamente cuando el flujo de autorización se completa por primera vez.

## main
El main de la aplicación realiza la lógica principal luego de realizar las conexiones iniciales de la base de datos y la API de Google.
Se listan los archivos encontrados en el Google Drive al cual se encuentra conectada la aplicación (por medio de las credenciales cargadas en el archivo credentials.json) y evalúa si los mismos poseen permisos públicos o privados. En caso de ser públicos, la aplicación realiza modificaciones en la visibilidad del documento y es notificado al owner del documento.
En el archivo test.py se encuentra el mock test realizado para la aplicación. 


# Bibliografía consultada

A continuación se detalla la bibliografía consultada

 - https://developers.google.com/
 - https://stackoverflow.com/
 - https://docs.python.org/3/library/unittest.mock.html
 - https://rico-schmidt.name/pymotw-3/
 - https://www.programcreek.com/python/example/72607/mock.PropertyMock
