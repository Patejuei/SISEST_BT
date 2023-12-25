import os

from lib.Models.connection import Conexion
from PySide6.QtWidgets import QFileDialog, QWidget
from lib.Models import Filter
import datetime
import pandas as pd


# TODO: Implementar los métodos de Conexión relacionados con la generación de informes

class Informe(Conexion):
    DateStart: datetime.date
    month: str
    year: int
    DateEnd: datetime.date

    def __init__(self, Widget, DateStart=None, DateEnd=None, month=None, year=None):
        super().__init__()
        meses = {
            "Enero": "January",
            "Febrero": "February",
            "Marzo": "March",
            "Abril": "April",
            "Mayo": "May",
            "Junio": "June",
            "Julio": "July",
            "Agosto": "August",
            "Septiembre": "September",
            "Octubre": "October",
            "Noviembre": "November",
            "Diciembre": "December"
        }
        file_filter = 'Todos los Archivos;; Archivo Excel (*.xlsx *.xls);; Archivo PDF (*.pdf)'
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop/')
        self.saveDirectory, self.saveFilter = QFileDialog.getSaveFileName(
            parent=Widget,
            caption='Guardar el Reporte',
            dir=desktop,
            filter=file_filter,
            selectedFilter='Archivo Excel (*.xlsx *.xls)'
        )
        self._HeaderVols = ["Reg. Gral", "Nombre", "Apellido Paterno", "Apellido Materno", "Listas Totales",
                            "Porcentaje General", "Listas Obligatorias", "Porcentaje Obligatorias"]
        self._HeaderActos = ["Correlativo Compañía", "Acto", "Correlativo General", "Fecha", "Dirección", "Lista",
                             "Cantidad de Voluntarios", "Carro"]
        self._Header90days = ["Reg. Gral", "Nombre", "Apellido Paterno", "Apellido Materno"]
        self.excelWriter = pd.ExcelWriter(self.saveDirectory)

        if DateStart is not None:
            self.DateStart = Filter.Filter_Date(DateStart)
        if DateEnd is not None:
            self.DateEnd = Filter.Filter_Date(DateEnd)
        if month is not None:
            self.month = meses[month]
        if year is not None:
            self.year = int(year)

    def resMensual(self):
        _DateDefiner = (self.month, self.year)
        # Get the active firefighters' data from the database
        self.cursor.execute('SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos WHERE sub_estado = "ACTIVO"')
        firefighters_data = self.cursor.fetchall()

        # Prepare the initial data structure as a list of lists
        lista = [list(row) + [0, 0, 0, 0] for row in firefighters_data]

        query_conditions = [self.month, self.year]
        qty_conditions = len([row[0] for row in firefighters_data])
        query_conditions += [row[0] for row in firefighters_data]

        # Combine all queries into a single query for better performance
        self.cursor.execute('''
            SELECT 
                reg_gral_voluntario,
                COUNT(DISTINCT corr_cia_acto),
                COUNT(DISTINCT CASE WHEN a.lista = 'OB' THEN corr_cia_acto END)
            FROM asistencia
            INNER JOIN actos a ON asistencia.corr_cia_acto = a.corr_cia
            WHERE 
                MONTHNAME(fecha) = %s AND YEAR(fecha) = %s
                AND (a.lista != 'C. ADM.' AND a.lista != 'J. OFF' AND a.lista != 'CONS. DISC')
                AND reg_gral_voluntario IN ({})
            GROUP BY reg_gral_voluntario
        '''.format(','.join(['%s'] * qty_conditions)), query_conditions)

        # Fetch all results at once
        results = self.cursor.fetchall()

        # Cantidad de actos
        self.cursor.execute('''
            SELECT 
                count(corr_cia),
                count(CASE WHEN lista = 'OB' THEN corr_cia END)
            FROM actos
            WHERE
                MONTHNAME(fecha) = %s AND YEAR(fecha) = %s
        ''', _DateDefiner)

        total_lists, total_ob_lists = self.cursor.fetchone()
        # Update the lista with the calculated values
        for row in results:
            firefighter_id = row[0]
            index = next((idx for idx, item in enumerate(lista) if item[0] == firefighter_id), None)
            if index is not None:
                lista[index][4] = row[1]  # Count of total lists attended
                lista[index][5] = row[1] / total_lists if total_lists > 0 else 0  # Attendance percentage
                lista[index][6] = row[2]  # Count of obligatory lists attended
                lista[index][7] = row[2] / total_ob_lists if total_ob_lists > 0 else 0  # Obligatory lists percentage

        self.cursor.execute(
            'SELECT * FROM actos WHERE MONTHNAME(fecha) = %s AND YEAR(fecha) = %s ORDER BY fecha ASC, corr_cia ASC',
            _DateDefiner
            )
        actos = self.cursor.fetchall()

        # Define the queries and their labels in a dictionary
        _Query = f'''
            SELECT
                MONTH(fecha),
                count(CASE WHEN acto = 'INCENDIO' THEN corr_cia END),
                count(CASE WHEN acto = 'I. FOREST.' THEN corr_cia END),
                count(CASE WHEN acto LIKE '10-%' AND acto NOT LIKE '10-9-%' AND NOT acto = '10-3-9' THEN corr_cia END),
                count(CASE WHEN acto LIKE '10-0-%' THEN corr_cia END),
                count(CASE WHEN acto LIKE '10-4-%' THEN corr_cia END),
                count(CASE WHEN acto LIKE '10-3-%' AND NOT acto = '10-3-9' THEN corr_cia END),
                count(CASE WHEN acto LIKE '10-5-%' OR acto LIKE '10-6-%' THEN corr_cia END),
                count(CASE WHEN acto = '10-12' OR acto = '0-11' THEN corr_cia END),
                count(CASE WHEN acto LIKE '10-9-%' OR acto = '10-3-9' THEN corr_cia END),
                count(CASE WHEN acto = 'SS.OO.' OR acto = 'SS.EE' THEN corr_cia END),
                count(CASE WHEN acto = 'ACADEMIA' THEN corr_cia END),
                count(CASE WHEN acto LIKE '10-%' OR acto IN ('INCENDIO' , 'I. FOREST.') THEN corr_cia END),
                count(corr_cia),
                avg(CASE WHEN acto LIKE '10-%' OR acto IN ('INCENDIO' , 'I. FOREST.') THEN c_vols END),
                avg(CASE WHEN acto = 'SS.OO.' OR acto = 'SS.EE' THEN c_vols END),
                avg(CASE WHEN acto = 'ACADEMIA' THEN c_vols END),
                avg(CASE WHEN acto IN ('DESFILE CB', 'ROMERIA CB', 'SS. EE. CB') THEN c_vols END),
                avg(c_vols),
                count(CASE WHEN unidad LIKE '%B9%' THEN corr_cia END),
                count(CASE WHEN unidad LIKE '%M9%' THEN corr_cia END),
                count(CASE WHEN unidad LIKE '%UT9%' THEN corr_cia END)
            FROM actos
            WHERE
                YEAR(fecha) = {self.year}
            GROUP BY MONTH(fecha)
            ORDER BY MONTH(fecha)
        '''
        self.cursor.execute(_Query)
        _Statistics = {'Mes': [],
                       'Incendios Estructurales': [],
                       'Incendios Forestales': [],
                       'Llamados de Comandancia':[],
                       'Claves 10-0':[],
                       'Rescates':[],
                       'Salvamentos':[],
                       'Materiales Peligrosos (10-5, 10-6)':[],
                       'Apoyos a otros cuerpos (10-12, 0-11)':[],
                       'Otros Servicios':[],
                       'Sesiones': [],
                       'Academias': [],
                       'Total Servicios': [],
                       'Total Listas': [],
                       'Promedio Asistencia Despachos': [],
                       'Promedio Asistencia Sesiones': [],
                       'Promedio Asistencia Academias': [],
                       'Promedio Asistencia Citaciones CBPA': [],
                       'Promedio Asistencia General': [],
                       'Salidas B9' : [],
                       'Salidas M9' : [],
                       'Salidas UT9' : []}
        for row in self.cursor.fetchall():
            _Statistics['Mes'].append(row[0])
            _Statistics['Incendios Estructurales'].append(row[1])
            _Statistics['Incendios Forestales'].append(row[2])
            _Statistics['Llamados de Comandancia'].append(row[3])
            _Statistics['Claves 10-0'].append(row[4])
            _Statistics['Rescates'].append(row[5])
            _Statistics['Salvamentos'].append(row[6])
            _Statistics['Materiales Peligrosos (10-5, 10-6)'].append(row[7])
            _Statistics['Apoyos a otros cuerpos (10-12, 0-11)'].append(row[8])
            _Statistics['Otros Servicios'].append(row[9])
            _Statistics['Sesiones'].append(row[10])
            _Statistics['Academias'].append(row[11])
            _Statistics['Total Servicios'].append(row[12])
            _Statistics['Total Listas'].append(row[13])
            _Statistics['Promedio Asistencia Despachos'].append(row[14])
            _Statistics['Promedio Asistencia Sesiones'].append(row[15])
            _Statistics['Promedio Asistencia Academias'].append(row[16])
            _Statistics['Promedio Asistencia Citaciones CBPA'].append(row[17])
            _Statistics['Promedio Asistencia General'].append(row[18])
            _Statistics['Salidas B9'].append(row[19])
            _Statistics['Salidas M9'].append(row[20])
            _Statistics['Salidas UT9'].append(row[21])

        self.connection.close()

        dfActs = pd.DataFrame(actos)
        dfAsist = pd.DataFrame(lista)
        dfStatistics = pd.DataFrame(_Statistics)

        dfActs.to_excel(self.excelWriter, sheet_name="Actos del Mes", header=self._HeaderActos, index=False)
        dfAsist.to_excel(self.excelWriter, sheet_name="Asistencia Voluntarios", header=self._HeaderVols, index=False)
        dfStatistics.to_excel(self.excelWriter, sheet_name="Estadísticas", index=False)
        self.excelWriter.close()

        os.startfile(self.saveDirectory)

    def resEspecifico(self):
        _DateDifference = (self.DateStart, self.DateEnd)
        # Get the active firefighters' data from the database
        self.cursor.execute('SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos WHERE sub_estado = "ACTIVO"')
        firefighters_data = self.cursor.fetchall()

        # Prepare the initial data structure as a list of lists
        lista = [list(row) + [0, 0, 0, 0] for row in firefighters_data]

        # Create a dictionary to store the query conditions for each firefighter
        query_conditions = [self.DateStart, self.DateEnd]
        qty_conditions = len([row[0] for row in firefighters_data])
        query_conditions += [row[0] for row in firefighters_data]

        # Combine all queries into a single query for better performance
        self.cursor.execute('''
            SELECT 
                reg_gral_voluntario,
                COUNT(DISTINCT corr_cia_acto),
                COUNT(DISTINCT CASE WHEN a.lista = 'OB' THEN corr_cia_acto END)
            FROM asistencia
            INNER JOIN actos a ON asistencia.corr_cia_acto = a.corr_cia
            WHERE 
                a.fecha BETWEEN %s AND %s
                AND (a.lista != 'C. ADM.' AND a.lista != 'J. OFF' AND a.lista != 'CONS. DISC')
                AND reg_gral_voluntario IN ({})
            GROUP BY reg_gral_voluntario
        '''.format(','.join(['%s'] * qty_conditions)), query_conditions)

        # Fetch all results at once
        results = self.cursor.fetchall()

        self.cursor.execute(
            '''
            SELECT
                COUNT(corr_cia),
                COUNT(CASE WHEN lista = 'OB' THEN corr_cia END)
            FROM actos
            WHERE
                fecha BETWEEN %s AND %s

            ''', _DateDifference
        )

        total_lists, total_ob_lists = self.cursor.fetchone()

        # Update the lista with the calculated values
        for row in results:
            firefighter_id = row[0]
            index = next((idx for idx, item in enumerate(lista) if item[0] == firefighter_id), None)
            if index is not None:
                lista[index][4] = row[1]  # Count of total lists attended
                lista[index][5] = row[1] / total_lists if total_lists > 0 else 0  # Attendance percentage
                lista[index][6] = row[2]  # Count of obligatory lists attended
                lista[index][7] = row[2] / total_ob_lists if total_ob_lists > 0 else 0  # Obligatory lists percentage

        self.cursor.execute('SELECT * FROM actos WHERE fecha BETWEEN %s AND %s ORDER BY fecha DESC, corr_cia DESC',
                            _DateDifference
                            )
        actos = self.cursor.fetchall()

        _Query = '''
            SELECT
                MONTH(fecha),
                count(CASE WHEN acto = 'INCENDIO' THEN corr_cia END),
                count(CASE WHEN acto = 'I. FOREST.' THEN corr_cia END),
                count(CASE WHEN acto LIKE '10-%' AND acto NOT LIKE '10-9-%' AND NOT acto = '10-3-9' THEN corr_cia END),
                count(CASE WHEN acto LIKE '10-0-%' THEN corr_cia END),
                count(CASE WHEN acto LIKE '10-4-%' THEN corr_cia END),
                count(CASE WHEN acto LIKE '10-3-%' AND NOT acto = '10-3-9' THEN corr_cia END),
                count(CASE WHEN acto LIKE '10-5-%' OR acto LIKE '10-6-%' THEN corr_cia END),
                count(CASE WHEN acto = '10-12' THEN corr_cia END),
                count(CASE WHEN acto LIKE '10-9-%' OR acto = '10-3-9' THEN corr_cia END),
                count(CASE WHEN acto = 'SS.OO.' OR acto = 'SS.EE' THEN corr_cia END),
                count(CASE WHEN acto = 'ACADEMIA' THEN corr_cia END),
                count(CASE WHEN acto LIKE '10-%' OR acto IN ('INCENDIO' , 'I. FOREST.') THEN corr_cia END),
                count(corr_cia),
                avg(CASE WHEN acto LIKE '10-%' OR acto IN ('INCENDIO' , 'I. FOREST.') THEN c_vols END),
                avg(CASE WHEN acto = 'SS.OO.' OR acto = 'SS.EE' THEN c_vols END),
                avg(CASE WHEN acto = 'ACADEMIA' THEN c_vols END),
                avg(CASE WHEN acto IN ('DESFILE CB', 'ROMERIA CB', 'SS. EE. CB') THEN c_vols END),
                avg(c_vols),
                count(CASE WHEN unidad LIKE '%B9%' THEN corr_cia END),
                count(CASE WHEN unidad LIKE '%M9%' THEN corr_cia END),
                count(CASE WHEN unidad LIKE '%UT9%' THEN corr_cia END)
            FROM actos
            WHERE
                fecha BETWEEN %s AND %s
            GROUP BY MONTH(fecha)
            ORDER BY MONTH(fecha)
        '''
        self.cursor.execute(_Query, _DateDifference)
        _Statistics = {'Mes': [],
                       'Incendios Estructurales': [],
                       'Incendios Forestales': [],
                       'Llamados de Comandancia':[],
                       'Claves 10-0':[],
                       'Rescates':[],
                       'Salvamentos':[],
                       'Materiales Peligrosos (10-5, 10-6)':[],
                       'Apoyos a otros cuerpos (10-12, 0-11)':[],
                       'Otros Servicios':[],
                       'Sesiones': [],
                       'Academias': [],
                       'Total Servicios': [],
                       'Total Listas': [],
                       'Promedio Asistencia Despachos': [],
                       'Promedio Asistencia Sesiones': [],
                       'Promedio Asistencia Academias': [],
                       'Promedio Asistencia Citaciones CBPA': [],
                       'Promedio Asistencia General': [],
                       'Salidas B9' : [],
                       'Salidas M9' : [],
                       'Salidas UT9' : []}
        for row in self.cursor.fetchall():
            _Statistics['Mes'].append(row[0])
            _Statistics['Incendios Estructurales'].append(row[1])
            _Statistics['Incendios Forestales'].append(row[2])
            _Statistics['Llamados de Comandancia'].append(row[3])
            _Statistics['Claves 10-0'].append(row[4])
            _Statistics['Rescates'].append(row[5])
            _Statistics['Salvamentos'].append(row[6])
            _Statistics['Materiales Peligrosos (10-5, 10-6)'].append(row[7])
            _Statistics['Apoyos a otros cuerpos (10-12, 0-11)'].append(row[8])
            _Statistics['Otros Servicios'].append(row[9])
            _Statistics['Sesiones'].append(row[10])
            _Statistics['Academias'].append(row[11])
            _Statistics['Total Servicios'].append(row[12])
            _Statistics['Total Listas'].append(row[13])
            _Statistics['Promedio Asistencia Despachos'].append(row[14])
            _Statistics['Promedio Asistencia Sesiones'].append(row[15])
            _Statistics['Promedio Asistencia Academias'].append(row[16])
            _Statistics['Promedio Asistencia Citaciones CBPA'].append(row[17])
            _Statistics['Promedio Asistencia General'].append(row[18])
            _Statistics['Salidas B9'].append(row[19])
            _Statistics['Salidas M9'].append(row[20])
            _Statistics['Salidas UT9'].append(row[21])


        self.connection.close()
        # Execute the queries and update the _Statistics dictionary

        dfActs = pd.DataFrame(actos)
        dfAsist = pd.DataFrame(lista)
        dfStatistics = pd.DataFrame(_Statistics)

        dfActs.to_excel(self.excelWriter, sheet_name="Actos del Periodo", header=self._HeaderActos, index=False)
        dfAsist.to_excel(self.excelWriter, sheet_name="Asistencia Voluntarios", header=self._HeaderVols, index=False)
        dfStatistics.to_excel(self.excelWriter, sheet_name="Estadísticas", index=False)
        self.excelWriter.close()

        os.startfile(self.saveDirectory)

    def info90(self):
        lista = []
        self.cursor.execute('SELECT reg_gral, nombre, apellidoP, apellidoM FROM bomberos where sub_estado = "ACTIVO"')
        for row in self.cursor.fetchall():
            lista.append(list(row))
        self.cursor.execute(
            'SELECT reg_gral_voluntario FROM asistencia INNER JOIN actos a on asistencia.corr_cia_acto = a.corr_cia WHERE a.fecha >= DATE_ADD(CURDATE(), INTERVAL -90 DAY) GROUP BY reg_gral_voluntario')
        for row in self.cursor.fetchall():
            for i in lista:
                if i[0] == row[0]:
                    lista.remove(i)
                    break
        self.cursor.execute(f'SELECT * FROM actos WHERE fecha >= DATE_ADD(CURDATE(), INTERVAL -90 DAY)')
        actos = self.cursor.fetchall()
        self.connection.close()

        dfLista = pd.DataFrame(lista)
        dfActos = pd.DataFrame(actos)
        dfLista.to_excel(self.excelWriter, sheet_name='Voluntarios sin Asistencia', header=self._Header90days, index=False)
        dfActos.to_excel(self.excelWriter, sheet_name='Actos en los 90 Dias', header=self._HeaderActos, index=False)
        self.excelWriter.close()
        os.startfile(self.saveDirectory)

    def informe_personal(self, reg_gral):
        asistencia_dict = {
            'Año': 'SELECT YEAR(fecha) from actos GROUP BY YEAR(fecha)',
            'Listas Totales': 'SELECT count(corr_cia) FROM actos JOIN asistencia a on actos.corr_cia = a.corr_cia_acto WHERE a.reg_gral_voluntario = %s GROUP BY YEAR(fecha)',
            'Asistencia Total' : 'SELECT (count(CASE WHEN a.reg_gral_voluntario = %s THEN corr_cia END) / count(corr_cia)) FROM actos JOIN asistencia a on actos.corr_cia = a.corr_cia_acto GROUP BY YEAR(fecha)',
            'Listas Obligatorias' : "SELECT count(corr_cia) FROM actos JOIN asistencia a on actos.corr_cia = a.corr_cia_acto WHERE a.reg_gral_voluntario = %s AND lista = 'OB' GROUP BY YEAR(fecha)",
            'Asistencia Obligatorias' : "SELECT (count(CASE WHEN a.reg_gral_voluntario = %s AND acto='OB' THEN corr_cia END) / count(corr_cia)) FROM actos JOIN asistencia a on actos.corr_cia = a.corr_cia_acto WHERE lista = 'OB' GROUP BY YEAR(fecha)"
        }
        for key, query in asistencia_dict.items():
            self.cursor.execute(query, self.filter_volunteer(reg_gral))
            asistencia_dict[key] = self.cursor.fetchall()
        actos_query = "SELECT corr_cia, acto, corr_gral, fecha, direccion, lista FROM actos INNER JOIN asistencia a on actos.corr_cia = a.corr_cia_acto WHERE a.reg_gral_voluntario = %s ORDER BY fecha DESC, corr_cia DESC"
        self.cursor.execute(actos_query, self.filter_volunteer(reg_gral))
        actos_array = self.cursor.fetchall()
        self.connection.close()

        asist_dataframe = pd.DataFrame(asistencia_dict)
        actos_dataframe = pd.DataFrame(actos_array)
        asist_dataframe.to_excel(self.excelWriter, sheet_name='Asistencia', index=False)
        actos_dataframe.to_excel(self.excelWriter, sheet_name='Actos Asistidos', header=self._HeaderActos, index=False)
        self.excelWriter.close()
        os.startfile(self.saveDirectory)



    @staticmethod
    def filter_volunteer(n_reg):
        if '-' not in n_reg:
            return None
        else:
            return n_reg.split('-')[0]





