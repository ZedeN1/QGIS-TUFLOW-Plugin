# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\esymons\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\tuflow\forms\ui_tuflowqgis_import_empties.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tuflowqgis_import_empty(object):
    def setupUi(self, tuflowqgis_import_empty):
        tuflowqgis_import_empty.setObjectName("tuflowqgis_import_empty")
        tuflowqgis_import_empty.resize(604, 619)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(tuflowqgis_import_empty)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(tuflowqgis_import_empty)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label1.setObjectName("label1")
        self.horizontalLayout_17.addWidget(self.label1)
        self.pbHideToolTip = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pbHideToolTip.setObjectName("pbHideToolTip")
        self.horizontalLayout_17.addWidget(self.pbHideToolTip)
        self.pbShowToolTip = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pbShowToolTip.setObjectName("pbShowToolTip")
        self.horizontalLayout_17.addWidget(self.pbShowToolTip)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.emptydir = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.emptydir.setMinimumSize(QtCore.QSize(250, 0))
        self.emptydir.setReadOnly(False)
        self.emptydir.setObjectName("emptydir")
        self.horizontalLayout.addWidget(self.emptydir)
        self.browsedir = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.browsedir.setObjectName("browsedir")
        self.horizontalLayout.addWidget(self.browsedir)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(0, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pbSaveToProject = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pbSaveToProject.setObjectName("pbSaveToProject")
        self.horizontalLayout_2.addWidget(self.pbSaveToProject)
        self.pbSaveToGlobal = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pbSaveToGlobal.setObjectName("pbSaveToGlobal")
        self.horizontalLayout_2.addWidget(self.pbSaveToGlobal)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(0, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label2.setObjectName("label2")
        self.horizontalLayout_3.addWidget(self.label2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.emptyType = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.emptyType.setMinimumSize(QtCore.QSize(0, 250))
        self.emptyType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.emptyType.setBaseSize(QtCore.QSize(0, 0))
        self.emptyType.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.emptyType.setObjectName("emptyType")
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.emptyType.addItem(item)
        self.horizontalLayout_4.addWidget(self.emptyType)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label3.setObjectName("label3")
        self.horizontalLayout_6.addWidget(self.label3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.txtRunID = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txtRunID.setReadOnly(False)
        self.txtRunID.setObjectName("txtRunID")
        self.horizontalLayout_5.addWidget(self.txtRunID)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkPoint = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkPoint.setObjectName("checkPoint")
        self.horizontalLayout_8.addWidget(self.checkPoint)
        self.checkLine = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkLine.setObjectName("checkLine")
        self.horizontalLayout_8.addWidget(self.checkLine)
        self.checkRegion = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkRegion.setObjectName("checkRegion")
        self.horizontalLayout_8.addWidget(self.checkRegion)
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.gbSpatialDatabaseOptions = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.gbSpatialDatabaseOptions.setObjectName("gbSpatialDatabaseOptions")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.gbSpatialDatabaseOptions)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cbConvertToDb = QtWidgets.QCheckBox(self.gbSpatialDatabaseOptions)
        self.cbConvertToDb.setObjectName("cbConvertToDb")
        self.verticalLayout_4.addWidget(self.cbConvertToDb)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.rbDatabaseSeparate = QtWidgets.QRadioButton(self.gbSpatialDatabaseOptions)
        self.rbDatabaseSeparate.setChecked(True)
        self.rbDatabaseSeparate.setObjectName("rbDatabaseSeparate")
        self.buttonGroup = QtWidgets.QButtonGroup(tuflowqgis_import_empty)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rbDatabaseSeparate)
        self.horizontalLayout_10.addWidget(self.rbDatabaseSeparate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.rbDatabaseGrouped = QtWidgets.QRadioButton(self.gbSpatialDatabaseOptions)
        self.rbDatabaseGrouped.setObjectName("rbDatabaseGrouped")
        self.buttonGroup.addButton(self.rbDatabaseGrouped)
        self.horizontalLayout_19.addWidget(self.rbDatabaseGrouped)
        self.verticalLayout_2.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.rbDatabaseOne = QtWidgets.QRadioButton(self.gbSpatialDatabaseOptions)
        self.rbDatabaseOne.setObjectName("rbDatabaseOne")
        self.buttonGroup.addButton(self.rbDatabaseOne)
        self.horizontalLayout_20.addWidget(self.rbDatabaseOne)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.btnDatabaseBrowse = QtWidgets.QToolButton(self.gbSpatialDatabaseOptions)
        self.btnDatabaseBrowse.setObjectName("btnDatabaseBrowse")
        self.horizontalLayout_21.addWidget(self.btnDatabaseBrowse)
        self.leDatabaseBrowse = QtWidgets.QLineEdit(self.gbSpatialDatabaseOptions)
        self.leDatabaseBrowse.setObjectName("leDatabaseBrowse")
        self.horizontalLayout_21.addWidget(self.leDatabaseBrowse)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_21)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_9.addWidget(self.gbSpatialDatabaseOptions)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem4 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.pbOk = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pbOk.setObjectName("pbOk")
        self.horizontalLayout_12.addWidget(self.pbOk)
        self.pbCancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_12.addWidget(self.pbCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_2)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.teToolTip = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.teToolTip.setOpenExternalLinks(True)
        self.teToolTip.setObjectName("teToolTip")
        self.horizontalLayout_13.addWidget(self.teToolTip)
        self.verticalLayout_3.addWidget(self.splitter)

        self.retranslateUi(tuflowqgis_import_empty)
        QtCore.QMetaObject.connectSlotsByName(tuflowqgis_import_empty)

    def retranslateUi(self, tuflowqgis_import_empty):
        _translate = QtCore.QCoreApplication.translate
        tuflowqgis_import_empty.setWindowTitle(_translate("tuflowqgis_import_empty", "Dialog"))
        self.label1.setText(_translate("tuflowqgis_import_empty", "Empty Directory"))
        self.pbHideToolTip.setText(_translate("tuflowqgis_import_empty", "<< Hide Tool Tip"))
        self.pbShowToolTip.setText(_translate("tuflowqgis_import_empty", "Show Tool Tip >>"))
        self.emptydir.setText(_translate("tuflowqgis_import_empty", "<directory>"))
        self.browsedir.setText(_translate("tuflowqgis_import_empty", "Browse..."))
        self.pbSaveToProject.setText(_translate("tuflowqgis_import_empty", "Save directory to Project"))
        self.pbSaveToGlobal.setText(_translate("tuflowqgis_import_empty", "Save directory to Global"))
        self.label2.setText(_translate("tuflowqgis_import_empty", "Empty Type"))
        __sortingEnabled = self.emptyType.isSortingEnabled()
        self.emptyType.setSortingEnabled(False)
        item = self.emptyType.item(0)
        item.setText(_translate("tuflowqgis_import_empty", "0d_RL"))
        item = self.emptyType.item(1)
        item.setText(_translate("tuflowqgis_import_empty", "1d_bc"))
        item = self.emptyType.item(2)
        item.setText(_translate("tuflowqgis_import_empty", "1d_iwl"))
        item = self.emptyType.item(3)
        item.setText(_translate("tuflowqgis_import_empty", "1d_mh"))
        item = self.emptyType.item(4)
        item.setText(_translate("tuflowqgis_import_empty", "1d_nd"))
        item = self.emptyType.item(5)
        item.setText(_translate("tuflowqgis_import_empty", "1d_nwk"))
        item = self.emptyType.item(6)
        item.setText(_translate("tuflowqgis_import_empty", "1d_nwkB"))
        item = self.emptyType.item(7)
        item.setText(_translate("tuflowqgis_import_empty", "1d_nwke"))
        item = self.emptyType.item(8)
        item.setText(_translate("tuflowqgis_import_empty", "1d_pit"))
        item = self.emptyType.item(9)
        item.setText(_translate("tuflowqgis_import_empty", "1d_tab"))
        item = self.emptyType.item(10)
        item.setText(_translate("tuflowqgis_import_empty", "1d_WLL"))
        item = self.emptyType.item(11)
        item.setText(_translate("tuflowqgis_import_empty", "2d_bc"))
        item = self.emptyType.item(12)
        item.setText(_translate("tuflowqgis_import_empty", "2d_code"))
        item = self.emptyType.item(13)
        item.setText(_translate("tuflowqgis_import_empty", "2d_fc"))
        item = self.emptyType.item(14)
        item.setText(_translate("tuflowqgis_import_empty", "2d_fcsh"))
        item = self.emptyType.item(15)
        item.setText(_translate("tuflowqgis_import_empty", "2d_glo"))
        item = self.emptyType.item(16)
        item.setText(_translate("tuflowqgis_import_empty", "2d_gw"))
        item = self.emptyType.item(17)
        item.setText(_translate("tuflowqgis_import_empty", "2d_iwl"))
        item = self.emptyType.item(18)
        item.setText(_translate("tuflowqgis_import_empty", "2d_lfcsh"))
        item = self.emptyType.item(19)
        item.setText(_translate("tuflowqgis_import_empty", "2d_loc"))
        item = self.emptyType.item(20)
        item.setText(_translate("tuflowqgis_import_empty", "2d_lp"))
        item = self.emptyType.item(21)
        item.setText(_translate("tuflowqgis_import_empty", "2d_mat"))
        item = self.emptyType.item(22)
        item.setText(_translate("tuflowqgis_import_empty", "2d_oz"))
        item = self.emptyType.item(23)
        item.setText(_translate("tuflowqgis_import_empty", "2d_po"))
        item = self.emptyType.item(24)
        item.setText(_translate("tuflowqgis_import_empty", "2d_rf"))
        item = self.emptyType.item(25)
        item.setText(_translate("tuflowqgis_import_empty", "2d_sa"))
        item = self.emptyType.item(26)
        item.setText(_translate("tuflowqgis_import_empty", "2d_sa_rf"))
        item = self.emptyType.item(27)
        item.setText(_translate("tuflowqgis_import_empty", "2d_sa_tr"))
        item = self.emptyType.item(28)
        item.setText(_translate("tuflowqgis_import_empty", "2d_soil"))
        item = self.emptyType.item(29)
        item.setText(_translate("tuflowqgis_import_empty", "2d_vzsh"))
        item = self.emptyType.item(30)
        item.setText(_translate("tuflowqgis_import_empty", "2d_z__"))
        item = self.emptyType.item(31)
        item.setText(_translate("tuflowqgis_import_empty", "2d_zsh"))
        item = self.emptyType.item(32)
        item.setText(_translate("tuflowqgis_import_empty", "2d_zshr"))
        self.emptyType.setSortingEnabled(__sortingEnabled)
        self.label3.setText(_translate("tuflowqgis_import_empty", "Run ID"))
        self.txtRunID.setText(_translate("tuflowqgis_import_empty", "RunID"))
        self.groupBox_2.setTitle(_translate("tuflowqgis_import_empty", "Geometry Type"))
        self.checkPoint.setText(_translate("tuflowqgis_import_empty", "Points"))
        self.checkLine.setText(_translate("tuflowqgis_import_empty", "Lines"))
        self.checkRegion.setText(_translate("tuflowqgis_import_empty", "Regions"))
        self.gbSpatialDatabaseOptions.setTitle(_translate("tuflowqgis_import_empty", "Spatial Database Options:"))
        self.cbConvertToDb.setText(_translate("tuflowqgis_import_empty", "Check if empty files are shp and whish to convert to gpkg"))
        self.rbDatabaseSeparate.setText(_translate("tuflowqgis_import_empty", "Separate"))
        self.rbDatabaseGrouped.setText(_translate("tuflowqgis_import_empty", "Group geometry types"))
        self.rbDatabaseOne.setText(_translate("tuflowqgis_import_empty", "All to one:"))
        self.btnDatabaseBrowse.setText(_translate("tuflowqgis_import_empty", "..."))
        self.leDatabaseBrowse.setText(_translate("tuflowqgis_import_empty", "<Existing or New Database>"))
        self.pbOk.setText(_translate("tuflowqgis_import_empty", "OK"))
        self.pbCancel.setText(_translate("tuflowqgis_import_empty", "Cancel"))
        self.teToolTip.setHtml(_translate("tuflowqgis_import_empty", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Tool Tip</span></p></body></html>"))
