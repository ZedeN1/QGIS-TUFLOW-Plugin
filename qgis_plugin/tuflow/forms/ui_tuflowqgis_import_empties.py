# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tuflowqgis_import_empties.ui'
#
# Created: Mon Oct 28 08:41:38 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_tuflowqgis_import_empty(object):
    def setupUi(self, tuflowqgis_import_empty):
        tuflowqgis_import_empty.setObjectName(_fromUtf8("tuflowqgis_import_empty"))
        tuflowqgis_import_empty.setWindowModality(QtCore.Qt.ApplicationModal)
        tuflowqgis_import_empty.setEnabled(True)
        tuflowqgis_import_empty.resize(388, 518)
        tuflowqgis_import_empty.setMouseTracking(False)
        self.buttonBox = QtGui.QDialogButtonBox(tuflowqgis_import_empty)
        self.buttonBox.setGeometry(QtCore.QRect(110, 480, 160, 26))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label1 = QtGui.QLabel(tuflowqgis_import_empty)
        self.label1.setGeometry(QtCore.QRect(10, 10, 108, 22))
        self.label1.setObjectName(_fromUtf8("label1"))
        self.emptydir = QtGui.QLineEdit(tuflowqgis_import_empty)
        self.emptydir.setGeometry(QtCore.QRect(10, 30, 261, 21))
        self.emptydir.setReadOnly(False)
        self.emptydir.setObjectName(_fromUtf8("emptydir"))
        self.browsedir = QtGui.QPushButton(tuflowqgis_import_empty)
        self.browsedir.setGeometry(QtCore.QRect(281, 27, 79, 26))
        self.browsedir.setObjectName(_fromUtf8("browsedir"))
        self.label2 = QtGui.QLabel(tuflowqgis_import_empty)
        self.label2.setGeometry(QtCore.QRect(10, 60, 108, 22))
        self.label2.setObjectName(_fromUtf8("label2"))
        self.emptyType = QtGui.QListWidget(tuflowqgis_import_empty)
        self.emptyType.setGeometry(QtCore.QRect(10, 80, 331, 311))
        self.emptyType.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.emptyType.setObjectName(_fromUtf8("emptyType"))
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        item = QtGui.QListWidgetItem()
        self.emptyType.addItem(item)
        self.checkPoint = QtGui.QCheckBox(tuflowqgis_import_empty)
        self.checkPoint.setGeometry(QtCore.QRect(20, 455, 70, 17))
        self.checkPoint.setObjectName(_fromUtf8("checkPoint"))
        self.checkLine = QtGui.QCheckBox(tuflowqgis_import_empty)
        self.checkLine.setGeometry(QtCore.QRect(150, 455, 70, 17))
        self.checkLine.setObjectName(_fromUtf8("checkLine"))
        self.checkRegion = QtGui.QCheckBox(tuflowqgis_import_empty)
        self.checkRegion.setGeometry(QtCore.QRect(270, 455, 70, 17))
        self.checkRegion.setObjectName(_fromUtf8("checkRegion"))
        self.label4 = QtGui.QLabel(tuflowqgis_import_empty)
        self.label4.setGeometry(QtCore.QRect(16, 436, 108, 22))
        self.label4.setObjectName(_fromUtf8("label4"))
        self.txtRunID = QtGui.QLineEdit(tuflowqgis_import_empty)
        self.txtRunID.setGeometry(QtCore.QRect(10, 412, 261, 21))
        self.txtRunID.setReadOnly(False)
        self.txtRunID.setObjectName(_fromUtf8("txtRunID"))
        self.label3 = QtGui.QLabel(tuflowqgis_import_empty)
        self.label3.setGeometry(QtCore.QRect(12, 394, 108, 22))
        self.label3.setObjectName(_fromUtf8("label3"))

        self.retranslateUi(tuflowqgis_import_empty)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), tuflowqgis_import_empty.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), tuflowqgis_import_empty.reject)
        QtCore.QMetaObject.connectSlotsByName(tuflowqgis_import_empty)

    def retranslateUi(self, tuflowqgis_import_empty):
        tuflowqgis_import_empty.setWindowTitle(_translate("tuflowqgis_import_empty", "Import TUFLOW Empty File", None))
        self.label1.setText(_translate("tuflowqgis_import_empty", "Empty Directory", None))
        self.emptydir.setText(_translate("tuflowqgis_import_empty", "<directory>", None))
        self.browsedir.setText(_translate("tuflowqgis_import_empty", "Browse...", None))
        self.label2.setText(_translate("tuflowqgis_import_empty", "Empty Type", None))
        __sortingEnabled = self.emptyType.isSortingEnabled()
        self.emptyType.setSortingEnabled(False)
        item = self.emptyType.item(0)
        item.setText(_translate("tuflowqgis_import_empty", "1d_bc", None))
        item = self.emptyType.item(1)
        item.setText(_translate("tuflowqgis_import_empty", "1d_iwl", None))
        item = self.emptyType.item(2)
        item.setText(_translate("tuflowqgis_import_empty", "1d_mh", None))
        item = self.emptyType.item(3)
        item.setText(_translate("tuflowqgis_import_empty", "1d_nd", None))
        item = self.emptyType.item(4)
        item.setText(_translate("tuflowqgis_import_empty", "1d_nwk", None))
        item = self.emptyType.item(5)
        item.setText(_translate("tuflowqgis_import_empty", "1d_tab", None))
        item = self.emptyType.item(6)
        item.setText(_translate("tuflowqgis_import_empty", "1d_WLL", None))
        item = self.emptyType.item(7)
        item.setText(_translate("tuflowqgis_import_empty", "2d_bc", None))
        item = self.emptyType.item(8)
        item.setText(_translate("tuflowqgis_import_empty", "2d_code", None))
        item = self.emptyType.item(9)
        item.setText(_translate("tuflowqgis_import_empty", "2d_fcsh", None))
        item = self.emptyType.item(10)
        item.setText(_translate("tuflowqgis_import_empty", "2d_lfcsh", None))
        item = self.emptyType.item(11)
        item.setText(_translate("tuflowqgis_import_empty", "2d_loc", None))
        item = self.emptyType.item(12)
        item.setText(_translate("tuflowqgis_import_empty", "2d_mat", None))
        item = self.emptyType.item(13)
        item.setText(_translate("tuflowqgis_import_empty", "2d_po", None))
        item = self.emptyType.item(14)
        item.setText(_translate("tuflowqgis_import_empty", "2d_rf", None))
        item = self.emptyType.item(15)
        item.setText(_translate("tuflowqgis_import_empty", "2d_sa", None))
        item = self.emptyType.item(16)
        item.setText(_translate("tuflowqgis_import_empty", "2d_vzsh", None))
        item = self.emptyType.item(17)
        item.setText(_translate("tuflowqgis_import_empty", "2d_zsh", None))
        self.emptyType.setSortingEnabled(__sortingEnabled)
        self.checkPoint.setText(_translate("tuflowqgis_import_empty", "Points", None))
        self.checkLine.setText(_translate("tuflowqgis_import_empty", "Lines", None))
        self.checkRegion.setText(_translate("tuflowqgis_import_empty", "Regions", None))
        self.label4.setText(_translate("tuflowqgis_import_empty", "Geometry Type", None))
        self.txtRunID.setText(_translate("tuflowqgis_import_empty", "RunID", None))
        self.label3.setText(_translate("tuflowqgis_import_empty", "Run ID", None))

