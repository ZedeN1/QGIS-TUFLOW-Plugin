# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\esymons\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\tuflow\forms\FMResImport_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FMResDialog(object):
    def setupUi(self, FMResDialog):
        FMResDialog.setObjectName("FMResDialog")
        FMResDialog.resize(569, 384)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(FMResDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(FMResDialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelGXY = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelGXY.setObjectName("labelGXY")
        self.horizontalLayout_2.addWidget(self.labelGXY)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBrowseGXY = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.btnBrowseGXY.setObjectName("btnBrowseGXY")
        self.horizontalLayout.addWidget(self.btnBrowseGXY)
        self.leGXY = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.leGXY.setObjectName("leGXY")
        self.horizontalLayout.addWidget(self.leGXY)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.labelSectionData = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelSectionData.setObjectName("labelSectionData")
        self.horizontalLayout_7.addWidget(self.labelSectionData)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btnBrowseSectionData = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.btnBrowseSectionData.setObjectName("btnBrowseSectionData")
        self.horizontalLayout_8.addWidget(self.btnBrowseSectionData)
        self.leSectionData = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.leSectionData.setObjectName("leSectionData")
        self.horizontalLayout_8.addWidget(self.leSectionData)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelCSV = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelCSV.setObjectName("labelCSV")
        self.horizontalLayout_4.addWidget(self.labelCSV)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnBrowseCSV = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.btnBrowseCSV.setObjectName("btnBrowseCSV")
        self.horizontalLayout_3.addWidget(self.btnBrowseCSV)
        self.btnRemCSV = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.btnRemCSV.setObjectName("btnRemCSV")
        self.horizontalLayout_3.addWidget(self.btnRemCSV)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lwCSVFiles = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.lwCSVFiles.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lwCSVFiles.setObjectName("lwCSVFiles")
        self.horizontalLayout_5.addWidget(self.lwCSVFiles)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ToolTip = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.ToolTip.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ToolTip.setObjectName("ToolTip")
        self.verticalLayout_2.addWidget(self.ToolTip)
        self.verticalLayout_3.addWidget(self.splitter)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.pbOK = QtWidgets.QPushButton(FMResDialog)
        self.pbOK.setObjectName("pbOK")
        self.horizontalLayout_6.addWidget(self.pbOK)
        self.pbCancel = QtWidgets.QPushButton(FMResDialog)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_6.addWidget(self.pbCancel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.retranslateUi(FMResDialog)
        QtCore.QMetaObject.connectSlotsByName(FMResDialog)

    def retranslateUi(self, FMResDialog):
        _translate = QtCore.QCoreApplication.translate
        FMResDialog.setWindowTitle(_translate("FMResDialog", "Import Flood Modeller Results"))
        self.labelGXY.setText(_translate("FMResDialog", "GXY File"))
        self.btnBrowseGXY.setText(_translate("FMResDialog", "..."))
        self.labelSectionData.setText(_translate("FMResDialog", "Section Data (optional)"))
        self.btnBrowseSectionData.setText(_translate("FMResDialog", "..."))
        self.labelCSV.setText(_translate("FMResDialog", "Result CSV Files"))
        self.btnBrowseCSV.setText(_translate("FMResDialog", "..."))
        self.btnRemCSV.setText(_translate("FMResDialog", "..."))
        self.ToolTip.setHtml(_translate("FMResDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Tool Tip</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Imports Flood Modeller time series results into TUFLOW Viewer. Require </span><span style=\" font-size:10pt; font-weight:600;\">Node/Link</span><span style=\" font-size:10pt;\"> georeferenced input (.gxy) and </span><span style=\" font-size:10pt; font-weight:600;\">result CSV</span><span style=\" font-size:10pt;\"> file exported from Flood Modeller in the format of </span><span style=\" font-size:10pt; font-weight:600;\">column per node.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">It is also recommended to export with header information, however it is not a requirement.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Supported result types:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    - stage</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    - flow</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">    - velocity</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Inputs</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">GXY File</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Select georeferenced node / link data file (.gxy) from Flood Modeller model. This will be imported into QGIS can be used to select which element to view result for.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Section Data</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Optional input (.dat) for cross-section data that will display cross section data in map window and plot window. Users will also be able plot water level results on the cross section data. Input .dat file must contain X, Y coordinate data for input cross-sections. Note only open channel sections will be imported and displayed.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Result CSV Files</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Result data exported from Flood Modeller in \'column per node format\'. Can import result type (stage, flow etc) separately or in the same file. Can also import multiple results (e.g. from different events).</span></p></body></html>"))
        self.pbOK.setText(_translate("FMResDialog", "OK"))
        self.pbCancel.setText(_translate("FMResDialog", "Cancel"))

