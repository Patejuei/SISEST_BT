import mysql.connector as db
import yagmail
import os
from dotenv import load_dotenv
import datetime

from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor


class Conexion:
    connection : MySQLConnection
    cursor : MySQLCursor
    def __init__(self):
        load_dotenv()
        self.connection = db.connect(
            host = os.getenv('DB_HOST'),
            port = os.getenv('DB_PORT'),
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'),
            database = os.getenv('DB_NAME')
        )
        self.cursor = self.connection.cursor()


    def srcVols(self, source):
        
        self.cursor.execute(f"SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos WHERE reg_gral LIKE '{source}%'")
        _search = self.cursor.fetchall()
        
        return _search

    def srcLista(self, srcLista):
        self.cursor.execute(
            f'''SELECT
                    corr_cia, 
                    DATE_FORMAT(fecha, '%d-%m-%Y'), 
                    acto, 
                    direccion 
                FROM actos 
                WHERE 
                    corr_cia like '{srcLista}%' OR direccion LIKE '%{srcLista}%'
                ORDER BY 
                    fecha desc, 
                    corr_cia DESC''')
        _SrcResults = self.cursor.fetchall()
        return _SrcResults

    def extVols(self, corrCia):
        self.connection.connect()
        self.cursor.execute(
            f'SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos b INNER JOIN asistencia a ON a.reg_gral_voluntario = b.reg_gral WHERE a.corr_cia_acto = "{corrCia}"')
        result = self.cursor.fetchall()
        self.connection.close()
        return result


    def addVolLista(self, vol):
        self.connection.connect()
        self.cursor.execute(f'SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos WHERE reg_gral = "{vol}"')
        result = self.cursor.fetchall()[0]
        self.connection.close()
        
        return result


    def getYear(self):
        self.connection.connect()
        years = [""]
        self.cursor.execute("SELECT YEAR(fecha) FROM actos GROUP BY year(fecha)")
        for ye in self.cursor.fetchall():
            years.append(str(ye[0]))
        self.connection.close()
        return years

    def getActos(self):
        self.connection.connect()
        self.cursor.execute('SELECT corr_cia, acto, corr_gral, fecha, direccion, lista, unidad FROM actos ORDER BY fecha DESC, corr_cia DESC')
        result = self.cursor.fetchall()
        self.connection.close()
        return result

    def delLista(self, cCia):
        self.connection.connect()
        self.cursor.execute(f'DELETE FROM asistencia WHERE corr_cia_acto = "{cCia}"')
        self.cursor.execute(f'DELETE FROM actos WHERE corr_cia = "{cCia}"')
        self.connection.commit()
        self.connection.close()
        

    def getVols(self):
        self.connection.connect()
        self.cursor.execute(f'SELECT * FROM bomberos')
        result = self.cursor.fetchall()
        self.connection.close()
        return result

    #TODO: Pasar a Informes
    def getArrastre(self, date_s, date_l):
        
        arrastre = open(os.path.abspath('resources/styles.html'), 'r').read()
        self.cursor.execute(
            f'SELECT direccion, acto, DATE_FORMAT(fecha, "%d-%m-%Y"), corr_gral, corr_cia, lista FROM actos WHERE fecha BETWEEN STR_TO_DATE("{date_s}", "%d-%m-%Y") AND STR_TO_DATE("{date_l}", "%d-%m-%Y")')
        for row in self.cursor.fetchall():
            direccion, acto, fecha, corr_gral, corr_cia, lista = row
            header = f'<table> <tr> <td class="c1">Direccion: </td><td class="c2">{direccion}</td></tr>' \
                     f'<tr><td class="c1">Acto: </td><td class="c2">{acto}</td></tr>' \
                     f'<tr><td class="c1">Fecha: </td><td class="c2">{fecha}</td></tr>' \
                     f'<tr><td class="c1">Correlativo General: </td><td class="c2">{corr_gral}</td></tr>' \
                     f'<tr><td class="c1">Correlativo de Compañía: </td><td class="c2">{corr_cia}</td></tr>' \
                     f'<tr><td class="c1">Lista</td><td>{lista}</td class="c2"></tr><br>'
            content = '<tr><th>Registro General</th><th>Nombre</th></tr>'
            self.cursor.execute(
                f'SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos INNER JOIN asistencia a on bomberos.reg_gral = a.reg_gral_voluntario WHERE corr_cia_acto = "{corr_cia}" AND sub_estado = "ACTIVO" ORDER BY reg_gral')
            for vol in self.cursor.fetchall():
                reg_gral, nombre, apellidoP, apellidoM = vol
                content += f'<tr><td class="c1">{reg_gral}</td><td class="c2">{nombre} {apellidoP} {apellidoM}</td></tr>'
            arrastre += header + content + "</table><br>"
            
        return arrastre

    #TODO: pasar a informes
    def getInformePersonal(self, rGral):
        # Primera hoja : Asistencia x Año
        
        asistencia = []
        self.cursor.execute("SELECT YEAR(fecha) from actos GROUP BY YEAR(fecha)")
        years = self.cursor.fetchall()
        for n in range(len(years)):
            asistencia.append([years[n][0]])
            self.cursor.execute(f"SELECT count(corr_cia) FROM actos INNER JOIN asistencia a on actos.corr_cia = a.corr_cia_acto WHERE YEAR(fecha) = {years[n][0]} AND a.reg_gral_voluntario = '{rGral}'")
            asistencia[n].append(self.cursor.fetchone()[0])
            self.cursor.execute(f"SELECT count(corr_cia) FROM actos WHERE YEAR(fecha) = {years[n][0]}")
            asistencia[n].append(asistencia[n][1]/self.cursor.fetchone()[0])
            self.cursor.execute(f"SELECT count(corr_cia) FROM actos INNER JOIN asistencia a on actos.corr_cia = a.corr_cia_acto WHERE YEAR(fecha) = {years[n][0]} AND a.reg_gral_voluntario = '{rGral}' AND lista = 'OB'")
            asistencia[n].append(self.cursor.fetchone()[0])
            self.cursor.execute(f"SELECT count(corr_cia) FROM actos WHERE YEAR(fecha) = {years[n][0]} AND lista = 'OB'")
            asistencia[n].append(asistencia[n][3]/self.cursor.fetchone()[0])
        # Segunda Hoja : Actos
        self.cursor.execute(f"SELECT corr_cia, acto, corr_gral, fecha, direccion, lista FROM actos INNER JOIN asistencia a on actos.corr_cia = a.corr_cia_acto WHERE a.reg_gral_voluntario = '{rGral}' ORDER BY fecha DESC, corr_cia DESC")
        actos = self.cursor.fetchall()
        
        return asistencia, actos

    def getVolsInfoPers(self):
        self.connection.connect()
        vols = []
        self.cursor.execute("SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos")
        for vol in self.cursor.fetchall():
            rGral, nombre, apellidoP, apellidoM = vol
            vols.append(f"{rGral} - {nombre} {apellidoP} {apellidoM}")
        self.connection.close()
        
        return vols

    #TODO: Crear Clase Licencias.py


    #Retornar Nombre para el campo
    def get_nameVols(self, nReg):
        
        query = f"SELECT nombre, apellidoP, apellidoM FROM bomberos WHERE reg_gral = '{nReg}'"
        self.cursor.execute(query)
        nom, apeP, apeM = self.cursor.fetchone()
        nombre = f'{nom} {apeP} {apeM}'
        
        return nombre

    # Retornar Lista de Licencias.py
    def get_ListLic(self, inp):
        
        query = f"SELECT corr_Lic, b.nombre, b.apellidoP, b.apellidoM, f_desde, f_hasta FROM licencias INNER JOIN bomberos b on nro_registro = b.reg_gral WHERE b.nombre LIKE '{inp}%' OR b.apellidoP LIKE '{inp}%' ORDER BY corr_Lic DESC"
        self.cursor.execute(query)
        licencias = self.cursor.fetchall()
        
        return licencias

    # Retornar contenido de licencias
    def get_LicCont(self, CLic):
        
        query = f"SELECT corr_Lic, nro_registro, f_desde, f_hasta, motivo, aprobado FROM licencias WHERE corr_Lic='{CLic}'"
        self.cursor.execute(query)
        licencia=self.cursor.fetchone()
        
        return licencia

    # Eliminar Licencia
    def deleteLicencia(self, corr_Lic):
        
        sql = f'DELETE FROM licencias WHERE corr_Lic = "{corr_Lic}"'
        self.cursor.execute(sql)
        self.connection.commit()
        

