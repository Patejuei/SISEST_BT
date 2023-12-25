from lib.Models.connection import Conexion
from lib.Models import Filter
import datetime

class Voluntario:
    rGeneral : str
    rCia : int
    nombre : str
    apellidoP: str
    apellidoM : str
    eMail : str
    fIngreso : datetime.date
    Sub_Estado : str
    rut : int
    dv : str
    def __init__(self, rGeneral, rCia, nombre, apellidoP, apellidoM, eMail, Sub_Estado):
        self.rGeneral = rGeneral
        self.rCia = rCia
        self.nombre = nombre
        self.apellidoP = apellidoP
        self.apellidoM = apellidoM
        self.eMail = eMail
        self.Sub_Estado = Sub_Estado

    def set_fullRut(self, rut):
        self.rut, self.dv = self.FilterRut(rut)

    def set_divRut(self, rut, dv):
        self.rut = rut
        self.dv = dv
    @staticmethod
    def FilterRut(rut):
        if '-' in rut:
            rut = rut.split('-')
            dv = rut[1]
            rut = int(rut[0])
            return rut, dv
        else:
            return 0, '0'

    def addVols(self):
        database = Conexion()
        _values = (self.rGeneral, self.nombre, self.apellidoP, self.apellidoM, self.eMail, self.rut, self.dv, self.rCia, self.fIngreso, self.Sub_Estado)
        database.cursor.execute('INSERT INTO bomberos VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', _values)
        database.connection.commit()
        database.connection.close()

    def editVol(self):
        database = Conexion()
        _values = (self.rGeneral, self.nombre, self.apellidoP, self.apellidoM, self.eMail, self.rut, self.dv, self.rCia, self.fIngreso, self.Sub_Estado, self.rGeneral)
        _query = '''
        UPDATE bomberos 
        SET 
            reg_gral = %s,
            nombre = %s, 
            apellidoP = %s, 
            apellidoM = %s, 
            email = %s, 
            rut = %s, 
            dv = %s, 
            reg_cia = %s, 
            f_ingreso = %s, 
            sub_estado = %s 
        WHERE 
            reg_gral = %s'''
        database.cursor.execute(_query, _values)
        database.connection.commit()
        database.connection.close()

    #TODO: Implementar el calculo e ingreso de las suspenciones