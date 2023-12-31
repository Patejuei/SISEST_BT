from lib.Models.connection import Conexion
import datetime as dt

class Licencia:
    correlativoLicencia : str
    registroVoluntario : str
    fechaDesde : dt.date
    fechaHasta : dt.date
    motivo : str
    estadoLicencia = str
    def __init__(self, cLic, regVol, fDesde, fHasta, motivo, estadoLicencia):
        self.correlativoLicencia = cLic
        self.registroVoluntario = regVol
        self.fechaDesde = self.Filter_Date(fDesde)
        self.fechaHasta = self.Filter_Date(fHasta)
        self.motivo = motivo
        self.estadoLicencia = estadoLicencia
        self.values = (
            self.registroVoluntario,
            self.fechaDesde,
            self.fechaHasta,
            self.motivo,
            self.estadoLicencia,
            self.correlativoLicencia
        )

    @staticmethod
    def Filter_Date(date):
        fecha, hora = date.split(' ')
        day, month, year = fecha.split("-")
        hh, mm = hora.split(":")
        date = dt.datetime(
            year=int(year),
            month=int(month),
            day=int(day),
            hour=int(hh),
            minute=int(mm),
        )
        return date

    #Ingresar Nueva Licencia
    def nv_lic(self):
        database = Conexion()
        cmd = '''
            INSERT INTO licencias
            VALUES
                (%s, %s, %s, %s, %s, %s)
            '''

        database.cursor.execute(cmd, self.values)
        database.connection.commit()
        database.connection.close()

    # Actualizar Licencia
    def licenciaUpdate(self):
        database = Conexion()
        query = '''
            UPDATE
                licencias
            SET 
                nro_registro = %s,
                f_desde = %s,
                f_hasta = %s,
                motivo = %s,
                aprobado = %s
            WHERE
                corr_Lic = %s
        '''
        database.cursor.execute(query, self.values)
        database.connection.commit()
        database.connection.close()

