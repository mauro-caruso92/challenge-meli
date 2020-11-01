import mysql.connector


class MySql():
    def __init__(self, _host, _usuario, _pass):
        self.db = mysql.connector.connect(
        host = _host,
        user = _usuario,
        passwd = _pass
        )
        self.cursor = self.db.cursor()
        self.crearDB(_host, _usuario, _pass)

    def crearDB(self,_host,_usuario,_pass):

        self.cursor.execute("CREATE DATABASE IF NOT EXISTS bbdd_docsdrive")

        self.db = mysql.connector.connect(
        host = _host,
        user = _usuario,
        passwd = _pass,
        database = 'bbdd_docsdrive'
        )
        self.cursor = self.db.cursor()
        self.db.commit()
        self.crearDrive()
        self.crearBitacora()


    def crearDrive(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS docsdrive"
                    "(id VARCHAR(100),"
                    "name VARCHAR(100),"
                    "owners VARCHAR(100),"
                    "shared VARCHAR(100),"
                    "modifiedTime VARCHAR(100),"
                    "mimeType VARCHAR(100))")
        self.db.commit()

    def crearBitacora(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS log"
                    "(id VARCHAR(100),"
                    "name VARCHAR(100),"
                    "shared VARCHAR(100))")
        self.db.commit()

    def sqldat(self, _datos):
        n_id = _datos[0] 
        name = _datos[1] 
        owners = _datos[2] 
        shared = _datos[3] 
        modifiedTime = _datos[4] 
        mimeType = _datos[5]
        params = [n_id, name, owners, shared, modifiedTime, mimeType]

        query = "SELECT * FROM docsdrive WHERE (id='{0}')".format(n_id)
        self.cursor.execute(query)
        resp = self.cursor.fetchall()
        
        if len(resp) == 0:
            query = "INSERT INTO docsdrive(id, name, owners, shared, modifiedTime, mimeType) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(query, params)
            self.db.commit()


    def sqlhist(self, _datoshist):

        n_id = _datoshist[0] 
        name = _datoshist[1] 
        shared = _datoshist[2] 
        params = [n_id, name, shared]
        query = "INSERT INTO log(id, name, shared) VALUES (%s, %s, %s)"
        self.cursor.execute(query, params)
        self.db.commit()

    def sqlupdt(self, n_id):
        query = "UPDATE docsdrive SET shared='0' WHERE (id='{0}')".format(n_id)
        self.cursor.execute(query)
        self.db.commit()
    
    def close_bd(self):
        self.cursor.close()
        self.db.close()