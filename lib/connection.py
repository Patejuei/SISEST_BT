import mysql.connector as db
import yagmail
import os
class Conexion:
    def __init__(self):
        self.data = eval(open(os.path.abspath('params.txt'), 'r').read())
        self.conecta = db.connect(host=self.data['Host'],
                                  user=self.data['User'],
                                  password=self.data['Password'],
                                  database=self.data['DataBase'])
        self.cursor = self.conecta.cursor()

    def addLista(self, *params):
        Corr_Cia, acto, corr_gral, fecha, direccion, lista, cvols, vols = params
        query = f"INSERT INTO actos VALUES ('{Corr_Cia}', '{acto}', {corr_gral}, STR_TO_DATE('{fecha}','%d-%m-%Y'), '{direccion}', '{lista}', {cvols})"
        self.cursor.execute(query)
        for vol in vols:
            self.cursor.execute(f"INSERT INTO asistencia VALUES (default, '{Corr_Cia}', '{vol}')")
        self.conecta.commit()

    def srcVols(self, source):
        self.cursor.execute(f"SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos WHERE reg_gral LIKE '{source}%'")
        busqueda = self.cursor.fetchall()
        return busqueda

    def addVols(self, *source):
        rGral, rCia, nombre, apellidoP, apellidoM, crut, email, fIngreso, sub_estado = source
        rut = crut.split('-')
        dv = rut[1]
        rut = int(rut[0])
        self.cursor.execute(f'INSERT INTO bomberos VALUES ("{rGral}", "{nombre}", "{apellidoP}", "{apellidoM}", "{email}", {rut}, "{dv}", {rCia}, STR_TO_DATE("{fIngreso}", "%d-%m-%Y"), "{sub_estado}")')
        self.conecta.commit()

    def srcLista(self, srcLista):
        self.cursor.execute(f'SELECT corr_cia, DATE_FORMAT(fecha, "%d-%m-%Y"), acto, direccion FROM actos WHERE corr_cia like "{srcLista}%" OR direccion LIKE "%{srcLista}%" ORDER BY fecha desc, corr_cia DESC')
        busq = self.cursor.fetchall()
        return busq

    def extVols(self, corrCia):
        self.cursor.execute(
            f'SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos b INNER JOIN asistencia a ON a.reg_gral_voluntario = b.reg_gral WHERE a.corr_cia_acto = "{corrCia}"')
        result = self.cursor.fetchall()
        return result

    def editLista(self, *params):
        corr_cia, acto, corr_gral, fecha, direccion, lista, cvols, vols = params
        self.cursor.execute(
            f'UPDATE actos SET acto="{acto}", fecha=STR_TO_DATE("{fecha}","%d-%m-%Y") , corr_gral={corr_gral}, direccion="{direccion}", lista="{lista}", c_vols={cvols} WHERE corr_cia = "{corr_cia}"')
        self.cursor.execute(f'DELETE FROM asistencia WHERE corr_cia_acto = "{corr_cia}"')
        for vol in vols:
            self.cursor.execute(f'INSERT INTO asistencia VALUES (default, "{corr_cia}", "{vol}")')
        self.conecta.commit()

    def addVolLista(self, vol):
        self.cursor.execute(f'SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos WHERE reg_gral = "{vol}"')
        result = self.cursor.fetchall()[0]
        return result

    def editVol(self, *params):
        rGrali, rGral, rCia, nombre, apellidoP, apellidoM, crut, email, fIngreso, sub_estado = params
        rut = crut.split('-')
        dv = rut[1]
        rut = int(rut[0])
        self.cursor.execute(f'UPDATE bomberos SET reg_gral = "{rGral}",nombre = "{nombre}", apellidoP = "{apellidoP}", apellidoM = "{apellidoM}", email = "{email}", rut = {rut}, dv = "{dv}", reg_cia = {rCia}, f_ingreso = STR_TO_DATE("{fIngreso}", "%d-%m-%Y"), sub_estado = "{sub_estado}" WHERE reg_gral = "{rGrali}"')
        self.conecta.commit()

    def resMensual(self, month, year):
        lista = []
        self.cursor.execute('SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos where sub_estado = "ACTIVO"')
        for row in self.cursor.fetchall():
            lista.append(list(row))
        for row in lista:
            self.cursor.execute(f'SELECT count(corr_cia_acto) FROM asistencia INNER JOIN actos a on asistencia.corr_cia_acto = a.corr_cia WHERE MONTHNAME(a.fecha) = "{month}" AND YEAR(a.fecha) = {year} and reg_gral_voluntario = "{row[0]}" AND NOT (a.acto in ("C. ADM.","J. OFF", "CONS. DISC"))')
            lista[lista.index(row)].append(self.cursor.fetchall()[0][0])
            self.cursor.execute(f'SELECT count(corr_cia) FROM actos WHERE MONTHNAME(fecha) = "{month}" AND YEAR (fecha) = {year} AND NOT (acto in ("C. ADM.","J. OFF", "CONS. DISC"))')
            lista[lista.index(row)].append(row[4] / self.cursor.fetchall()[0][0])
            self.cursor.execute(f'SELECT count(corr_cia_acto) FROM asistencia INNER JOIN actos a on asistencia.corr_cia_acto = a.corr_cia WHERE MONTHNAME(a.fecha) = "{month}" AND YEAR(a.fecha) = {year} and reg_gral_voluntario = "{row[0]}" AND a.lista = "OB"')
            lista[lista.index(row)].append(self.cursor.fetchall()[0][0])
            self.cursor.execute(f'SELECT count(corr_cia) FROM actos WHERE MONTHNAME(fecha) = "{month}" AND YEAR (fecha) = {year} AND lista = "OB"')
            lista[lista.index(row)].append(row[6] / self.cursor.fetchall()[0][0])
        self.cursor.execute(f'SELECT * FROM actos WHERE MONTHNAME(fecha) = "{month}" AND YEAR(fecha) = {year} ORDER BY fecha DESC, corr_cia DESC')
        actos = self.cursor.fetchall()
        estadistica = []
        # Incendios
        self.cursor.execute(f"SELECT count(corr_cia) FROM actos WHERE MONTHNAME(fecha) = '{month}' AND YEAR(fecha) = {year} AND acto = 'INCENDIO'")
        estadistica.append(['Incendios', self.cursor.fetchone()[0]])
        # Forestales
        self.cursor.execute(f"SELECT count(corr_cia) FROM actos WHERE MONTHNAME(fecha) = '{month}' AND YEAR(fecha) = {year} AND acto = 'I. FOREST.'")
        estadistica.append(['Incendios Forestales', self.cursor.fetchone()[0]])
        # Llamados de comandancia
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE MONTHNAME(fecha) = '{month}' AND YEAR(fecha) = {year} AND (acto LIKE '10-%' AND acto NOT LIKE '10-9-%' AND NOT acto = '10-3-9')")
        estadistica.append(['Llamados de Comandancia', self.cursor.fetchone()[0]])
        # Estructurales
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE MONTHNAME(fecha) = '{month}' AND YEAR(fecha) = {year} AND acto LIKE '10-0-%'")
        estadistica.append(['Claves 10-0', self.cursor.fetchone()[0]])
        # Rescates
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE MONTHNAME(fecha) = '{month}' AND YEAR(fecha) = {year} AND acto LIKE '10-4-%'")
        estadistica.append(['Rescates', self.cursor.fetchone()[0]])
        # Salvamentos
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE MONTHNAME(fecha) = '{month}' AND YEAR(fecha) = {year} AND acto LIKE '10-3-%' AND NOT acto = '10-3-9'")
        estadistica.append(['Salvamentos', self.cursor.fetchone()[0]])
        # Materiales Peligrosos
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE MONTHNAME(fecha) = '{month}' AND YEAR(fecha) = {year} AND (acto LIKE '10-5-%' OR acto LIKE '10-6-%')")
        estadistica.append(['Materiales Peligrosos (10-5, 10-6)', self.cursor.fetchone()[0]])
        # Apoyos
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE MONTHNAME(fecha) = '{month}' AND YEAR(fecha) = {year} AND acto = '10-12'")
        estadistica.append(['Apoyos a Otros Cuerpos (10-12, 0-11)', self.cursor.fetchone()[0]])
        # Otros Servicios
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE MONTHNAME(fecha) = '{month}' AND YEAR(fecha) = {year} AND (acto LIKE '10-9-%' OR acto = '10-3-9')")
        estadistica.append(['Otros Servicios', self.cursor.fetchone()[0]])
        # Reuniones
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE MONTHNAME(fecha) = '{month}' AND YEAR(fecha) = {year} AND (acto = 'SS.OO.' OR acto = 'SS.EE')")
        estadistica.append(['Sesiones', self.cursor.fetchone()[0]])
        # Academias
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE MONTHNAME(fecha) = '{month}' AND YEAR(fecha) = {year} AND acto = 'ACADEMIA'")
        estadistica.append(['Academias', self.cursor.fetchone()[0]])
        # Asistencia Despachos
        self.cursor.execute(
            f"SELECT avg(c_vols) FROM actos WHERE MONTHNAME(fecha) = '{month}' AND YEAR(fecha) = {year} AND (acto LIKE '10-%' OR acto = 'INCENDIO' or acto = 'I. FOREST.')")
        estadistica.append(['Promedio Asistencia Actos de Servicio', self.cursor.fetchone()[0]])
        # Asistencia Academias
        self.cursor.execute(
            f"SELECT avg(c_vols) FROM actos WHERE MONTHNAME(fecha) = '{month}' AND YEAR(fecha) = {year} AND acto = 'ACADEMIA'")
        estadistica.append(['Promedio Asistencia Academias', self.cursor.fetchone()[0]])
        # Asistencia Sesiones
        self.cursor.execute(
            f"SELECT avg(c_vols) FROM actos WHERE MONTHNAME(fecha) = '{month}' AND YEAR(fecha) = {year} AND (acto = 'SS.OO.' OR acto = 'SS.EE')")
        estadistica.append(['Promedio Asistencia Sesiones', self.cursor.fetchone()[0]])
        # Asistencia Citaciones Cuerpo
        self.cursor.execute(
            f"SELECT avg(c_vols) FROM actos WHERE MONTHNAME(fecha) = '{month}' AND YEAR(fecha) = {year} AND (acto = 'DESFILE CB' OR acto = 'ROMERIA CB' or acto = 'SS. SOL. CB')")
        estadistica.append(['Promedio Asistencia Citaciones CBPA', self.cursor.fetchone()[0]])
        # Asistencia General
        self.cursor.execute(
            f"SELECT avg(c_vols) FROM actos WHERE MONTHNAME(fecha) = '{month}' AND YEAR(fecha) = {year} AND NOT (acto in ('C. ADM.','J. OFF', 'CONS. DISC'))")
        estadistica.append(['Promedio Asistencia General', self.cursor.fetchone()[0]])



        return lista, actos, estadistica

    def resEspecifico(self, fDesde, fHasta):
        lista = []
        self.cursor.execute('SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos where sub_estado = "ACTIVO"')
        for row in self.cursor.fetchall():
            lista.append(list(row))
        for row in lista:
            self.cursor.execute(f'SELECT count(corr_cia_acto) FROM asistencia INNER JOIN actos a on asistencia.corr_cia_acto = a.corr_cia WHERE fecha BETWEEN STR_TO_DATE("{fDesde}", "%d-%m-%Y") AND STR_TO_DATE("{fHasta}", "%d-%m-%Y") and reg_gral_voluntario = "{row[0]}" AND NOT (a.acto in ("C. ADM.","J. OFF", "CONS. DISC"))')
            lista[lista.index(row)].append(self.cursor.fetchall()[0][0])
            self.cursor.execute(f'SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN STR_TO_DATE("{fDesde}", "%d-%m-%Y") AND STR_TO_DATE("{fHasta}", "%d-%m-%Y") AND NOT (acto in ("C. ADM.","J. OFF", "CONS. DISC"))')
            lista[lista.index(row)].append(row[4] / self.cursor.fetchall()[0][0])
            self.cursor.execute(f'SELECT count(corr_cia_acto) FROM asistencia INNER JOIN actos a on asistencia.corr_cia_acto = a.corr_cia WHERE fecha BETWEEN STR_TO_DATE("{fDesde}", "%d-%m-%Y") AND STR_TO_DATE("{fHasta}", "%d-%m-%Y") and reg_gral_voluntario = "{row[0]}" AND a.lista = "OB"')
            lista[lista.index(row)].append(self.cursor.fetchall()[0][0])
            self.cursor.execute(f'SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN STR_TO_DATE("{fDesde}", "%d-%m-%Y") AND STR_TO_DATE("{fHasta}", "%d-%m-%Y") AND lista = "OB"')
            lista[lista.index(row)].append(row[6] / self.cursor.fetchall()[0][0])
        self.cursor.execute(f'SELECT * FROM actos WHERE fecha BETWEEN STR_TO_DATE("{fDesde}", "%d-%m-%Y") AND STR_TO_DATE("{fHasta}", "%d-%m-%Y") ORDER BY fecha DESC, corr_cia DESC')
        actos = self.cursor.fetchall()

        estadistica = []
        # Incendios
        self.cursor.execute(f"SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN STR_TO_DATE('{fDesde}', '%d-%m-%Y') AND STR_TO_DATE('{fHasta}', '%d-%m-%Y') AND acto = 'INCENDIO'")
        estadistica.append(['Incendios Estructurales', self.cursor.fetchone()[0]])
        # Forestales
        self.cursor.execute(f"SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN STR_TO_DATE('{fDesde}', '%d-%m-%Y') AND STR_TO_DATE('{fHasta}', '%d-%m-%Y') AND acto = 'I. FOREST.'")
        estadistica.append(['Incendios Forestales', self.cursor.fetchone()[0]])
        # Llamados de comandancia
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN STR_TO_DATE('{fDesde}', '%d-%m-%Y') AND STR_TO_DATE('{fHasta}', '%d-%m-%Y') AND acto LIKE '10-%' AND acto NOT LIKE '10-9-%' AND NOT acto = '10-3-9'")
        estadistica.append(['Llamados de Comandancia', self.cursor.fetchone()[0]])
        # Estructurales
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN STR_TO_DATE('{fDesde}', '%d-%m-%Y') AND STR_TO_DATE('{fHasta}', '%d-%m-%Y') AND acto LIKE '10-0-%'")
        estadistica.append(['Claves 10-0', self.cursor.fetchone()[0]])
        # Rescates
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN STR_TO_DATE('{fDesde}', '%d-%m-%Y') AND STR_TO_DATE('{fHasta}', '%d-%m-%Y') AND acto LIKE '10-4-%'")
        estadistica.append(['Rescates', self.cursor.fetchone()[0]])
        # Salvamentos
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN STR_TO_DATE('{fDesde}', '%d-%m-%Y') AND STR_TO_DATE('{fHasta}', '%d-%m-%Y') AND acto LIKE '10-3-%' AND NOT acto = '10-3-9'")
        estadistica.append(['Salvamentos', self.cursor.fetchone()[0]])
        # Materiales Peligrosos
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN STR_TO_DATE('{fDesde}', '%d-%m-%Y') AND STR_TO_DATE('{fHasta}', '%d-%m-%Y') AND (acto LIKE '10-5-%' OR acto LIKE '10-6-%')")
        estadistica.append(['Materiales Peligrosos (10-5, 10-6)', self.cursor.fetchone()[0]])
        # Apoyos
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN STR_TO_DATE('{fDesde}', '%d-%m-%Y') AND STR_TO_DATE('{fHasta}', '%d-%m-%Y') AND acto = '10-12'")
        estadistica.append(['Apoyos a Otros Cuerpos (10-12, 0-11)', self.cursor.fetchone()[0]])
        # Otros Servicios
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN STR_TO_DATE('{fDesde}', '%d-%m-%Y') AND STR_TO_DATE('{fHasta}', '%d-%m-%Y') AND (acto LIKE '10-9-%' OR acto = '10-3-9')")
        estadistica.append(['Otros Servicios', self.cursor.fetchone()[0]])
        # Reuniones
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN STR_TO_DATE('{fDesde}', '%d-%m-%Y') AND STR_TO_DATE('{fHasta}', '%d-%m-%Y') AND (acto = 'SS.OO.' OR acto = 'SS.EE')")
        estadistica.append(['Sesiones', self.cursor.fetchone()[0]])
        # Academias
        self.cursor.execute(
            f"SELECT count(corr_cia) FROM actos WHERE fecha BETWEEN STR_TO_DATE('{fDesde}', '%d-%m-%Y') AND STR_TO_DATE('{fHasta}', '%d-%m-%Y') AND acto = 'ACADEMIA'")
        estadistica.append(['Academias', self.cursor.fetchone()[0]])
        # Asistencia Despachos
        self.cursor.execute(
            f"SELECT avg(c_vols) FROM actos WHERE fecha BETWEEN STR_TO_DATE('{fDesde}', '%d-%m-%Y') AND STR_TO_DATE('{fHasta}', '%d-%m-%Y') AND (acto LIKE '10-%' OR acto = 'INCENDIO' or acto = 'I. FOREST.')")
        estadistica.append(['Promedio Asistencia Despachos', self.cursor.fetchone()[0]])
        # Asistencia Academias
        self.cursor.execute(
            f"SELECT avg(c_vols) FROM actos WHERE fecha BETWEEN STR_TO_DATE('{fDesde}', '%d-%m-%Y') AND STR_TO_DATE('{fHasta}', '%d-%m-%Y') AND acto = 'ACADEMIA'")
        estadistica.append(['Promedio Asistencia Academias', self.cursor.fetchone()[0]])
        # Asistencia Sesiones
        self.cursor.execute(
            f"SELECT avg(c_vols) FROM actos WHERE fecha BETWEEN STR_TO_DATE('{fDesde}', '%d-%m-%Y') AND STR_TO_DATE('{fHasta}', '%d-%m-%Y') AND (acto = 'SS.OO.' OR acto = 'SS.EE')")
        estadistica.append(['Promedio Asistencia Sesiones', self.cursor.fetchone()[0]])
        # Asistencia Citaciones Cuerpo
        self.cursor.execute(
            f"SELECT avg(c_vols) FROM actos WHERE fecha BETWEEN STR_TO_DATE('{fDesde}', '%d-%m-%Y') AND STR_TO_DATE('{fHasta}', '%d-%m-%Y') AND (acto = 'DESFILE CB' OR acto = 'ROMERIA CB' or acto = 'SS. EE. CB')")
        estadistica.append(['Promedio Asistencia Citaciones CBPA', self.cursor.fetchone()[0]])
        # Asistencia General
        self.cursor.execute(
            f"SELECT avg(c_vols) FROM actos WHERE fecha BETWEEN STR_TO_DATE('{fDesde}', '%d-%m-%Y') AND STR_TO_DATE('{fHasta}', '%d-%m-%Y') AND NOT (acto in ('C. ADM.','J. OFF', 'CONS. DISC'))")
        estadistica.append(['Promedio Asistencia General', self.cursor.fetchone()[0]])

        return lista, actos, estadistica

    def info90(self):
        lista = []
        self.cursor.execute('SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos where sub_estado = "ACTIVO"')
        for row in self.cursor.fetchall():
            lista.append(list(row))
        self.cursor.execute('SELECT reg_gral_voluntario ,count(corr_cia_acto) FROM asistencia INNER JOIN actos a on asistencia.corr_cia_acto = a.corr_cia WHERE a.fecha >= DATE_ADD(CURDATE(), INTERVAL -90 DAY) GROUP BY reg_gral_voluntario')
        for row in self.cursor.fetchall():
            for i in lista:
                if i[0] == row[0]:
                    lista.remove(i)
                    break
        self.cursor.execute(f'SELECT * FROM actos WHERE fecha >= DATE_ADD(CURDATE(), INTERVAL -90 DAY)')
        actos = self.cursor.fetchall()
        return lista, actos

    def send_messageMo(self, month, year):
        content = open(os.path.abspath('resources/message.html'), 'r').read()
        style = open(os.path.abspath('resources/messagestyle.html'), 'r').read()
        yagmail.register(self.data['eMail'], self.data['pass_eMail'])
        yag = yagmail.SMTP(self.data["eMail"])
        self.cursor.execute('SELECT reg_gral, nombre, apellidoP, apellidoM, email FROM bomberos WHERE sub_estado = "ACTIVO"')
        dbrow = self.cursor.fetchall()
        for row in dbrow:
            reg_gral, nombre, apellidoP, apellidoM, email = row
            asunto = f"Asistencia mensual voluntario/a {nombre} {apellidoP}"
            aquery = f"""SELECT corr_cia, acto, fecha, direccion from actos
            INNER JOIN asistencia a on actos.corr_cia = a.corr_cia_acto
            WHERE reg_gral_voluntario = '{reg_gral}'
            AND MONTHNAME(fecha) = '{month}'
            AND YEAR(fecha) = {year}"""
            self.cursor.execute(aquery)
            alist = self.cursor.fetchall()
            actos = ""
            for asis in alist:
                actos += "<tr>"
                actos += "<td>" + asis[0] + "</td><td>" + asis[1] + "</td><td>" + asis[2].strftime("%d-%m-%Y") + "</td><td>" + asis[3] + "</td>"
                actos += "</tr>"
            contentm = content.format(nombreD=nombre, apellido1D=apellidoP, apellido2D=apellidoM, actos=actos, nombre_oficial=self.data['Nombre'], cargo_oficial=self.data['Cargo'])
            #yag.send(self.data["eMail"], asunto, style + contentm)
            yag.send(email, asunto, style + contentm)

    def getMonth(self):
        meses = [""]
        self.cursor.execute("SELECT MONTHNAME(fecha) FROM actos GROUP BY month(fecha) ORDER BY MONTH(fecha)")
        for mo in self.cursor.fetchall():
            meses.append(mo[0])
        return meses

    def getYear(self):
        años = [""]
        self.cursor.execute("SELECT YEAR(fecha) FROM actos GROUP BY year(fecha) ORDER BY fecha")
        for ye in self.cursor.fetchall():
            años.append(str(ye[0]))
        return años

    def getActos(self, cCia):
        self.cursor.execute(f'SELECT acto, corr_gral, fecha, direccion, lista FROM actos WHERE corr_cia = "{cCia}"')
        result = self.cursor.fetchall()[0]
        return result

    def delLista(self, cCia):
        self.cursor.execute(f'DELETE FROM asistencia WHERE corr_cia_acto = "{cCia}"')
        self.cursor.execute(f'DELETE FROM actos WHERE corr_cia = "{cCia}"')
        self.conecta.commit()

    def getVols(self, rGral):
        self.cursor.execute(f'SELECT * FROM bomberos WHERE reg_gral = "{rGral}"')
        result = self.cursor.fetchall()[0]
        return result

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
        vols = []
        self.cursor.execute("SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos")
        for vol in self.cursor.fetchall():
            rGral, nombre, apellidoP, apellidoM = vol
            vols.append(f"{rGral} - {nombre} {apellidoP} {apellidoM}")
        return vols

    #Ingresar Nueva Licencia
    def nv_lic(self, *args):
        cLic, n_reg, f_desde, f_hasta, motivo, aprobado = args
        query = f'INSERT INTO licencias VALUES ("{n_reg}", STR_TO_DATE("{f_desde}" , "%d-%m-%Y"), STR_TO_DATE("{f_hasta}", "%d-%m-%Y"), "{motivo}", "{aprobado}", "{cLic}")'
        self.cursor.execute(query)
        self.conecta.commit()
        return

    #Retornar Nombre para el campo
    def get_nameVols(self, nReg):
        query = f"SELECT nombre, apellidoP, apellidoM FROM bomberos WHERE reg_gral = '{nReg}'"
        self.cursor.execute(query)
        nom, apeP, apeM = self.cursor.fetchone()
        nombre = f'{nom} {apeP} {apeM}'
        return nombre

    # Retornar Lista de Licencias
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
    # Actualizar Licencia
    def licenciaUpdate(self, *licencia):
        cLic, n_reg, f_desde, f_hasta, motivo, aprobado = licencia
        query = f'UPDATE licencias SET nro_registro = "{n_reg}", f_desde = STR_TO_DATE("{f_desde}" , "%d-%m-%Y"),f_hasta = STR_TO_DATE("{f_hasta}", "%d-%m-%Y"), motivo = "{motivo}", aprobado = "{aprobado}", corr_Lic = "{cLic}")'
        self.cursor.execute(query)
        self.conecta.commit()
        return

    # Eliminar Licencia
    def deleteLicencia(self, corr_Lic):
        sql = f'DELETE FROM licencias WHERE corr_Lic = "{corr_Lic}"'
        self.cursor.execute(sql)
        self.conecta.commit()

