# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacepnQxVK.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDateTimeEdit, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
import lib.Recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 638)
        MainWindow.setMinimumSize(QSize(1080, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/Logos/CbpaLogo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	font-family: \"Roboto Medium\";\n"
"}\n"
"\n"
"#SideBar, #actionMenu, #infoMenu{\n"
"	background-color: #424242;\n"
"}\n"
"\n"
"QPushButton{\n"
"	cursor: pointer;\n"
"}")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#SideBar QPushButton{\n"
"background-color: transparent;\n"
"color: #f5f5f5;\n"
"border: none;\n"
"border-radius: 10%;\n"
"transition: all .5s;\n"
"text-align: left;\n"
"padding: 0.5em;\n"
"}\n"
"#SideBar QPushButton:hover{\n"
"background-color: #4a4a4a;\n"
"font-weight: 700;\n"
"}\n"
"QLineEdit, QTableWidget, QDateEdit{\n"
"border-radius: 4px;\n"
"border: 0.5px solid lightgrey;\n"
"}\n"
"\n"
"#SideBar #btnInsertList{\n"
"	text-align: center;\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-radius: 2em;\n"
"	border-color: #8ab4f8;\n"
"	color: #8ab4f8;\n"
"}\n"
"\n"
"#SideBar #btnInsertList:hover{\n"
"	background-color: rgba(138,180,248,.1);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SideBar = QWidget(self.centralwidget)
        self.SideBar.setObjectName(u"SideBar")
        self.verticalLayout_3 = QVBoxLayout(self.SideBar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.actionMenu = QWidget(self.SideBar)
        self.actionMenu.setObjectName(u"actionMenu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionMenu.sizePolicy().hasHeightForWidth())
        self.actionMenu.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Roboto Medium"])
        font.setBold(True)
        self.actionMenu.setFont(font)
        self.verticalLayout = QVBoxLayout(self.actionMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnInsertList = QPushButton(self.actionMenu)
        self.btnInsertList.setObjectName(u"btnInsertList")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnInsertList.sizePolicy().hasHeightForWidth())
        self.btnInsertList.setSizePolicy(sizePolicy1)
        self.btnInsertList.setMinimumSize(QSize(0, 0))
        self.btnInsertList.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnInsertList.setIcon(icon1)

        self.verticalLayout.addWidget(self.btnInsertList)

        self.btnViewList = QPushButton(self.actionMenu)
        self.btnViewList.setObjectName(u"btnViewList")
        sizePolicy1.setHeightForWidth(self.btnViewList.sizePolicy().hasHeightForWidth())
        self.btnViewList.setSizePolicy(sizePolicy1)
        self.btnViewList.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnViewList.setIcon(icon2)

        self.verticalLayout.addWidget(self.btnViewList)

        self.btnGenInforms = QPushButton(self.actionMenu)
        self.btnGenInforms.setObjectName(u"btnGenInforms")
        sizePolicy1.setHeightForWidth(self.btnGenInforms.sizePolicy().hasHeightForWidth())
        self.btnGenInforms.setSizePolicy(sizePolicy1)
        self.btnGenInforms.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Icons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnGenInforms.setIcon(icon3)

        self.verticalLayout.addWidget(self.btnGenInforms)

        self.btnAdminVols = QPushButton(self.actionMenu)
        self.btnAdminVols.setObjectName(u"btnAdminVols")
        sizePolicy1.setHeightForWidth(self.btnAdminVols.sizePolicy().hasHeightForWidth())
        self.btnAdminVols.setSizePolicy(sizePolicy1)
        self.btnAdminVols.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Icons/user-check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAdminVols.setIcon(icon4)

        self.verticalLayout.addWidget(self.btnAdminVols)

        self.btnLicencias = QPushButton(self.actionMenu)
        self.btnLicencias.setObjectName(u"btnLicencias")
        sizePolicy1.setHeightForWidth(self.btnLicencias.sizePolicy().hasHeightForWidth())
        self.btnLicencias.setSizePolicy(sizePolicy1)
        self.btnLicencias.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Icons/inbox.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLicencias.setIcon(icon5)

        self.verticalLayout.addWidget(self.btnLicencias)


        self.verticalLayout_3.addWidget(self.actionMenu)

        self.infoMenu = QWidget(self.SideBar)
        self.infoMenu.setObjectName(u"infoMenu")
        self.verticalLayout_2 = QVBoxLayout(self.infoMenu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnInfo = QPushButton(self.infoMenu)
        self.btnInfo.setObjectName(u"btnInfo")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnInfo.setIcon(icon6)

        self.verticalLayout_2.addWidget(self.btnInfo)

        self.btnHelp = QPushButton(self.infoMenu)
        self.btnHelp.setObjectName(u"btnHelp")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/Icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnHelp.setIcon(icon7)

        self.verticalLayout_2.addWidget(self.btnHelp)


        self.verticalLayout_3.addWidget(self.infoMenu)


        self.horizontalLayout.addWidget(self.SideBar)

        self.contentField = QStackedWidget(self.centralwidget)
        self.contentField.setObjectName(u"contentField")
        self.contentField.setStyleSheet(u"Qwidget QPushButton{\n"
"	cursor: pointer;\n"
"	\n"
"}")
        self.pageInsert = QWidget()
        self.pageInsert.setObjectName(u"pageInsert")
        self.verticalLayout_10 = QVBoxLayout(self.pageInsert)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.pageInsert)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.inpCorrCia = QLineEdit(self.pageInsert)
        self.inpCorrCia.setObjectName(u"inpCorrCia")
        self.inpCorrCia.setMinimumSize(QSize(80, 0))
        self.inpCorrCia.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_6.addWidget(self.inpCorrCia)

        self.cbEfectiva = QCheckBox(self.pageInsert)
        self.cbEfectiva.setObjectName(u"cbEfectiva")

        self.horizontalLayout_6.addWidget(self.cbEfectiva)

        self.label_2 = QLabel(self.pageInsert)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.inpCorrGral = QLineEdit(self.pageInsert)
        self.inpCorrGral.setObjectName(u"inpCorrGral")
        self.inpCorrGral.setMinimumSize(QSize(80, 0))
        self.inpCorrGral.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_6.addWidget(self.inpCorrGral)

        self.label_41 = QLabel(self.pageInsert)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(36, 16777215))

        self.horizontalLayout_6.addWidget(self.label_41)

        self.cb_actC1 = QComboBox(self.pageInsert)
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.addItem("")
        self.cb_actC1.setObjectName(u"cb_actC1")
        self.cb_actC1.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.cb_actC1)

        self.label_5 = QLabel(self.pageInsert)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.cb_actC2 = QComboBox(self.pageInsert)
        self.cb_actC2.setObjectName(u"cb_actC2")

        self.horizontalLayout_6.addWidget(self.cb_actC2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.pageInsert)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.inpDireccion = QLineEdit(self.pageInsert)
        self.inpDireccion.setObjectName(u"inpDireccion")

        self.horizontalLayout_7.addWidget(self.inpDireccion)

        self.label_4 = QLabel(self.pageInsert)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.inpFecha = QDateEdit(self.pageInsert)
        self.inpFecha.setObjectName(u"inpFecha")

        self.horizontalLayout_7.addWidget(self.inpFecha)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.liVols = QTableWidget(self.pageInsert)
        if (self.liVols.columnCount() < 2):
            self.liVols.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.liVols.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.liVols.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.liVols.setObjectName(u"liVols")
        self.liVols.setMinimumSize(QSize(600, 0))
        self.liVols.setAutoFillBackground(False)
        self.liVols.setStyleSheet(u"")
        self.liVols.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.liVols.setSelectionMode(QAbstractItemView.SingleSelection)
        self.liVols.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_8.addWidget(self.liVols)

        self.newListActions = QVBoxLayout()
        self.newListActions.setObjectName(u"newListActions")
        self.newListActions.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_29 = QLabel(self.pageInsert)
        self.label_29.setObjectName(u"label_29")

        self.newListActions.addWidget(self.label_29)

        self.lblTotalLista = QLabel(self.pageInsert)
        self.lblTotalLista.setObjectName(u"lblTotalLista")

        self.newListActions.addWidget(self.lblTotalLista)

        self.label_6 = QLabel(self.pageInsert)
        self.label_6.setObjectName(u"label_6")

        self.newListActions.addWidget(self.label_6)

        self.inpVol = QLineEdit(self.pageInsert)
        self.inpVol.setObjectName(u"inpVol")

        self.newListActions.addWidget(self.inpVol)

        self.btnAddVol = QPushButton(self.pageInsert)
        self.btnAddVol.setObjectName(u"btnAddVol")

        self.newListActions.addWidget(self.btnAddVol)

        self.btnDelVol = QPushButton(self.pageInsert)
        self.btnDelVol.setObjectName(u"btnDelVol")

        self.newListActions.addWidget(self.btnDelVol)

        self.groupBox_3 = QGroupBox(self.pageInsert)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.cbInsertB9 = QCheckBox(self.groupBox_3)
        self.cbInsertB9.setObjectName(u"cbInsertB9")

        self.horizontalLayout_9.addWidget(self.cbInsertB9)

        self.cbInsertUT9 = QCheckBox(self.groupBox_3)
        self.cbInsertUT9.setObjectName(u"cbInsertUT9")

        self.horizontalLayout_9.addWidget(self.cbInsertUT9)

        self.cbInsertM9 = QCheckBox(self.groupBox_3)
        self.cbInsertM9.setObjectName(u"cbInsertM9")

        self.horizontalLayout_9.addWidget(self.cbInsertM9)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)


        self.newListActions.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.newListActions.addItem(self.verticalSpacer)

        self.btnSave = QPushButton(self.pageInsert)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMaximumSize(QSize(16777215, 16777215))
        icon8 = QIcon()
        icon8.addFile(u":/Icons/Icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSave.setIcon(icon8)

        self.newListActions.addWidget(self.btnSave)


        self.horizontalLayout_8.addLayout(self.newListActions)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.contentField.addWidget(self.pageInsert)
        self.pageView = QWidget()
        self.pageView.setObjectName(u"pageView")
        self.horizontalLayout_2 = QHBoxLayout(self.pageView)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.viewLl = QWidget(self.pageView)
        self.viewLl.setObjectName(u"viewLl")
        self.verticalLayout_4 = QVBoxLayout(self.viewLl)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_10 = QLabel(self.viewLl)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_18.addWidget(self.label_10)

        self.cb_srcMonth = QComboBox(self.viewLl)
        self.cb_srcMonth.setObjectName(u"cb_srcMonth")
        self.cb_srcMonth.setMinimumSize(QSize(124, 0))

        self.horizontalLayout_18.addWidget(self.cb_srcMonth)

        self.cb_srcYear = QComboBox(self.viewLl)
        self.cb_srcYear.setObjectName(u"cb_srcYear")
        self.cb_srcYear.setMinimumSize(QSize(92, 0))

        self.horizontalLayout_18.addWidget(self.cb_srcYear)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_18)

        self.liListsView = QTableWidget(self.viewLl)
        if (self.liListsView.columnCount() < 4):
            self.liListsView.setColumnCount(4)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.liListsView.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.liListsView.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.liListsView.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.liListsView.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        self.liListsView.setObjectName(u"liListsView")
        self.liListsView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.liListsView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.liListsView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.liListsView.horizontalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_4.addWidget(self.liListsView)


        self.horizontalLayout_2.addWidget(self.viewLl)

        self.editLl = QWidget(self.pageView)
        self.editLl.setObjectName(u"editLl")
        self.editLl.setEnabled(True)
        self.editLl.setMaximumSize(QSize(368, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.editLl)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.actEdit = QWidget(self.editLl)
        self.actEdit.setObjectName(u"actEdit")
        self.verticalLayout_6 = QVBoxLayout(self.actEdit)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.actEdit)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.inpCorrGenEdit = QLineEdit(self.actEdit)
        self.inpCorrGenEdit.setObjectName(u"inpCorrGenEdit")
        self.inpCorrGenEdit.setMinimumSize(QSize(80, 0))
        self.inpCorrGenEdit.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.inpCorrGenEdit)

        self.cbEfectivaEdit = QCheckBox(self.actEdit)
        self.cbEfectivaEdit.setObjectName(u"cbEfectivaEdit")

        self.horizontalLayout_3.addWidget(self.cbEfectivaEdit)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.actEdit)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(48, 16777215))

        self.horizontalLayout_11.addWidget(self.label_11)

        self.inpFechaEdit = QDateEdit(self.actEdit)
        self.inpFechaEdit.setObjectName(u"inpFechaEdit")
        self.inpFechaEdit.setMaximumSize(QSize(84, 16777215))

        self.horizontalLayout_11.addWidget(self.inpFechaEdit)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.actEdit)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.inpDireccionEdit = QLineEdit(self.actEdit)
        self.inpDireccionEdit.setObjectName(u"inpDireccionEdit")

        self.horizontalLayout_5.addWidget(self.inpDireccionEdit)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_40 = QLabel(self.actEdit)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(36, 16777215))

        self.horizontalLayout_15.addWidget(self.label_40)

        self.cb_catAct = QComboBox(self.actEdit)
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.addItem("")
        self.cb_catAct.setObjectName(u"cb_catAct")
        self.cb_catAct.setMinimumSize(QSize(93, 0))
        self.cb_catAct.setMaximumSize(QSize(93, 16777215))

        self.horizontalLayout_15.addWidget(self.cb_catAct)

        self.label_8 = QLabel(self.actEdit)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(93, 16777215))

        self.horizontalLayout_15.addWidget(self.label_8)

        self.cb_espAct = QComboBox(self.actEdit)
        self.cb_espAct.setObjectName(u"cb_espAct")
        self.cb_espAct.setMinimumSize(QSize(93, 0))
        self.cb_espAct.setMaximumSize(QSize(93, 16777215))

        self.horizontalLayout_15.addWidget(self.cb_espAct)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)


        self.verticalLayout_5.addWidget(self.actEdit)

        self.volsEdit = QWidget(self.editLl)
        self.volsEdit.setObjectName(u"volsEdit")
        self.verticalLayout_7 = QVBoxLayout(self.volsEdit)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_31 = QLabel(self.volsEdit)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_13.addWidget(self.label_31)

        self.lbl_cVolsEdit = QLabel(self.volsEdit)
        self.lbl_cVolsEdit.setObjectName(u"lbl_cVolsEdit")

        self.horizontalLayout_13.addWidget(self.lbl_cVolsEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.label_12 = QLabel(self.volsEdit)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_7.addWidget(self.label_12)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.inpAddVolEdit = QLineEdit(self.volsEdit)
        self.inpAddVolEdit.setObjectName(u"inpAddVolEdit")

        self.horizontalLayout_12.addWidget(self.inpAddVolEdit)

        self.btnAddVol_2 = QPushButton(self.volsEdit)
        self.btnAddVol_2.setObjectName(u"btnAddVol_2")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/Icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAddVol_2.setIcon(icon9)

        self.horizontalLayout_12.addWidget(self.btnAddVol_2)

        self.btnDelVol_2 = QPushButton(self.volsEdit)
        self.btnDelVol_2.setObjectName(u"btnDelVol_2")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/Icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDelVol_2.setIcon(icon10)

        self.horizontalLayout_12.addWidget(self.btnDelVol_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.liVolsEdit = QTableWidget(self.volsEdit)
        if (self.liVolsEdit.columnCount() < 2):
            self.liVolsEdit.setColumnCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.liVolsEdit.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.liVolsEdit.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        self.liVolsEdit.setObjectName(u"liVolsEdit")
        self.liVolsEdit.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.liVolsEdit.setSelectionMode(QAbstractItemView.SingleSelection)
        self.liVolsEdit.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_7.addWidget(self.liVolsEdit)

        self.groupBox_4 = QGroupBox(self.volsEdit)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(168, 16777215))
        self.groupBox_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.cbEditB9 = QCheckBox(self.groupBox_4)
        self.cbEditB9.setObjectName(u"cbEditB9")

        self.horizontalLayout_10.addWidget(self.cbEditB9)

        self.cbEditUT9 = QCheckBox(self.groupBox_4)
        self.cbEditUT9.setObjectName(u"cbEditUT9")

        self.horizontalLayout_10.addWidget(self.cbEditUT9)

        self.cbEditM9 = QCheckBox(self.groupBox_4)
        self.cbEditM9.setObjectName(u"cbEditM9")

        self.horizontalLayout_10.addWidget(self.cbEditM9)


        self.verticalLayout_7.addWidget(self.groupBox_4)


        self.verticalLayout_5.addWidget(self.volsEdit)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btnSaveEdit = QPushButton(self.editLl)
        self.btnSaveEdit.setObjectName(u"btnSaveEdit")
        self.btnSaveEdit.setMinimumSize(QSize(192, 0))
        self.btnSaveEdit.setMaximumSize(QSize(192, 16777215))
        self.btnSaveEdit.setIcon(icon8)

        self.horizontalLayout_14.addWidget(self.btnSaveEdit)

        self.btnDeleteEdit = QPushButton(self.editLl)
        self.btnDeleteEdit.setObjectName(u"btnDeleteEdit")
        self.btnDeleteEdit.setMinimumSize(QSize(96, 0))
        self.btnDeleteEdit.setMaximumSize(QSize(96, 16777215))
        icon11 = QIcon()
        icon11.addFile(u":/Icons/Icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDeleteEdit.setIcon(icon11)

        self.horizontalLayout_14.addWidget(self.btnDeleteEdit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_2.addWidget(self.editLl)

        self.contentField.addWidget(self.pageView)
        self.pageInform = QWidget()
        self.pageInform.setObjectName(u"pageInform")
        self.verticalLayout_12 = QVBoxLayout(self.pageInform)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.groupBox = QGroupBox(self.pageInform)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 20, 351, 60))
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_4.addWidget(self.label_15)

        self.cbMesInforme = QComboBox(self.groupBox_2)
        self.cbMesInforme.addItem("")
        self.cbMesInforme.addItem("")
        self.cbMesInforme.addItem("")
        self.cbMesInforme.addItem("")
        self.cbMesInforme.addItem("")
        self.cbMesInforme.addItem("")
        self.cbMesInforme.addItem("")
        self.cbMesInforme.addItem("")
        self.cbMesInforme.addItem("")
        self.cbMesInforme.addItem("")
        self.cbMesInforme.addItem("")
        self.cbMesInforme.addItem("")
        self.cbMesInforme.setObjectName(u"cbMesInforme")

        self.horizontalLayout_4.addWidget(self.cbMesInforme)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_4.addWidget(self.label_16)

        self.cbAnoInforme = QComboBox(self.groupBox_2)
        self.cbAnoInforme.setObjectName(u"cbAnoInforme")

        self.horizontalLayout_4.addWidget(self.cbAnoInforme)

        self.btnResMen = QPushButton(self.groupBox_2)
        self.btnResMen.setObjectName(u"btnResMen")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnResMen.sizePolicy().hasHeightForWidth())
        self.btnResMen.setSizePolicy(sizePolicy2)
        self.btnResMen.setMinimumSize(QSize(96, 0))
        self.btnResMen.setMaximumSize(QSize(96, 16777215))

        self.horizontalLayout_4.addWidget(self.btnResMen)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 90, 591, 141))
        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 20, 431, 51))
        self.label_14 = QLabel(self.groupBox_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 20, 71, 16))
        self.label_14.setMinimumSize(QSize(71, 0))
        self.label_14.setMaximumSize(QSize(71, 16777215))
        self.infoFechaDesde = QDateEdit(self.groupBox_6)
        self.infoFechaDesde.setObjectName(u"infoFechaDesde")
        self.infoFechaDesde.setGeometry(QRect(90, 20, 81, 22))
        self.infoFechaDesde.setMinimumSize(QSize(81, 0))
        self.infoFechaDesde.setMaximumSize(QSize(81, 16777215))
        self.label_17 = QLabel(self.groupBox_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(180, 20, 71, 16))
        self.label_17.setMinimumSize(QSize(71, 0))
        self.label_17.setMaximumSize(QSize(71, 16777215))
        self.infoFechaHasta = QDateEdit(self.groupBox_6)
        self.infoFechaHasta.setObjectName(u"infoFechaHasta")
        self.infoFechaHasta.setGeometry(QRect(250, 20, 81, 22))
        self.infoFechaHasta.setMinimumSize(QSize(81, 0))
        self.infoFechaHasta.setMaximumSize(QSize(81, 16777215))
        self.btnGenResEsp = QPushButton(self.groupBox_6)
        self.btnGenResEsp.setObjectName(u"btnGenResEsp")
        self.btnGenResEsp.setGeometry(QRect(340, 20, 75, 24))
        self.btnInfo90Dias = QPushButton(self.groupBox_5)
        self.btnInfo90Dias.setObjectName(u"btnInfo90Dias")
        self.btnInfo90Dias.setGeometry(QRect(450, 40, 111, 24))
        self.groupBox_7 = QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(10, 80, 561, 51))
        self.fldInfoPersonal = QLineEdit(self.groupBox_7)
        self.fldInfoPersonal.setObjectName(u"fldInfoPersonal")
        self.fldInfoPersonal.setGeometry(QRect(10, 20, 461, 21))
        self.btnGetInfoP = QPushButton(self.groupBox_7)
        self.btnGetInfoP.setObjectName(u"btnGetInfoP")
        self.btnGetInfoP.setGeometry(QRect(480, 20, 75, 24))

        self.verticalLayout_12.addWidget(self.groupBox)

        self.contentField.addWidget(self.pageInform)
        self.pageVols = QWidget()
        self.pageVols.setObjectName(u"pageVols")
        self.horizontalLayout_21 = QHBoxLayout(self.pageVols)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.widget = QWidget(self.pageVols)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_13 = QVBoxLayout(self.widget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_16.addWidget(self.label_13)

        self.fldSrcAdminVols = QLineEdit(self.widget)
        self.fldSrcAdminVols.setObjectName(u"fldSrcAdminVols")

        self.horizontalLayout_16.addWidget(self.fldSrcAdminVols)


        self.verticalLayout_13.addLayout(self.horizontalLayout_16)

        self.tblAdminVols = QTableWidget(self.widget)
        if (self.tblAdminVols.columnCount() < 2):
            self.tblAdminVols.setColumnCount(2)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblAdminVols.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblAdminVols.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        self.tblAdminVols.setObjectName(u"tblAdminVols")
        self.tblAdminVols.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblAdminVols.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblAdminVols.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_13.addWidget(self.tblAdminVols)


        self.horizontalLayout_21.addWidget(self.widget)

        self.widget_2 = QWidget(self.pageVols)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_14 = QVBoxLayout(self.widget_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_20 = QLabel(self.widget_2)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_14.addWidget(self.label_20)

        self.fldRegGral = QLineEdit(self.widget_2)
        self.fldRegGral.setObjectName(u"fldRegGral")

        self.verticalLayout_14.addWidget(self.fldRegGral)

        self.label_21 = QLabel(self.widget_2)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_14.addWidget(self.label_21)

        self.fldRegCia = QLineEdit(self.widget_2)
        self.fldRegCia.setObjectName(u"fldRegCia")

        self.verticalLayout_14.addWidget(self.fldRegCia)

        self.label_23 = QLabel(self.widget_2)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_14.addWidget(self.label_23)

        self.fldNombre = QLineEdit(self.widget_2)
        self.fldNombre.setObjectName(u"fldNombre")

        self.verticalLayout_14.addWidget(self.fldNombre)

        self.label_24 = QLabel(self.widget_2)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_14.addWidget(self.label_24)

        self.fldApellidoP = QLineEdit(self.widget_2)
        self.fldApellidoP.setObjectName(u"fldApellidoP")

        self.verticalLayout_14.addWidget(self.fldApellidoP)

        self.label_25 = QLabel(self.widget_2)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_14.addWidget(self.label_25)

        self.fldApellidoM = QLineEdit(self.widget_2)
        self.fldApellidoM.setObjectName(u"fldApellidoM")

        self.verticalLayout_14.addWidget(self.fldApellidoM)

        self.label_26 = QLabel(self.widget_2)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_14.addWidget(self.label_26)

        self.fldRut = QLineEdit(self.widget_2)
        self.fldRut.setObjectName(u"fldRut")

        self.verticalLayout_14.addWidget(self.fldRut)

        self.label_27 = QLabel(self.widget_2)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_14.addWidget(self.label_27)

        self.fldeMail = QLineEdit(self.widget_2)
        self.fldeMail.setObjectName(u"fldeMail")

        self.verticalLayout_14.addWidget(self.fldeMail)

        self.label_22 = QLabel(self.widget_2)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_14.addWidget(self.label_22)

        self.fldFechaIn = QDateEdit(self.widget_2)
        self.fldFechaIn.setObjectName(u"fldFechaIn")

        self.verticalLayout_14.addWidget(self.fldFechaIn)

        self.label_28 = QLabel(self.widget_2)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_14.addWidget(self.label_28)

        self.cbSubEstado = QComboBox(self.widget_2)
        self.cbSubEstado.addItem("")
        self.cbSubEstado.addItem("")
        self.cbSubEstado.addItem("")
        self.cbSubEstado.addItem("")
        self.cbSubEstado.addItem("")
        self.cbSubEstado.setObjectName(u"cbSubEstado")

        self.verticalLayout_14.addWidget(self.cbSubEstado)

        self.btnEditVol = QPushButton(self.widget_2)
        self.btnEditVol.setObjectName(u"btnEditVol")

        self.verticalLayout_14.addWidget(self.btnEditVol)

        self.btnAddVol_3 = QPushButton(self.widget_2)
        self.btnAddVol_3.setObjectName(u"btnAddVol_3")

        self.verticalLayout_14.addWidget(self.btnAddVol_3)

        self.btn_clflds = QPushButton(self.widget_2)
        self.btn_clflds.setObjectName(u"btn_clflds")

        self.verticalLayout_14.addWidget(self.btn_clflds)


        self.horizontalLayout_21.addWidget(self.widget_2)

        self.contentField.addWidget(self.pageVols)
        self.pageLicencia = QWidget()
        self.pageLicencia.setObjectName(u"pageLicencia")
        self.horizontalLayout_17 = QHBoxLayout(self.pageLicencia)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.layoutSrcLic = QVBoxLayout()
        self.layoutSrcLic.setObjectName(u"layoutSrcLic")
        self.label_38 = QLabel(self.pageLicencia)
        self.label_38.setObjectName(u"label_38")

        self.layoutSrcLic.addWidget(self.label_38)

        self.inpSrcLic = QLineEdit(self.pageLicencia)
        self.inpSrcLic.setObjectName(u"inpSrcLic")

        self.layoutSrcLic.addWidget(self.inpSrcLic)

        self.tblLicencias = QTableWidget(self.pageLicencia)
        if (self.tblLicencias.columnCount() < 4):
            self.tblLicencias.setColumnCount(4)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tblLicencias.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tblLicencias.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tblLicencias.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tblLicencias.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        self.tblLicencias.setObjectName(u"tblLicencias")
        self.tblLicencias.setMinimumSize(QSize(568, 0))
        self.tblLicencias.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblLicencias.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblLicencias.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.layoutSrcLic.addWidget(self.tblLicencias)


        self.horizontalLayout_17.addLayout(self.layoutSrcLic)

        self.layoutCRUDLic = QVBoxLayout()
        self.layoutCRUDLic.setObjectName(u"layoutCRUDLic")
        self.label_39 = QLabel(self.pageLicencia)
        self.label_39.setObjectName(u"label_39")

        self.layoutCRUDLic.addWidget(self.label_39)

        self.inpCorrLic = QLineEdit(self.pageLicencia)
        self.inpCorrLic.setObjectName(u"inpCorrLic")
        self.inpCorrLic.setMaxLength(5)

        self.layoutCRUDLic.addWidget(self.inpCorrLic)

        self.label_32 = QLabel(self.pageLicencia)
        self.label_32.setObjectName(u"label_32")

        self.layoutCRUDLic.addWidget(self.label_32)

        self.inpNomLic = QLineEdit(self.pageLicencia)
        self.inpNomLic.setObjectName(u"inpNomLic")
        self.inpNomLic.setEnabled(False)
        self.inpNomLic.setCursor(QCursor(Qt.ForbiddenCursor))
        self.inpNomLic.setReadOnly(False)

        self.layoutCRUDLic.addWidget(self.inpNomLic)

        self.label_33 = QLabel(self.pageLicencia)
        self.label_33.setObjectName(u"label_33")

        self.layoutCRUDLic.addWidget(self.label_33)

        self.inpRegLic = QLineEdit(self.pageLicencia)
        self.inpRegLic.setObjectName(u"inpRegLic")

        self.layoutCRUDLic.addWidget(self.inpRegLic)

        self.label_34 = QLabel(self.pageLicencia)
        self.label_34.setObjectName(u"label_34")

        self.layoutCRUDLic.addWidget(self.label_34)

        self.dateDesdeLic = QDateTimeEdit(self.pageLicencia)
        self.dateDesdeLic.setObjectName(u"dateDesdeLic")

        self.layoutCRUDLic.addWidget(self.dateDesdeLic)

        self.label_35 = QLabel(self.pageLicencia)
        self.label_35.setObjectName(u"label_35")

        self.layoutCRUDLic.addWidget(self.label_35)

        self.dateHastaLic = QDateTimeEdit(self.pageLicencia)
        self.dateHastaLic.setObjectName(u"dateHastaLic")

        self.layoutCRUDLic.addWidget(self.dateHastaLic)

        self.label_36 = QLabel(self.pageLicencia)
        self.label_36.setObjectName(u"label_36")

        self.layoutCRUDLic.addWidget(self.label_36)

        self.txtMotivoLic = QTextEdit(self.pageLicencia)
        self.txtMotivoLic.setObjectName(u"txtMotivoLic")

        self.layoutCRUDLic.addWidget(self.txtMotivoLic)

        self.label_37 = QLabel(self.pageLicencia)
        self.label_37.setObjectName(u"label_37")

        self.layoutCRUDLic.addWidget(self.label_37)

        self.cbVBCapitan = QCheckBox(self.pageLicencia)
        self.cbVBCapitan.setObjectName(u"cbVBCapitan")

        self.layoutCRUDLic.addWidget(self.cbVBCapitan)

        self.btnSaveLic = QPushButton(self.pageLicencia)
        self.btnSaveLic.setObjectName(u"btnSaveLic")

        self.layoutCRUDLic.addWidget(self.btnSaveLic)

        self.btnUpdateLic = QPushButton(self.pageLicencia)
        self.btnUpdateLic.setObjectName(u"btnUpdateLic")

        self.layoutCRUDLic.addWidget(self.btnUpdateLic)

        self.btnClLic = QPushButton(self.pageLicencia)
        self.btnClLic.setObjectName(u"btnClLic")

        self.layoutCRUDLic.addWidget(self.btnClLic)


        self.horizontalLayout_17.addLayout(self.layoutCRUDLic)

        self.contentField.addWidget(self.pageLicencia)

        self.horizontalLayout.addWidget(self.contentField)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.contentField.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema de Estadistica - Bomba Tobalaba", None))
        self.btnInsertList.setText(QCoreApplication.translate("MainWindow", u"Insertar Lista", None))
        self.btnViewList.setText(QCoreApplication.translate("MainWindow", u"Ver Servicios", None))
        self.btnGenInforms.setText(QCoreApplication.translate("MainWindow", u"Generar Informes", None))
        self.btnAdminVols.setText(QCoreApplication.translate("MainWindow", u"Administrar Bomberos", None))
        self.btnLicencias.setText(QCoreApplication.translate("MainWindow", u"Licencias", None))
        self.btnInfo.setText(QCoreApplication.translate("MainWindow", u"Informaci\u00f3n", None))
        self.btnHelp.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Correlativo Compa\u00f1\u00eda", None))
        self.cbEfectiva.setText(QCoreApplication.translate("MainWindow", u"Obligaroria", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Correlativo General", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Clave", None))
        self.cb_actC1.setItemText(0, QCoreApplication.translate("MainWindow", u"Seleccione", None))
        self.cb_actC1.setItemText(1, QCoreApplication.translate("MainWindow", u"Compa\u00f1\u00eda", None))
        self.cb_actC1.setItemText(2, QCoreApplication.translate("MainWindow", u"CB", None))
        self.cb_actC1.setItemText(3, QCoreApplication.translate("MainWindow", u"10-0", None))
        self.cb_actC1.setItemText(4, QCoreApplication.translate("MainWindow", u"10-1", None))
        self.cb_actC1.setItemText(5, QCoreApplication.translate("MainWindow", u"10-2", None))
        self.cb_actC1.setItemText(6, QCoreApplication.translate("MainWindow", u"10-3", None))
        self.cb_actC1.setItemText(7, QCoreApplication.translate("MainWindow", u"10-4", None))
        self.cb_actC1.setItemText(8, QCoreApplication.translate("MainWindow", u"10-5", None))
        self.cb_actC1.setItemText(9, QCoreApplication.translate("MainWindow", u"10-6", None))
        self.cb_actC1.setItemText(10, QCoreApplication.translate("MainWindow", u"10-7", None))
        self.cb_actC1.setItemText(11, QCoreApplication.translate("MainWindow", u"10-8", None))
        self.cb_actC1.setItemText(12, QCoreApplication.translate("MainWindow", u"10-9", None))
        self.cb_actC1.setItemText(13, QCoreApplication.translate("MainWindow", u"10-10", None))
        self.cb_actC1.setItemText(14, QCoreApplication.translate("MainWindow", u"10-11", None))
        self.cb_actC1.setItemText(15, QCoreApplication.translate("MainWindow", u"10-12", None))
        self.cb_actC1.setItemText(16, QCoreApplication.translate("MainWindow", u"10-13", None))
        self.cb_actC1.setItemText(17, QCoreApplication.translate("MainWindow", u"10-14", None))
        self.cb_actC1.setItemText(18, QCoreApplication.translate("MainWindow", u"10-15", None))
        self.cb_actC1.setItemText(19, QCoreApplication.translate("MainWindow", u"10-16", None))
        self.cb_actC1.setItemText(20, QCoreApplication.translate("MainWindow", u"10-17", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Sub-Clasificaci\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        ___qtablewidgetitem = self.liVols.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Registro General", None));
        ___qtablewidgetitem1 = self.liVols.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Total de Voluntarios:", None))
        self.lblTotalLista.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Registro Voluntario", None))
        self.btnAddVol.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.btnDelVol.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Carros Asistentes", None))
        self.cbInsertB9.setText(QCoreApplication.translate("MainWindow", u"B-9", None))
        self.cbInsertUT9.setText(QCoreApplication.translate("MainWindow", u"UT-9", None))
        self.cbInsertM9.setText(QCoreApplication.translate("MainWindow", u"M-9", None))
        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Buscar Acto de Servicio", None))
        ___qtablewidgetitem2 = self.liListsView.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Correlativo Cia", None));
        ___qtablewidgetitem3 = self.liListsView.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem4 = self.liListsView.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Acto", None));
        ___qtablewidgetitem5 = self.liListsView.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Correlativo General", None))
        self.cbEfectivaEdit.setText(QCoreApplication.translate("MainWindow", u"Obligatorio", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Fecha", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Clave", None))
        self.cb_catAct.setItemText(0, QCoreApplication.translate("MainWindow", u"-", None))
        self.cb_catAct.setItemText(1, QCoreApplication.translate("MainWindow", u"Compa\u00f1\u00eda", None))
        self.cb_catAct.setItemText(2, QCoreApplication.translate("MainWindow", u"CB", None))
        self.cb_catAct.setItemText(3, QCoreApplication.translate("MainWindow", u"10-0", None))
        self.cb_catAct.setItemText(4, QCoreApplication.translate("MainWindow", u"10-1", None))
        self.cb_catAct.setItemText(5, QCoreApplication.translate("MainWindow", u"10-2", None))
        self.cb_catAct.setItemText(6, QCoreApplication.translate("MainWindow", u"10-3", None))
        self.cb_catAct.setItemText(7, QCoreApplication.translate("MainWindow", u"10-4", None))
        self.cb_catAct.setItemText(8, QCoreApplication.translate("MainWindow", u"10-5", None))
        self.cb_catAct.setItemText(9, QCoreApplication.translate("MainWindow", u"10-6", None))
        self.cb_catAct.setItemText(10, QCoreApplication.translate("MainWindow", u"10-7", None))
        self.cb_catAct.setItemText(11, QCoreApplication.translate("MainWindow", u"10-8", None))
        self.cb_catAct.setItemText(12, QCoreApplication.translate("MainWindow", u"10-9", None))
        self.cb_catAct.setItemText(13, QCoreApplication.translate("MainWindow", u"10-10", None))
        self.cb_catAct.setItemText(14, QCoreApplication.translate("MainWindow", u"10-11", None))
        self.cb_catAct.setItemText(15, QCoreApplication.translate("MainWindow", u"10-12", None))
        self.cb_catAct.setItemText(16, QCoreApplication.translate("MainWindow", u"10-13", None))
        self.cb_catAct.setItemText(17, QCoreApplication.translate("MainWindow", u"10-14", None))
        self.cb_catAct.setItemText(18, QCoreApplication.translate("MainWindow", u"10-15", None))
        self.cb_catAct.setItemText(19, QCoreApplication.translate("MainWindow", u"10-16", None))
        self.cb_catAct.setItemText(20, QCoreApplication.translate("MainWindow", u"10-17", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Sub-Clasificaci\u00f3n", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Total de Voluntarios:", None))
        self.lbl_cVolsEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Voluntario", None))
        self.btnAddVol_2.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        self.btnDelVol_2.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        ___qtablewidgetitem6 = self.liVolsEdit.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Registro General", None));
        ___qtablewidgetitem7 = self.liVolsEdit.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Carros Asistentes", None))
        self.cbEditB9.setText(QCoreApplication.translate("MainWindow", u"B-9", None))
        self.cbEditUT9.setText(QCoreApplication.translate("MainWindow", u"UT-9", None))
        self.cbEditM9.setText(QCoreApplication.translate("MainWindow", u"M-9", None))
        self.btnSaveEdit.setText(QCoreApplication.translate("MainWindow", u"Guardar Lista", None))
        self.btnDeleteEdit.setText(QCoreApplication.translate("MainWindow", u"Eliminar Lista", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Resumen Mensual", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Preferencias", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Mes", None))
        self.cbMesInforme.setItemText(0, QCoreApplication.translate("MainWindow", u"Enero", None))
        self.cbMesInforme.setItemText(1, QCoreApplication.translate("MainWindow", u"Febrero", None))
        self.cbMesInforme.setItemText(2, QCoreApplication.translate("MainWindow", u"Marzo", None))
        self.cbMesInforme.setItemText(3, QCoreApplication.translate("MainWindow", u"Abril", None))
        self.cbMesInforme.setItemText(4, QCoreApplication.translate("MainWindow", u"Mayo", None))
        self.cbMesInforme.setItemText(5, QCoreApplication.translate("MainWindow", u"Junio", None))
        self.cbMesInforme.setItemText(6, QCoreApplication.translate("MainWindow", u"Julio", None))
        self.cbMesInforme.setItemText(7, QCoreApplication.translate("MainWindow", u"Agosto", None))
        self.cbMesInforme.setItemText(8, QCoreApplication.translate("MainWindow", u"Septiembre", None))
        self.cbMesInforme.setItemText(9, QCoreApplication.translate("MainWindow", u"Octubre", None))
        self.cbMesInforme.setItemText(10, QCoreApplication.translate("MainWindow", u"Noviembre", None))
        self.cbMesInforme.setItemText(11, QCoreApplication.translate("MainWindow", u"Diciembre", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None))
        self.btnResMen.setText(QCoreApplication.translate("MainWindow", u"Extraer Informe", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Informes Personalizados", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Periodo Especifico", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Fecha Desde", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Fecha Hasta", None))
        self.btnGenResEsp.setText(QCoreApplication.translate("MainWindow", u"Generar", None))
        self.btnInfo90Dias.setText(QCoreApplication.translate("MainWindow", u"Informe de 90 D\u00edas", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Por Voluntario", None))
        self.btnGetInfoP.setText(QCoreApplication.translate("MainWindow", u"Generar", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Reg. Greneral", None))
        ___qtablewidgetitem8 = self.tblAdminVols.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Registro", None));
        ___qtablewidgetitem9 = self.tblAdminVols.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Registro General", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Registro Compa\u00f1\u00eda", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Apellido Paterno", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Apellido Materno", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Rut", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Fecha de Ingreso", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Sub-Estado", None))
        self.cbSubEstado.setItemText(0, QCoreApplication.translate("MainWindow", u"ACTIVO", None))
        self.cbSubEstado.setItemText(1, QCoreApplication.translate("MainWindow", u"SUSPENDIDO", None))
        self.cbSubEstado.setItemText(2, QCoreApplication.translate("MainWindow", u"RENUNCIADO", None))
        self.cbSubEstado.setItemText(3, QCoreApplication.translate("MainWindow", u"SEPARADO", None))
        self.cbSubEstado.setItemText(4, QCoreApplication.translate("MainWindow", u"EXPULSADO", None))

        self.btnEditVol.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btnAddVol_3.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.btn_clflds.setText(QCoreApplication.translate("MainWindow", u"Limpiar Campos", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        ___qtablewidgetitem10 = self.tblLicencias.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Correlativo", None));
        ___qtablewidgetitem11 = self.tblLicencias.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem12 = self.tblLicencias.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Fecha Desde", None));
        ___qtablewidgetitem13 = self.tblLicencias.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Fecha Hasta", None));
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Correlativo", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de Registro", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Fecha Desde", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Fecha Hasta", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Motivo", None))
        self.txtMotivoLic.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto Medium'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Inter'; font-size:12px; font-weight:700;\"><br /></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"V.B Capit\u00e1n", None))
        self.cbVBCapitan.setText(QCoreApplication.translate("MainWindow", u"Aprobado", None))
        self.btnSaveLic.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.btnUpdateLic.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnClLic.setText(QCoreApplication.translate("MainWindow", u"Limpiar Campos", None))
    # retranslateUi

