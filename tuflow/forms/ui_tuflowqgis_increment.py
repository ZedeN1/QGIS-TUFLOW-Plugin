# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\esymons\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\tuflow\forms\ui_tuflowqgis_increment.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tuflowqgis_increment(object):
    def setupUi(self, tuflowqgis_increment):
        tuflowqgis_increment.setObjectName("tuflowqgis_increment")
        tuflowqgis_increment.resize(438, 519)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(tuflowqgis_increment)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(tuflowqgis_increment)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.sourcelayer = QtWidgets.QComboBox(tuflowqgis_increment)
        self.sourcelayer.setObjectName("sourcelayer")
        self.verticalLayout.addWidget(self.sourcelayer)
        self.label_2 = QtWidgets.QLabel(tuflowqgis_increment)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.outfolder = QtWidgets.QLineEdit(tuflowqgis_increment)
        self.outfolder.setReadOnly(False)
        self.outfolder.setObjectName("outfolder")
        self.horizontalLayout_6.addWidget(self.outfolder)
        self.btnBrowseDatabase = QtWidgets.QPushButton(tuflowqgis_increment)
        self.btnBrowseDatabase.setObjectName("btnBrowseDatabase")
        self.horizontalLayout_6.addWidget(self.btnBrowseDatabase)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.label = QtWidgets.QLabel(tuflowqgis_increment)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.outfilename = QtWidgets.QLineEdit(tuflowqgis_increment)
        self.outfilename.setReadOnly(False)
        self.outfilename.setObjectName("outfilename")
        self.gridLayout.addWidget(self.outfilename, 0, 0, 1, 1)
        self.browseoutfile = QtWidgets.QPushButton(tuflowqgis_increment)
        self.browseoutfile.setAutoDefault(False)
        self.browseoutfile.setObjectName("browseoutfile")
        self.gridLayout.addWidget(self.browseoutfile, 0, 1, 1, 1)
        self.twTables = QtWidgets.QTableWidget(tuflowqgis_increment)
        self.twTables.setColumnCount(2)
        self.twTables.setObjectName("twTables")
        self.twTables.setRowCount(0)
        self.twTables.horizontalHeader().setVisible(True)
        self.twTables.horizontalHeader().setCascadingSectionResizes(True)
        self.twTables.horizontalHeader().setHighlightSections(True)
        self.twTables.horizontalHeader().setStretchLastSection(True)
        self.twTables.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.twTables, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.cbMoveToSS = QtWidgets.QCheckBox(tuflowqgis_increment)
        self.cbMoveToSS.setObjectName("cbMoveToSS")
        self.verticalLayout.addWidget(self.cbMoveToSS)
        self.rbRemoveSource = QtWidgets.QRadioButton(tuflowqgis_increment)
        self.rbRemoveSource.setChecked(True)
        self.rbRemoveSource.setObjectName("rbRemoveSource")
        self.buttonGroup = QtWidgets.QButtonGroup(tuflowqgis_increment)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rbRemoveSource)
        self.verticalLayout.addWidget(self.rbRemoveSource)
        self.rbKeepSource = QtWidgets.QRadioButton(tuflowqgis_increment)
        self.rbKeepSource.setObjectName("rbKeepSource")
        self.buttonGroup.addButton(self.rbKeepSource)
        self.verticalLayout.addWidget(self.rbKeepSource)
        self.gbSpatialDatabaseOptions = QtWidgets.QGroupBox(tuflowqgis_increment)
        self.gbSpatialDatabaseOptions.setObjectName("gbSpatialDatabaseOptions")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gbSpatialDatabaseOptions)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rbDatabaseLayer = QtWidgets.QRadioButton(self.gbSpatialDatabaseOptions)
        self.rbDatabaseLayer.setChecked(True)
        self.rbDatabaseLayer.setObjectName("rbDatabaseLayer")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(tuflowqgis_increment)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.rbDatabaseLayer)
        self.horizontalLayout_3.addWidget(self.rbDatabaseLayer)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rbDatabaseDbLayer = QtWidgets.QRadioButton(self.gbSpatialDatabaseOptions)
        self.rbDatabaseDbLayer.setChecked(False)
        self.rbDatabaseDbLayer.setObjectName("rbDatabaseDbLayer")
        self.buttonGroup_2.addButton(self.rbDatabaseDbLayer)
        self.horizontalLayout_2.addWidget(self.rbDatabaseDbLayer)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.gbSpatialDatabaseOptions)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pbOk = QtWidgets.QPushButton(tuflowqgis_increment)
        self.pbOk.setObjectName("pbOk")
        self.horizontalLayout.addWidget(self.pbOk)
        self.pbCancel = QtWidgets.QPushButton(tuflowqgis_increment)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout.addWidget(self.pbCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(tuflowqgis_increment)
        QtCore.QMetaObject.connectSlotsByName(tuflowqgis_increment)

    def retranslateUi(self, tuflowqgis_increment):
        _translate = QtCore.QCoreApplication.translate
        tuflowqgis_increment.setWindowTitle(_translate("tuflowqgis_increment", "Increment Selected Layer"))
        self.label_1.setText(_translate("tuflowqgis_increment", "Source Layer"))
        self.label_2.setText(_translate("tuflowqgis_increment", "Output Folder"))
        self.outfolder.setText(_translate("tuflowqgis_increment", "<outfolder>"))
        self.btnBrowseDatabase.setText(_translate("tuflowqgis_increment", "Browse..."))
        self.label.setText(_translate("tuflowqgis_increment", "Output File"))
        self.outfilename.setText(_translate("tuflowqgis_increment", "<filename.shp>"))
        self.browseoutfile.setText(_translate("tuflowqgis_increment", "Browse..."))
        self.cbMoveToSS.setText(_translate("tuflowqgis_increment", "Move Source Layer to Superseded (SS) folder"))
        self.rbRemoveSource.setText(_translate("tuflowqgis_increment", "Remove Source Layer from Workspace"))
        self.rbKeepSource.setText(_translate("tuflowqgis_increment", "Keep Source Layer in Workspace"))
        self.gbSpatialDatabaseOptions.setTitle(_translate("tuflowqgis_increment", "Spatial Database Options"))
        self.rbDatabaseLayer.setText(_translate("tuflowqgis_increment", "Increment layer only"))
        self.rbDatabaseDbLayer.setText(_translate("tuflowqgis_increment", "Increment layer and preserve database"))
        self.pbOk.setText(_translate("tuflowqgis_increment", "OK"))
        self.pbCancel.setText(_translate("tuflowqgis_increment", "Cancel"))

