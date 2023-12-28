from lib.ui_interface import Ui_MainWindow
from lib.Models.connection import Conexion
from lib.Models.Acto import Acto
from lib.Models.Voluntario import Voluntario
from lib.Models.Informe import Informe
from lib.Models.Licencias import Licencia
from lib.Models import Filter
from PySide6 import QtWidgets, QtCore
import sys
import os.path
import pdfkit
import pandas as pd
import datetime as dt


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    information = {
        "version": "0.2.0.0",
        "autor": "Andrés Bahamondes Carvajal"
    }
    efectiva_estate_in = {2: "OB", 0: "AB"}
    lista = set()
    _second_class_acts = {
        'Compañía': ['SS.EE', 'SS.OO.', 'ACADEMIA', 'J. OFF.', 'C. ADM.', 'CONS. DISC.', 'ROMERÍA', 'COMP. INT.',
                     'G. PREVENT', 'O. CITAC.'],
        'CB': ['DESFILE CB', 'DESFILE', 'ROMERÍA CB', 'SS. EE. CB', 'FUNERAL', 'INCENDIO', 'I. FOREST.',
               'O. CITAC. CB'],
        '10-0': ['10-0-1', '10-0-2', '10-0-3', '10-0-4', '10-0-5', '10-0-6', '10-0-7'],
        '10-1': ['10-1-1', '10-1-2', '10-1-3'],
        '10-2': ['10-2-1', '10-2-2', '10-2-3'],
        '10-3': ['10-3-1', '10-3-2', '10-3-3', '10-3-4', '10-3-5', '10-3-6', '10-3-7', '10-3-8', '10-3-9',
                 '10-3-10'],
        '10-4': ['10-4-1', '10-4-2', '10-4-3', '10-4-4', '10-4-5'],
        '10-5': ['10-5-1', '10-5-2', '10-5-3'],
        '10-6': ['10-6-1', '10-6-2', '10-6-3', '10-6-4', '10-6-5'],
        '10-7': ['10-7-1'],
        '10-8': ['10-8-1', '10-8-2', '10-8-3', '10-8-4'],
        '10-9': ['10-9-1', '10-9-2', '10-9-3', '10-9-4', '10-9-5', '10-9-6', '10-9-7', '10-9-8'],
        '10-10': ['10-10-1', '10-10-2'],
        '10-11': ['10-11'],
        '10-12': ['10-12', '0-11'],
        '10-13': ['10-13'],
        '10-14': ['10-14'],
        '10-15': ['10-15'],
        '10-16': ['10-16'],
        '10-17': ['10-17-1', '10-17-2', '10-17-3']
    } # Conjunto de subclasificación de los actos
    efectiva_edit_estates = {
        2: "OB",
        0: "AB"
    }   # Diccionario de estados para CheckBox de UI de edición para escritura
    cb_efectiva_edit_estates = {
        "OB": QtCore.Qt.CheckState.Checked,
        "AB": QtCore.Qt.CheckState.Unchecked
    } # Diccionario de estados para ChackBox de Ui de Edición para lectura
    license_aproved = 'Pendiente' # Estado inicial de las Licencias
    license_states = {
        2: 'Aprobado',
        0: 'Pendiente',
        1: 'Rechazado'
    } # Diccionario de estados para CheckBox de UI de Gestión de licencias para escritura
    cb_license_states = {'Aprobado': QtCore.Qt.CheckState.Checked,
                         'Pendiente': QtCore.Qt.CheckState.Unchecked,
                         'Rechazado': QtCore.Qt.CheckState.PartiallyChecked
                         } # Diccionario de estados para CHeckBox de UI de Gestión de licencias para lectura

    actos : dict = {}
    vols: dict = {}
    firefighters = []
    selectedFirefighter : Voluntario
    years : list = ["2022", "2023", "2024"]
    months : dict = {
        "Enero" : 1,
        "Febrero" : 2,
        "Marzo" : 3,
        "Abril" : 4,
        "Mayo" : 5,
        "Junio" : 6,
        "Julio" : 7,
        "Agosto" : 8,
        "Septiembre" : 9,
        "Octubre" : 10,
        "Noviembre" : 11,
        "Diciembre" : 12
    }

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.unidades_asistentes = []
        self.ingreso_carros = {
            'B9' : self.cbInsertB9,
            'M9' : self.cbInsertM9,
            'UT9' : self.cbInsertUT9,
        }
        self.edicion_carros = {
            'B9' : self.cbEditB9,
            'M9' : self.cbEditM9,
            'UT9' : self.cbEditUT9
        }
        # Probar conexión a base de datos
        try:
            self.database = Conexion()
            self.fillActos()
            self.fillVols()

        except Exception as e:
            QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error conectandose a la base de datos.\n Código de error: {e}"
            )
        # Mostrar interfaz de ingreso
        self.btnInsertList.clicked.connect(self.setInsertListUI)
        # Mostrar interfaz de edicion
        self.btnViewList.clicked.connect(self.setViewListUI)
        # Mostrar interfaz de informes
        self.btnGenInforms.clicked.connect(self.setGenResumeUI)
        # Mostrar interfaz de voluntarios
        self.btnAdminVols.clicked.connect(self.setFirefighterDataUI)
        # Mostrar interfaz de Licencias
        self.btnLicencias.clicked.connect(self.setLicenceUI)
        # Mostrar info
        self.btnInfo.clicked.connect(self.show_app_info)
        # Mostrar ayuda
        self.btnHelp.clicked.connect(self.show_help_manual)

        self.setInsertListUI() # Iniciar la aplicación con la UI de ingreso de Listas

        # Interfaz de Ingreso
        # Configuración de inicio
        self.cb_actC1.currentTextChanged.connect(lambda: self.setSubClassList(self.cb_actC1, self.cb_actC2))
        header = self.liVols.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.lblTotalLista.setText(str(len(self.lista))) # Actualización de la cantidad de voluntarios
        # Añadir voluntarios a la lista de asistencia
        self.btnAddVol.clicked.connect(lambda: self.add_vol_to_list(self.inpVol.text()))
        self.inpVol.returnPressed.connect(lambda: self.add_vol_to_list(self.inpVol.text()))
        # Conexión de botones
        self.btnDelVol.clicked.connect(self.del_vol_to_list)
        self.btnSave.clicked.connect(self.save_list)

        # Interfaz de Edicion
        # Configuración inicial
        headerSrcList = self.liListsView.horizontalHeader()
        headerSrcList.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        headerSrcList.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        headerSrcList.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        headerSrcList.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.Stretch)
        headerEditList = self.liVolsEdit.horizontalHeader()
        headerEditList.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        headerEditList.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.cb_srcMonth.addItems(self.months.keys())
        self.cb_srcYear.addItems(self.years)

        # Conexión de campo de búsqueda
        self.cb_srcMonth.currentTextChanged.connect(self.buscar_listas)
        self.cb_srcYear.currentTextChanged.connect(self.buscar_listas)
        # Conexión de selección de la tabla
        self.liListsView.selectionModel().selectionChanged.connect(self.getActo)
        # Configuración para edición de los actos
        self.cb_catAct.currentTextChanged.connect(lambda: self.setSubClassList(self.cb_catAct, self.cb_espAct)) # Editar clasificación del acto
        self.inpAddVolEdit.returnPressed.connect(lambda: self.add_vol_to_list(self.inpAddVolEdit.text())) # Añadir voluntarios a la tabla de asistentes con la tecla Enter
        # Conexión de botones
        self.btnAddVol_2.clicked.connect(lambda: self.add_vol_to_list(self.inpAddVolEdit.text()))
        self.btnDelVol_2.clicked.connect(self.del_vol_to_list)
        self.btnDeleteEdit.clicked.connect(self.delete_list)
        self.btnSaveEdit.clicked.connect(self.edit_list)

        # Interfaz de Informes
        # Configuración inicial
        completer = QtWidgets.QCompleter(self.database.getVolsInfoPers())
        self.fldInfoPersonal.setCompleter(completer)
        # Conexión de botones
        self.btnResMen.clicked.connect(self.resumenMensual)
        self.btnGenResEsp.clicked.connect(self.resumenEspecifico)
        self.btnInfo90Dias.clicked.connect(self.informe90dias)
        # self.btnGenArr.clicked.connect(self.arrastre)
        self.btnGetInfoP.clicked.connect(self.informePersonal)

        # Interfaz de Administracion
        # Configuración inicial
        self.tblAdminVols.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tblAdminVols.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        # Conexión de campo de búsqueda
        self.fldSrcAdminVols.textChanged.connect(self.buscar_bomberos)
        # Conexión de selección de la tabla
        self.tblAdminVols.selectionModel().selectionChanged.connect(self.getBombero)
        # Conexión de botones
        self.btnEditVol.clicked.connect(self.editar_vol)
        self.btnAddVol_3.clicked.connect(self.insert_vol)

        # Interfaz Licencias
        # Configuración inicial
        self.cbVBCapitan.setTristate(True)
        self.tblLicencias.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tblLicencias.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tblLicencias.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tblLicencias.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        # Conexión de campo de búsqueda
        self.inpSrcLic.textChanged.connect(self.buscarLicencias)
        # Conexión de selección en la tabla
        self.tblLicencias.selectionModel().selectionChanged.connect(self.getLicencia)
        self.inpRegLic.textChanged.connect(self.buscarNombre)
        # Conexión de botones
        self.btnSaveLic.clicked.connect(self.saveLicencia)
        self.btnUpdateLic.clicked.connect(self.updateLicencia)
        self.btnClLic.clicked.connect(self.limpiarLicencia)

    def fillVols(self):
        for vols in self.database.getVols():
            self.vols[vols[0]] = Voluntario(
                rGeneral=vols[0],
                nombre=vols[1],
                apellidoP=vols[2],
                apellidoM=vols[3],
                eMail=vols[4],
                rCia=vols[7],
                Sub_Estado=vols[9]
            )
            self.vols[vols[0]].set_divRut(vols[5], vols[6])
            self.vols[vols[0]].fIngreso = vols[8]
    def fillActos(self):
        dbData = self.database.getActos()
        for data in dbData:
            self.actos[data[0]] = Acto(data[0], data[1], data[2], data[3], data[4], data[5], data[6])

    def get_carros(self):
        self.unidades_asistentes.clear()
        if self.contentField.currentIndex() == 0:
            for key, value in self.ingreso_carros.items():
                if value.isChecked():
                    self.unidades_asistentes.append(key)
        elif self.contentField.currentIndex() == 1:
            for key, value in self.edicion_carros.items():
                if value.isChecked():
                    self.unidades_asistentes.append(key)

    def set_carros(self, carros):
        if type(carros) is not None:
            carros = carros.split(',')
            for key, value in self.edicion_carros.items():
                if key not in carros:
                    value.setCheckState(QtCore.Qt.CheckState.Unchecked)
                else:
                    value.setCheckState(QtCore.Qt.CheckState.Checked)


    def filter_Act(self, act):
        for key, values in self._second_class_acts.items():
            if act in values:
                return key

    def setSubClassList(self, clave, subclave):
        subclave.clear()
        subclave.addItems(self._second_class_acts[clave.currentText()])

    def setInsertListUI(self):
        self.database.connection.close()
        self.contentField.setCurrentIndex(0)
        self.database.connection.connect()
        self.clearFields()

    def setViewListUI(self):
        self.database.connection.close()
        self.contentField.setCurrentIndex(1)
        self.buscar_listas()

    def setGenResumeUI(self):
        self.database.connection.close()
        self.contentField.setCurrentIndex(2)
        self.database.connection.connect()
        self.cbAnoInforme.clear()
        self.cbAnoInforme.addItems(self.years)

    def setFirefighterDataUI(self):
        self.database.connection.close()
        self.contentField.setCurrentIndex(3)
        self.buscar_bomberos()

    def setLicenceUI(self):
        self.database.connection.close()
        self.contentField.setCurrentIndex(4)
        self.buscarLicencias()

    def limpiarLicencia(self):
        self.inpCorrLic.clear()
        self.inpRegLic.clear()
        self.txtMotivoLic.clear()

    def updateLicencia(self):
        try:
            licencia = Licencia(self.inpCorrLic.text(), self.inpRegLic.text(), self.dateDesdeLic.text(),
                                self.dateHastaLic.text(), self.txtMotivoLic.toPlainText(),
                                self.license_states[self.cbVBCapitan.checkState().value])
            licencia.licenciaUpdate()
            self.buscarLicencias()
            QtWidgets.QMessageBox.information(self, "Licencias", "Licencia actualizada con éxito")
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
            )

    def saveLicencia(self):
        try:
            licencia = Licencia(self.inpCorrLic.text(), self.inpRegLic.text(), self.dateDesdeLic.text(),
                                self.dateHastaLic.text(), self.txtMotivoLic.toPlainText(),
                                self.license_states[self.cbVBCapitan.checkState().value])
            licencia.nv_lic()
            QtWidgets.QMessageBox.information(self, "Licencias", "Licencia guardada con éxito")
            self.buscarLicencias()
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
            )

    def buscarNombre(self):
        try:
            self.inpNomLic.setText(self.database.get_nameVols(self.inpRegLic.text()))
        except Exception as e:
            pass

    def getLicencia(self, seleccion):
        if seleccion.indexes():
            fila = seleccion.indexes()[0].row()
            cLic = self.tblLicencias.model().index(fila, 0).data()
            CorrLic, nReg, fDesde, fHasta, motivo, aprobado = self.database.get_LicCont(cLic)
            self.inpCorrLic.setText(CorrLic)
            self.inpNomLic.setText(self.database.get_nameVols(nReg))
            self.inpRegLic.setText(nReg)
            self.dateDesdeLic.setDateTime(fDesde)
            self.dateHastaLic.setDateTime(fHasta)
            self.txtMotivoLic.setText(motivo)
            self.cbVBCapitan.setCheckState(self.cb_license_states[aprobado])

    def buscarLicencias(self):
        self.database.connection.connect()
        self.clearTable(self.tblLicencias)
        # try:
        lics = self.database.get_ListLic(self.inpSrcLic.text())
        for i in range(len(lics)):
            cLic, nombre, apellido1, apellido2, fDesde, fHasta = lics[i]
            fNombre = f'{nombre} {apellido1} {apellido2}'
            self.tblLicencias.insertRow(i)
            self.tblLicencias.setItem(i, 0, QtWidgets.QTableWidgetItem(cLic))
            self.tblLicencias.setItem(i, 1, QtWidgets.QTableWidgetItem(fNombre))
            self.tblLicencias.setItem(i, 2, QtWidgets.QTableWidgetItem(str(fDesde)))
            self.tblLicencias.setItem(i, 3, QtWidgets.QTableWidgetItem(str(fHasta)))
        # except Exception as e:
        #     pass

    def informePersonal(self):
        try:
            informe_personal = Informe(self)
            informe_personal.informe_personal(self.fldInfoPersonal.text())
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
            )
            return

    # TODO: Reformat or redesign this function
    # def arrastre(self):
    #     try:
    #         arrastrePath = self.getSaveFile()
    #         arrastre = self.database.getArrastre(self.infoFechaDesde.text(), self.infoFechaHasta.text())
    #         open(os.path.abspath('resources/template.html'), 'w').write(arrastre)
    #         with open(os.path.abspath('resources/template.html')) as f:
    #             pdfkit.from_file(f, arrastrePath, options={'page-size': 'Legal', 'encoding': 'UTF-8'})
    #         os.startfile(arrastrePath)
    #     except Exception as e:
    #         dialogo = QtWidgets.QMessageBox.warning(
    #             self, "Error", f"Ha ocurrido un error generando el arrastre.\n Código de error: {e}"
    #         )
    #         return

    # DONE
    def informe90dias(self):

        try:
            _90Dias = Informe(self)
            _90Dias.info90()
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error generando el informe.\n Código de error: {e}"
            )
            return

    # DONE
    def resumenEspecifico(self):
        try:
            InformeEspecifico = Informe(self, DateStart=self.infoFechaDesde.text(), DateEnd=self.infoFechaHasta.text())

            InformeEspecifico.resEspecifico()
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error generando el informe.\n Código de error: {e}"
            )
            return

    # DONE
    def resumenMensual(self):
        try:
            InformeMensual = Informe(self, month=self.cbMesInforme.currentText(), year=self.cbAnoInforme.currentText())
            InformeMensual.resMensual()
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error generando el informe.\n Código de error: {e}"
            )
            return

    # DONE*
    def insert_vol(self):
        try:
            nVoluntario = Voluntario(rGeneral=self.fldRegGral.text(), 
                                     rCia=self.fldRegCia.text(), 
                                     nombre=self.fldNombre.text(),
                                     apellidoP=self.fldApellidoP.text(), 
                                     apellidoM=self.fldApellidoM.text(),
                                     eMail=self.fldeMail.text(), 
                                     Sub_Estado=self.cbSubEstado.currentText())
            nVoluntario.fIngreso = Filter.Filter_Date(self.fldFechaIn.text())
            nVoluntario.set_fullRut(self.fldRut.text())
            nVoluntario.addVols()
            self.vols[self.fldRegGral.text()] = nVoluntario
            self.buscar_bomberos()
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
            )
            return

    def editar_vol(self):
        try:
            _EditedFirefighter = Voluntario(rGeneral=self.fldRegGral.text(), 
                                            rCia=self.fldRegCia.text(), 
                                            nombre=self.fldNombre.text(),
                                            apellidoP=self.fldApellidoP.text(), 
                                            apellidoM=self.fldApellidoM.text(),
                                            eMail=self.fldeMail.text(),
                                            Sub_Estado=self.cbSubEstado.currentText())
            _EditedFirefighter.fIngreso = Filter.Filter_Date(self.fldFechaIn.text())
            _EditedFirefighter.set_fullRut(self.fldRut.text())
            _EditedFirefighter.editVol()
            self.vols[self.fldRegGral.text()] = _EditedFirefighter
            aviso = QtWidgets.QMessageBox.information(self, "Guardar", "Información actualizada exitosamente")
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
            )
            return

    def getBombero(self, seleccion):
        if seleccion.indexes():
            fila = seleccion.indexes()[0].row()
            cCia = self.tblAdminVols.model().index(fila, 0).data()
            bombero = self.vols[cCia]
            self.fldRegGral.setText(bombero.rGeneral)
            self.fldRegCia.setText(str(bombero.rCia))
            self.fldNombre.setText(bombero.nombre)
            self.fldApellidoP.setText(bombero.apellidoP)
            self.fldApellidoM.setText(bombero.apellidoM)
            self.fldRut.setText(f'{bombero.rut}-{bombero.dv}')
            self.fldeMail.setText(bombero.eMail)
            self.fldFechaIn.setDate(bombero.fIngreso)
            self.cbSubEstado.setCurrentText(bombero.Sub_Estado)
            self.selectedFirefighter = bombero

    def buscar_bomberos(self):
        self.clearTable(self.tblAdminVols)
        i = 0
        for bombero in self.vols.values():
            self.tblAdminVols.insertRow(i)
            self.tblAdminVols.setItem(i, 0, QtWidgets.QTableWidgetItem(bombero.rGeneral))
            self.tblAdminVols.setItem(i, 1, QtWidgets.QTableWidgetItem(f'{bombero.nombre} {bombero.apellidoP} {bombero.apellidoM}'))
            i += 1
    def edit_list(self):
        try:
            self.get_carros()
            cCia = self.liListsView.model().index(self.liListsView.currentRow(), 0).data()
            lista = Acto(ccia= cCia,
                         acto= self.cb_espAct.currentText(), 
                         cgral= self.inpCorrGenEdit.text(), 
                         date= self.inpFechaEdit.text(),
                         address=self.inpDireccionEdit.text(), 
                         lista=self.efectiva_estate_in[self.cbEfectivaEdit.checkState().value],
                         carros=self.unidades_asistentes)
            lista.set_vols(self.lista)
            lista.set_qty_vols()
            lista.editLista()
            self.actos[cCia] = lista
            aviso = QtWidgets.QMessageBox.information(self, "Guardar", "Lista guardada exitosamente")
            self.buscar_listas()
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
            )
            return

    def delete_list(self):
        alerta = QtWidgets.QMessageBox.warning(
            self, "Aviso", "¿Seguro que desea eliminar la lista?",
            buttons=QtWidgets.QMessageBox.Apply | QtWidgets.QMessageBox.Cancel
        )
        if alerta == QtWidgets.QMessageBox.Apply:
            try:
                cCia = self.liListsView.model().index(self.liListsView.currentRow(), 0).data()
                self.database.delLista(cCia)
                dialogo = QtWidgets.QMessageBox.information(
                    self, "Cambios aplicados", "Lista eliminada con exito"
                )
                self.actos.pop(cCia)
                self.buscar_listas()
            except Exception as e:
                dialogo = QtWidgets.QMessageBox.warning(
                    self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
                )
                return
        else:
            return

    def getActo(self, seleccion):
        if seleccion.indexes():
            self.lista.clear()
            fila = seleccion.indexes()[0].row()
            cCia = self.liListsView.model().index(fila, 0).data()
            self.inpCorrGenEdit.setText(str(self.actos[cCia].general_cor))
            self.cb_catAct.setCurrentText(self.filter_Act(self.actos[cCia].act_type))
            self.setSubClassList(self.cb_catAct, self.cb_espAct)
            self.cb_espAct.setCurrentText(self.actos[cCia].act_type)
            self.inpDireccionEdit.setText(self.actos[cCia].address)
            self.inpFechaEdit.setDate(self.actos[cCia].date)
            self.cbEfectivaEdit.setCheckState(self.cb_efectiva_edit_estates[self.actos[cCia].lista])
            self.clearTable(self.liVolsEdit)
            if len(self.actos[cCia].vols) == 0:
                vols = self.database.extVols(cCia)
                for i in range(len(vols)):
                    rGral, nombre, apellido1, apellido2 = vols[i]
                    self.liVolsEdit.insertRow(i)
                    self.liVolsEdit.setItem(i, 0, QtWidgets.QTableWidgetItem(rGral))
                    self.liVolsEdit.setItem(i, 1, QtWidgets.QTableWidgetItem(f'{nombre} {apellido1} {apellido2}'))
                    self.lista.add(rGral)
                self.lbl_cVolsEdit.setText(str(len(self.lista)))
                self.actos[cCia].set_vols(self.lista)
                self.actos[cCia].set_qty_vols()
            else:
                i = 1
                for vol in self.actos[cCia].vols:
                    self.liVolsEdit.insertRow(i)
                    self.liVolsEdit.setItem(i, 0, QtWidgets.QTableWidgetItem(vol))
                    self.liVolsEdit.setItem(i, 1, QtWidgets.QTableWidgetItem(f'{self.vols[vol].nombre} {self.vols[vol].apellidoP} {self.vols[vol].apellidoM}'))
                    self.lista.add(vol)
                    i += 1
                self.lbl_cVolsEdit.setText(str(self.actos[cCia].qty_vols))
            self.set_carros(self.actos[cCia].carros)


    def buscar_listas(self):
        rowIndex = 0
        self.clearTable(self.liListsView)
        for acto in self.actos.values():
            if (acto.date.year == int(self.cb_srcYear.currentText()) and acto.date.month == self.months.get(self.cb_srcMonth.currentText())) :
                self.liListsView.insertRow(rowIndex)
                self.liListsView.setItem(rowIndex, 0, QtWidgets.QTableWidgetItem(acto.company_cor))
                self.liListsView.setItem(rowIndex, 1, QtWidgets.QTableWidgetItem(str(acto.date)))
                self.liListsView.setItem(rowIndex, 2, QtWidgets.QTableWidgetItem(acto.act_type))
                self.liListsView.setItem(rowIndex, 3, QtWidgets.QTableWidgetItem(acto.address))
                rowIndex += 1
    def add_vol_to_list(self, input_vol):
        try:
            if self.contentField.currentIndex() == 0:
                rowPosition = self.liVols.rowCount()
                if input_vol not in self.lista:
                    self.liVols.insertRow(rowPosition)
                    self.liVols.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(self.vols[input_vol].rGeneral))
                    self.liVols.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(f'{self.vols[input_vol].nombre} {self.vols[input_vol].apellidoP} {self.vols[input_vol].apellidoM}'))
                    self.inpVol.clear()
                    self.lista.add(input_vol)
                    self.lblTotalLista.setText(str(len(self.lista)))
                else:
                    self.inpVol.clear()
                    return
            elif self.contentField.currentIndex() == 1:
                rowPosition = self.liVolsEdit.rowCount()
                if input_vol not in self.lista:
                    self.liVolsEdit.insertRow(rowPosition)
                    self.liVolsEdit.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(self.vols[input_vol].rGeneral))
                    self.liVolsEdit.setItem(rowPosition, 1,
                                            QtWidgets.QTableWidgetItem(f'{self.vols[input_vol].nombre} {self.vols[input_vol].apellidoP} {self.vols[input_vol].apellidoM}'))
                    self.inpAddVolEdit.clear()
                    self.lista.add(input_vol)
                    self.lbl_cVolsEdit.setText(str(len(self.lista)))
                else:
                    self.inpAddVolEdit.clear()
                    return
                return
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Voluntario no encontrado.\n Código de error: {e}"
            )
            return

    def del_vol_to_list(self):
        if self.contentField.currentIndex() == 0:
            self.lista.remove(self.liVols.model().index(self.liVols.currentRow(), 0).data())
            self.liVols.removeRow(self.liVols.currentRow())
            self.lblTotalLista.setText(str(len(self.lista)))
        elif self.contentField.currentIndex() == 1:
            self.lista.remove(self.liVolsEdit.model().index(self.liVolsEdit.currentRow(), 0).data())
            self.liVolsEdit.removeRow(self.liVolsEdit.currentRow())
            self.lbl_cVolsEdit.setText(str(len(self.lista)))
            return

    @staticmethod
    def clearTable(table):
        for i in range(table.rowCount(), -1, -1):
            table.removeRow(i)

    def clearFields(self):
        self.lista.clear()
        self.inpDireccion.clear()
        self.inpCorrCia.clear()
        self.inpCorrGral.clear()
        self.clearTable(self.liVols)
        self.cbEfectiva.setCheckState(QtCore.Qt.CheckState.Unchecked)
        self.lblTotalLista.setText(str(len(self.lista)))
        self.cbAnoInforme.clear()
        self.cbAnoInforme.addItems(self.years)
        self.unidades_asistentes.clear()
        for value in self.ingreso_carros.values():
            value.setCheckState(QtCore.Qt.CheckState.Unchecked)

    def save_list(self):
        try:
            self.get_carros()
            acto = Acto(ccia= self.inpCorrCia.text(), 
                        acto= self.cb_actC2.currentText(), 
                        cgral= self.inpCorrGral.text(),
                        date= self.inpFecha.text(),
                        address= self.inpDireccion.text(), 
                        lista= self.efectiva_estate_in[self.cbEfectiva.checkState().value],
                        carros= self.unidades_asistentes)
            acto.set_vols(self.lista)
            acto.set_qty_vols()
            acto.addLista()
            aviso = QtWidgets.QMessageBox.information(self, "Guardar", "Lista guardada exitosamente")
            self.actos[self.inpCorrCia.text()] = acto
            self.clearFields()
        except Exception as e:
            dialogo = QtWidgets.QMessageBox.warning(
                self, "Error", f"Ha ocurrido un error.\n Código de error: {e}"
            )
            return

    @staticmethod
    def show_help_manual():
        os.startfile(os.path.abspath("resources\\Instructivo Sistema de Estadistica.pdf"))
        return

    def show_app_info(self):
        QtWidgets.QMessageBox.information(self, "Información",
                                          f"Versión: {self.information['version']} \nAutor: {self.information['autor']} \n © 2023 por Andrés Bahamondes")
        return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())
