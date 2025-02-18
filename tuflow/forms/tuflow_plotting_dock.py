# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\esymons\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\tuflow\forms\tuflow_plotting_dock.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tuplot(object):
    def setupUi(self, Tuplot):
        Tuplot.setObjectName("Tuplot")
        Tuplot.resize(1067, 619)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_9.setContentsMargins(0, 0, 9, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.splitter_3 = QtWidgets.QSplitter(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_3.sizePolicy().hasHeightForWidth())
        self.splitter_3.setSizePolicy(sizePolicy)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.PlotLayout = QtWidgets.QWidget(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlotLayout.sizePolicy().hasHeightForWidth())
        self.PlotLayout.setSizePolicy(sizePolicy)
        self.PlotLayout.setObjectName("PlotLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.PlotLayout)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wTopBar = QtWidgets.QWidget(self.PlotLayout)
        self.wTopBar.setObjectName("wTopBar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.wTopBar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mainMenu_2 = QtWidgets.QWidget(self.wTopBar)
        self.mainMenu_2.setObjectName("mainMenu_2")
        self.mainMenu = QtWidgets.QVBoxLayout(self.mainMenu_2)
        self.mainMenu.setContentsMargins(0, 0, 0, 0)
        self.mainMenu.setSpacing(0)
        self.mainMenu.setObjectName("mainMenu")
        self.horizontalLayout_2.addWidget(self.mainMenu_2)
        self.label_4 = QtWidgets.QLabel(self.wTopBar)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/logo/resources/TUFLOW_logo_resized.png"))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.pbHidePlotWindow = QtWidgets.QPushButton(self.wTopBar)
        self.pbHidePlotWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pbHidePlotWindow.setObjectName("pbHidePlotWindow")
        self.horizontalLayout_2.addWidget(self.pbHidePlotWindow)
        self.verticalLayout_2.addWidget(self.wTopBar)
        self.tabWidget = QtWidgets.QTabWidget(self.PlotLayout)
        self.tabWidget.setObjectName("tabWidget")
        self.TimeSeriesTab = QtWidgets.QWidget()
        self.TimeSeriesTab.setObjectName("TimeSeriesTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.TimeSeriesTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.TimeSeriesLayout = QtWidgets.QGridLayout()
        self.TimeSeriesLayout.setObjectName("TimeSeriesLayout")
        self.TimeSeriesFrame = QtWidgets.QFrame(self.TimeSeriesTab)
        self.TimeSeriesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TimeSeriesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TimeSeriesFrame.setObjectName("TimeSeriesFrame")
        self.TimeSeriesLayout.addWidget(self.TimeSeriesFrame, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.TimeSeriesLayout, 0, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 10)
        self.gridLayout_3.setRowStretch(0, 10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/results.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.TimeSeriesTab, icon, "")
        self.LongPlotTab = QtWidgets.QWidget()
        self.LongPlotTab.setObjectName("LongPlotTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.LongPlotTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.LongPlotLayout = QtWidgets.QGridLayout()
        self.LongPlotLayout.setObjectName("LongPlotLayout")
        self.LongPlotFrame = QtWidgets.QFrame(self.LongPlotTab)
        self.LongPlotFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LongPlotFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LongPlotFrame.setObjectName("LongPlotFrame")
        self.LongPlotLayout.addWidget(self.LongPlotFrame, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.LongPlotLayout, 0, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/cross_section.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.LongPlotTab, icon1, "")
        self.CrossSectionTab = QtWidgets.QWidget()
        self.CrossSectionTab.setObjectName("CrossSectionTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.CrossSectionTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.CrossSectionLayout = QtWidgets.QGridLayout()
        self.CrossSectionLayout.setObjectName("CrossSectionLayout")
        self.CrossSectionFrame = QtWidgets.QFrame(self.CrossSectionTab)
        self.CrossSectionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CrossSectionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CrossSectionFrame.setObjectName("CrossSectionFrame")
        self.CrossSectionLayout.addWidget(self.CrossSectionFrame, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.CrossSectionLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.CrossSectionTab, "")
        self.VerticalProfileTab = QtWidgets.QWidget()
        self.VerticalProfileTab.setObjectName("VerticalProfileTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.VerticalProfileTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.VerticalProfileLayout = QtWidgets.QGridLayout()
        self.VerticalProfileLayout.setObjectName("VerticalProfileLayout")
        self.VerticalProfileFrame = QtWidgets.QFrame(self.VerticalProfileTab)
        self.VerticalProfileFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.VerticalProfileFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.VerticalProfileFrame.setObjectName("VerticalProfileFrame")
        self.VerticalProfileLayout.addWidget(self.VerticalProfileFrame, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.VerticalProfileLayout, 0, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/vertical_profile.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.VerticalProfileTab, icon2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.ResultLayout = QtWidgets.QWidget(self.splitter_3)
        self.ResultLayout.setObjectName("ResultLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.ResultLayout)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.SecondMenu = QtWidgets.QWidget(self.ResultLayout)
        self.SecondMenu.setObjectName("SecondMenu")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.SecondMenu)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pbShowPlotWindow = QtWidgets.QPushButton(self.SecondMenu)
        self.pbShowPlotWindow.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pbShowPlotWindow.setObjectName("pbShowPlotWindow")
        self.horizontalLayout_3.addWidget(self.pbShowPlotWindow)
        self.mainMenuSecond_2 = QtWidgets.QWidget(self.SecondMenu)
        self.mainMenuSecond_2.setObjectName("mainMenuSecond_2")
        self.mainMenuSecond = QtWidgets.QVBoxLayout(self.mainMenuSecond_2)
        self.mainMenuSecond.setContentsMargins(0, 0, 0, 0)
        self.mainMenuSecond.setSpacing(0)
        self.mainMenuSecond.setObjectName("mainMenuSecond")
        self.horizontalLayout_3.addWidget(self.mainMenuSecond_2)
        self.label_5 = QtWidgets.QLabel(self.SecondMenu)
        self.label_5.setMinimumSize(QtCore.QSize(0, 20))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/logo/resources/TUFLOW_logo_resized.png"))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout_6.addWidget(self.SecondMenu)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.splitter_4 = QtWidgets.QSplitter(self.ResultLayout)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.widget = QtWidgets.QWidget(self.splitter_4)
        self.widget.setObjectName("widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.splitter_2 = QtWidgets.QSplitter(self.widget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.OpenResultsWidget = QtWidgets.QWidget(self.splitter_2)
        self.OpenResultsWidget.setObjectName("OpenResultsWidget")
        self.OpenResultsLayout_2 = QtWidgets.QVBoxLayout(self.OpenResultsWidget)
        self.OpenResultsLayout_2.setContentsMargins(0, 0, 0, 0)
        self.OpenResultsLayout_2.setObjectName("OpenResultsLayout_2")
        self.PlotOptionSplitter = QtWidgets.QSplitter(self.OpenResultsWidget)
        self.PlotOptionSplitter.setOrientation(QtCore.Qt.Vertical)
        self.PlotOptionSplitter.setObjectName("PlotOptionSplitter")
        self.OpenResultsLayout = QtWidgets.QWidget(self.PlotOptionSplitter)
        self.OpenResultsLayout.setObjectName("OpenResultsLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.OpenResultsLayout)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.OpenResultsLayout)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.OpenResults = QtWidgets.QListWidget(self.OpenResultsLayout)
        self.OpenResults.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.OpenResults.setMovement(QtWidgets.QListView.Static)
        self.OpenResults.setResizeMode(QtWidgets.QListView.Fixed)
        self.OpenResults.setObjectName("OpenResults")
        self.verticalLayout_3.addWidget(self.OpenResults)
        self.MapPlottingLayout = QtWidgets.QWidget(self.PlotOptionSplitter)
        self.MapPlottingLayout.setObjectName("MapPlottingLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.MapPlottingLayout)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.MapPlottingLayout)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.cboSelectType = QtWidgets.QComboBox(self.MapPlottingLayout)
        self.cboSelectType.setEditable(True)
        self.cboSelectType.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cboSelectType.setObjectName("cboSelectType")
        self.cboSelectType.addItem("")
        self.cboSelectType.addItem("")
        self.cboSelectType.addItem("")
        self.verticalLayout_5.addWidget(self.cboSelectType)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.MapOutputPlotFrame = QtWidgets.QFrame(self.MapPlottingLayout)
        self.MapOutputPlotFrame.setMinimumSize(QtCore.QSize(300, 0))
        self.MapOutputPlotFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MapOutputPlotFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MapOutputPlotFrame.setObjectName("MapOutputPlotFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.MapOutputPlotFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addWidget(self.MapOutputPlotFrame)
        self.Mesh3DToolbarFrame = QtWidgets.QFrame(self.MapPlottingLayout)
        self.Mesh3DToolbarFrame.setMinimumSize(QtCore.QSize(300, 0))
        self.Mesh3DToolbarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Mesh3DToolbarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Mesh3DToolbarFrame.setObjectName("Mesh3DToolbarFrame")
        self.verticalLayout.addWidget(self.Mesh3DToolbarFrame)
        self.progressBar = QtWidgets.QProgressBar(self.MapPlottingLayout)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.line = QtWidgets.QFrame(self.MapPlottingLayout)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem)
        self.ViewToolbarFrame = QtWidgets.QFrame(self.MapPlottingLayout)
        self.ViewToolbarFrame.setMinimumSize(QtCore.QSize(300, 0))
        self.ViewToolbarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ViewToolbarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ViewToolbarFrame.setObjectName("ViewToolbarFrame")
        self.verticalLayout.addWidget(self.ViewToolbarFrame)
        self.mplToolbarFrame = QtWidgets.QFrame(self.MapPlottingLayout)
        self.mplToolbarFrame.setMinimumSize(QtCore.QSize(300, 0))
        self.mplToolbarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mplToolbarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mplToolbarFrame.setObjectName("mplToolbarFrame")
        self.verticalLayout.addWidget(self.mplToolbarFrame)
        self.plotCoords = QtWidgets.QLabel(self.MapPlottingLayout)
        self.plotCoords.setObjectName("plotCoords")
        self.verticalLayout.addWidget(self.plotCoords)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cbShowCurrentTime = QtWidgets.QCheckBox(self.MapPlottingLayout)
        self.cbShowCurrentTime.setObjectName("cbShowCurrentTime")
        self.horizontalLayout_5.addWidget(self.cbShowCurrentTime)
        self.cbShowAsDates = QtWidgets.QCheckBox(self.MapPlottingLayout)
        self.cbShowAsDates.setObjectName("cbShowAsDates")
        self.horizontalLayout_5.addWidget(self.cbShowAsDates)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.OpenResultsLayout_2.addWidget(self.PlotOptionSplitter)
        self.ResultTypeSplitter = QtWidgets.QSplitter(self.splitter_2)
        self.ResultTypeSplitter.setOrientation(QtCore.Qt.Vertical)
        self.ResultTypeSplitter.setObjectName("ResultTypeSplitter")
        self.ResultTypeLayout = QtWidgets.QWidget(self.ResultTypeSplitter)
        self.ResultTypeLayout.setObjectName("ResultTypeLayout")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.ResultTypeLayout)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.ResultTypeLayout)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_11.addWidget(self.label_6)
        self.OpenResultTypes = DataSetView(self.ResultTypeLayout)
        self.OpenResultTypes.setMinimumSize(QtCore.QSize(150, 55))
        self.OpenResultTypes.setMouseTracking(True)
        self.OpenResultTypes.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.OpenResultTypes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.OpenResultTypes.setObjectName("OpenResultTypes")
        self.verticalLayout_11.addWidget(self.OpenResultTypes)
        self.verticalLayout_7.addWidget(self.splitter_2)
        self.verticalWidget = QtWidgets.QWidget(self.splitter_4)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.sliderTime = TimeSlider(self.verticalWidget)
        self.sliderTime.setMaximum(100)
        self.sliderTime.setPageStep(100)
        self.sliderTime.setOrientation(QtCore.Qt.Horizontal)
        self.sliderTime.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sliderTime.setTickInterval(1)
        self.sliderTime.setObjectName("sliderTime")
        self.verticalLayout_10.addWidget(self.sliderTime)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cboTime = QtWidgets.QComboBox(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboTime.sizePolicy().hasHeightForWidth())
        self.cboTime.setSizePolicy(sizePolicy)
        self.cboTime.setMinimumSize(QtCore.QSize(0, 0))
        self.cboTime.setEditable(True)
        self.cboTime.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cboTime.setObjectName("cboTime")
        self.horizontalLayout_4.addWidget(self.cboTime)
        self.btnFirst = QtWidgets.QToolButton(self.verticalWidget)
        self.btnFirst.setAutoRaise(True)
        self.btnFirst.setObjectName("btnFirst")
        self.horizontalLayout_4.addWidget(self.btnFirst)
        self.btnPrev = QtWidgets.QToolButton(self.verticalWidget)
        self.btnPrev.setAutoRaise(True)
        self.btnPrev.setObjectName("btnPrev")
        self.horizontalLayout_4.addWidget(self.btnPrev)
        self.btnNext = QtWidgets.QToolButton(self.verticalWidget)
        self.btnNext.setAutoRaise(True)
        self.btnNext.setObjectName("btnNext")
        self.horizontalLayout_4.addWidget(self.btnNext)
        self.btnLast = QtWidgets.QToolButton(self.verticalWidget)
        self.btnLast.setAutoRaise(True)
        self.btnLast.setObjectName("btnLast")
        self.horizontalLayout_4.addWidget(self.btnLast)
        self.btnTimePlay = QtWidgets.QToolButton(self.verticalWidget)
        self.btnTimePlay.setCheckable(True)
        self.btnTimePlay.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.btnTimePlay.setAutoRaise(True)
        self.btnTimePlay.setArrowType(QtCore.Qt.NoArrow)
        self.btnTimePlay.setObjectName("btnTimePlay")
        self.horizontalLayout_4.addWidget(self.btnTimePlay)
        self.line_2 = QtWidgets.QFrame(self.verticalWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_4.addWidget(self.line_2)
        self.btn2dLock = QtWidgets.QToolButton(self.verticalWidget)
        self.btn2dLock.setCheckable(False)
        self.btn2dLock.setAutoRaise(True)
        self.btn2dLock.setObjectName("btn2dLock")
        self.horizontalLayout_4.addWidget(self.btn2dLock)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.verticalLayout_8.addWidget(self.splitter_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_8)
        self.verticalLayout_9.addWidget(self.splitter_3)
        Tuplot.setWidget(self.dockWidgetContents)

        self.retranslateUi(Tuplot)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Tuplot)

    def retranslateUi(self, Tuplot):
        _translate = QtCore.QCoreApplication.translate
        Tuplot.setWindowTitle(_translate("Tuplot", "TUFLOW Viewer"))
        self.pbHidePlotWindow.setText(_translate("Tuplot", "Hide Plot Window >>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TimeSeriesTab), _translate("Tuplot", "Time Series"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LongPlotTab), _translate("Tuplot", "Cross Section / Long Profile"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CrossSectionTab), _translate("Tuplot", "1D Cross Section Viewer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.VerticalProfileTab), _translate("Tuplot", "Vertical Profile"))
        self.pbShowPlotWindow.setText(_translate("Tuplot", "<< Plot Window"))
        self.label.setText(_translate("Tuplot", "Open Results"))
        self.label_3.setText(_translate("Tuplot", "Map Output Plotting"))
        self.cboSelectType.setItemText(0, _translate("Tuplot", "From Map"))
        self.cboSelectType.setItemText(1, _translate("Tuplot", "From Map Multi"))
        self.cboSelectType.setItemText(2, _translate("Tuplot", "Layer Selection"))
        self.plotCoords.setText(_translate("Tuplot", "X:  Y:  Z:"))
        self.cbShowCurrentTime.setText(_translate("Tuplot", "Show Current Time"))
        self.cbShowAsDates.setText(_translate("Tuplot", "Show as dates"))
        self.label_6.setText(_translate("Tuplot", "Result Type"))
        self.OpenResultTypes.setToolTip(_translate("Tuplot", "Test"))
        self.btnFirst.setToolTip(_translate("Tuplot", "First Timestep"))
        self.btnFirst.setText(_translate("Tuplot", "|<"))
        self.btnPrev.setToolTip(_translate("Tuplot", "Previous Timestep"))
        self.btnPrev.setText(_translate("Tuplot", "<"))
        self.btnNext.setToolTip(_translate("Tuplot", "Next Timestep"))
        self.btnNext.setText(_translate("Tuplot", ">"))
        self.btnLast.setToolTip(_translate("Tuplot", "Last Timestep"))
        self.btnLast.setText(_translate("Tuplot", ">|"))
        self.btnTimePlay.setToolTip(_translate("Tuplot", "Play Through Timesteps"))
        self.btnTimePlay.setText(_translate("Tuplot", "..."))
        self.btn2dLock.setToolTip(_translate("Tuplot", "Lock Timesteps to Map Outputs"))
        self.btn2dLock.setText(_translate("Tuplot", "..."))
from tuflow.dataset_view import DataSetView
from tuflow.time_slider import TimeSlider
import tuflow.resources.tuflow
