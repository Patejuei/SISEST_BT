import datetime
from lib.Models.connection import Conexion
import lib.Models.Filter as Filter
class Acto:
    company_cor : str
    act_type: str
    general_cor : int
    date : datetime.date
    address : str
    lista : str
    qty_vols : int
    vols : list = []
    carros : str

    def __init__(self, ccia, acto, cgral, date, address, lista, carros):
        self.company_cor = ccia
        self.act_type = acto
        self.general_cor = Filter.Filter_Int(cgral)
        self.date = Filter.Filter_Date(date)
        self.address = Filter.Filter_Address(address)
        self.lista = lista
        self.carros = Filter.list_to_string(carros)

    def set_qty_vols(self):
        self.qty_vols = len(self.vols)

    def set_vols(self, vols):
        self.vols = vols
    
    def get_Vols(self):
        lista = []
        for vol in self.vols:
            lista.append((self.company_cor, vol))
        return tuple(lista)

    def addLista(self):
        database = Conexion()
        query = "INSERT INTO actos VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        database.cursor.execute(query, (self.company_cor, self.act_type, self.general_cor, self.date, self.address, self.lista, self.qty_vols, self.carros))
        for item in self.get_Vols():
            database.cursor.execute("INSERT INTO asistencia (corr_cia_acto, reg_gral_voluntario) VALUES (%s, %s)", item)
        database.connection.commit()
        database.connection.close()

    def editLista(self):
        database = Conexion()
        act_data = (self.act_type, self.general_cor, self.date, self.address, self.lista, self.qty_vols, self.carros, self.company_cor)
        database.cursor.execute(
            'UPDATE actos SET acto=%s, corr_gral=%s, fecha=%s , direccion=%s, lista=%s, c_vols=%s, unidad=%s WHERE corr_cia = %s', act_data)
        database.cursor.execute(f'DELETE FROM asistencia WHERE corr_cia_acto = "{act_data[-1]}"')
        database.cursor.executemany('INSERT INTO asistencia VALUES (%s, %s)', self.get_Vols())
        database.connection.commit()
        database.connection.close()
