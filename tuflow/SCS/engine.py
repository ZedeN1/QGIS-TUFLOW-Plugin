import os, subprocess, re, csv
import numpy as np
from PyQt5.QtCore import QObject, pyqtSignal, QVariant
from PyQt5.QtWidgets import QMessageBox
from qgis.core import QgsVectorFileWriter, QgsFields, QgsField, QgsWkbTypes, QgsFeature, NULL


class SCS(QObject):
    """ Class for obtaining SCS data and processing into TUFLOW.
        Inherits from QObject so signals and QThread can be used.
    """

    # static values that don't need to be initialised
    auckland = 'auckland'
    other = 'other'
    #aucklandUh = 'aucklandUh'
    #otherUh = 'otherUh'
    manualApproachChecked = 1
    areaImp2Checked = 2
    tpManualChecked = 3
    tcManualChecked = 4
    tpTcCalcsManualChecked = 5
    gisApproachChecked = 6
    areaImp2GisChecked = 7
    tpTcGisChecked = 8
    tpGisChecked = 9
    tcGisChecked = 10
    tpTcCalcsGisChecked = 11
    lengthSlopeChecked = 12
    demStreamlineChecked = 13

    # signals
    scsStart = pyqtSignal()
    tuflowProcessingStart = pyqtSignal()
    finished = pyqtSignal(str)

    def __init__(self, inputs: dict = None) -> None:
        QObject.__init__(self)
        self.inputs = inputs

    def run(self) -> None:
        """ Run the tool using SCS. """

        self.scsStart.emit()
        self.processIntoTuflow()

    def processIntoTuflow(self) -> None:
        """ Process output data from SCS into TUFLOW format. """

        self.tuflowProcessingStart.emit()

        # create TEF
        self.createTef()

        # create bc_dbase
        self.createBcDbase()

        # create inflows
        self.createInflows()

        # create log of input parameters
        self.createInputLog()

        self.finished.emit('')

    def createTef(self) -> None:
        """ Create TUFLOW Event File (TEF) based on the user's selected events. """

        tef = os.path.join((self.inputs['outputFolder']), 'event_file.tef')
        events = self.inputs['events']
        try:
            with open(tef, 'w') as fo:
                fo.write('! TEF Written by SCS to TUFLOW QGIS Plugin Tool\n\n')
                fo.write('!! RAINFALL EVENTS !!\n')
                for event in events:
                    fo.write(f'Define Event == {event}\n')
                    fo.write(f'    BC Event Source == ~ARI~ | {event}\n')
                    fo.write('End Define\n')
                    fo.write('!----------------------------------------\n')
        except PermissionError:
            self.finished.emit(f'{tef} Locked')
            return
        except IOError:
            self.finished.emit(f'Error Opening {tef}')
            return

    def createBcDbase(self) -> None:
        """ Create TUFLOW bc_dbase.csv based on user inputs i.e. catchment name. """

        bc_dbase = os.path.join((self.inputs['outputFolder']), 'bc_dbase.csv')
        events = self.inputs['events']
        try:
            if self.inputs['manualApproachChecked']:
                catchIdManualList = self.getCatchIdManual()
                with open(bc_dbase, 'w') as fo:
                    fo.write('Name,Source,Column 1,Column 2\n')
                    for id in catchIdManualList:
                        fo.write(f'{id},Inflows_~ARI~.csv,Time (hr), {id}\n')
            else:
                catchIdGisList = self.getCatchIdGis()
                with open(bc_dbase, 'w') as fo:
                    fo.write('Name,Source,Column 1,Column 2\n')
                    for id in catchIdGisList:
                        fo.write(f'{id},Inflows_~ARI~.csv,Time (hr), {id}\n')
        except PermissionError:
            self.finished.emit(f'{bc_dbase} Locked')
            return
        except IOError:
            self.finished.emit(f'Error Opening {bc_dbase}')
            return

    def createInflows(self) -> None:
        """ Create Inflow .csv files for all events. """

        events = self.inputs['events']
        for event in events:
            self.inputs['sourceInflows'] = f'Inflows_{event}.csv'
            inflows = os.path.join((self.inputs['outputFolder']), self.inputs['sourceInflows'])
            hydrograph = self.calculateSCS(event)
            try:
                if self.inputs['manualApproachChecked']:
                    catchIdManualList = self.getCatchIdManual()
                    catchIdManualString = ','.join(catchIdManualList)
                    np.savetxt(inflows, hydrograph, delimiter=',', fmt='%0.5f', comments='',
                               header=(f'Time (hr), {catchIdManualString}'))
                else:
                    catchIdGisList = self.getCatchIdGis()
                    catchIdGisString = ','.join(catchIdGisList)
                    np.savetxt(inflows, hydrograph, delimiter=',', fmt='%0.5f', comments='',
                               header=(f'Time (hr), {catchIdGisString}'))
            except PermissionError:
                self.finished.emit(f'{inflows} Locked')
                return
            except IOError:
                self.finished.emit(f'Error Opening {inflows}')
                return

    def createInputLog(self) -> None:
        """ Create log of input parameters. """

        inputLog = os.path.join((self.inputs['outputFolder']), 'input_log.txt')
        events = self.inputs['events']

        with open(inputLog, 'w') as log:
            log.write('Events and Design Rainfall Depth (mm)\n')
            for event in events:
                depthCalcs = self.inputs[event]
                log.write(event + ': ' + str(depthCalcs) + '\n')
            log.write('\n')
            log.write('Simulation Settings\n')
            log.write('Input Interval  (min): ' + str(self.inputs['intervalIn']) + '\n')
            log.write('Output Interval (min): ' + str(self.inputs['intervalOut']) + '\n')
            log.write('Decimal Spaces       : ' + str(self.inputs['decimals']) + '\n')
            log.write('\n')
            if self.inputs['manualApproachChecked']:
                log.write('Manual Approach\n')
                log.write('Catchment ID: ' + self.inputs['catchmentId'] + '\n')
                log.write('Curve Number Pervious : ' + str(self.inputs['cnPer']) + '\n')
                log.write('Area-Pervious     (ha): ' + str(self.inputs['areaPer']) + ', Suffix: ' + self.inputs['areaPerSuf'] + '\n')
                log.write('Area-Impervious 1 (ha): ' + str(self.inputs['areaImp1']) + ', Suffix: ' + self.inputs['areaImp1Suf'] + '\n')
                if self.inputs['areaImp2Checked']:
                    log.write('Area-Impervious 2 (ha): ' + str(self.inputs['areaImp2']) + ', Suffix: ' + self.inputs['areaImp2Suf'] + '\n')
                if self.inputs['tpManualChecked']:
                    log.write('Tp (hr) Per: ' + str(self.inputs['tpPer']) + ', Imp: ' + str(self.inputs['tpImp']) + '\n')
                if self.inputs['tcManualChecked']:
                    log.write('Tc (hr) Per: ' + str(self.inputs['tcPer']) + ', Imp: ' + str(self.inputs['tcImp']) + '\n')
                if self.inputs['tpTcCalcsManualChecked']:
                    log.write('Channelisation Factor Per: ' + str(self.inputs['cPer']) + ', Imp: ' + str(self.inputs['cImp']) + '\n')
                    log.write('Length (km): ' + str(self.inputs['length']) + '\n')
                    log.write('Slope (m/m): ' + str(self.inputs['slope']) + '\n')
            else:
                log.write('GIS Approach\n')

    def calculateSCS(self, event) -> np.array:
        """ Calculate SCS inflows.
            Auckland - every catchment is split into pervious and impervious areas and calculated separately.
            :return: hydrograph
        """

        timeOut = self.getTimeOut()
        if self.inputs['manualApproachChecked']:
            inflowManual = self.calculateInflowManual(event)
            hydrograph = np.column_stack((timeOut, inflowManual))
        else:
            time = self.getTimeGis()
            inflowGis = self.calculateInflowGis(event)
            hydrograph = np.column_stack((time, inflowGis))

        return hydrograph

    def calculateInflowManual(self, event) -> np.array:
        """ Calculate inflows for manual approach.
        :return: inflowManual
        """

        # inputs
        depthCalcs = self.inputs[event]
        intensityPer = self.getIntensityPerManual(event)
        intensityImp = self.getIntensityImpManual(event)
        tpPer, tpImp = self.getTpManual()
        intervalPer, intervalImp = self.getIntervalManual()
        timePer, timeImp = self.getTimeManual()
        timeOut = self.getTimeOut()

        # soil storage
        soilStoragePer = ((1000 / self.inputs['cnPer']) - 10) * 25.4
        soilStorageImp = ((1000 / self.inputs['cnImp']) - 10) * 25.4

        # runoff depth for 24h in mm
        runoffDepth24hPer = ((depthCalcs - self.inputs['iniLossPer']) ** 2) / \
                         ((depthCalcs - self.inputs['iniLossPer']) + soilStoragePer)
        runoffDepth24hImp = ((depthCalcs - self.inputs['iniLossImp']) ** 2) / \
                         ((depthCalcs - self.inputs['iniLossImp']) + soilStorageImp)

        # peak flow rate of unit hydrograph
        qpPer = (self.inputs['uhCurve'] * runoffDepth24hPer*0.001 * self.inputs['areaPer']*10000) / (tpPer*3600)
        qpImp1 = (self.inputs['uhCurve'] * runoffDepth24hImp*0.001 * self.inputs['areaImp1']*10000) / (tpImp*3600)
        qpImp2 = 0
        if self.inputs['areaImp2Checked']:
            qpImp2 = (self.inputs['uhCurve'] * runoffDepth24hImp*0.001 * self.inputs['areaImp2']*10000) / (tpImp*3600)

        # rainfall depth in mm for specified interval
        rainfallDepthPer = ((depthCalcs * intensityPer) / (24 / intervalPer))
        rainfallDepthImp = ((depthCalcs * intensityImp) / (24 / intervalImp))

        # cumulative rainfall depth
        cumulativeRainfallDepthPer = np.reshape(np.array(rainfallDepthPer[0]), 1)
        cumulativeRainfallDepthImp = np.reshape(np.array(rainfallDepthImp[0]), 1)
        for i in range(1, rainfallDepthPer.size):
            cumulatedDepthPer = cumulativeRainfallDepthPer[i-1] + rainfallDepthPer[i]
            cumulativeRainfallDepthPer = np.append(cumulativeRainfallDepthPer, cumulatedDepthPer)
        for i in range(1, rainfallDepthImp.size):
            cumulatedDepthImp = cumulativeRainfallDepthImp[i - 1] + rainfallDepthImp[i]
            cumulativeRainfallDepthImp = np.append(cumulativeRainfallDepthImp, cumulatedDepthImp)

        # cumulative rainfall excess based on remaining initial loss
        cumulativeRainfallExcessPer = np.array([])
        for i in range(0, cumulativeRainfallDepthPer.size):
            if cumulativeRainfallDepthPer[i] < self.inputs['iniLossPer']:
                cumulativeRainfallExcessPer = np.append(cumulativeRainfallExcessPer, 0)
            else:
                cumulativeRainfallExcessPer = np.append(cumulativeRainfallExcessPer, cumulativeRainfallDepthPer[i])
        cumulativeRainfallExcessImp = np.array([])
        for i in range(0, cumulativeRainfallDepthImp.size):
            if cumulativeRainfallDepthImp[i] < self.inputs['iniLossImp']:
                cumulativeRainfallExcessImp = np.append(cumulativeRainfallExcessImp, 0)
            else:
                cumulativeRainfallExcessImp = np.append(cumulativeRainfallExcessImp, cumulativeRainfallDepthImp[i])

        # cumulative runoff depth
        cumulativeRunoffDepthPer = np.array([])
        for i in range(0, cumulativeRainfallExcessPer.size):
            if cumulativeRainfallExcessPer[i] == 0:
                cumulativeRunoffDepthPer = np.append(cumulativeRunoffDepthPer, 0)
            else:
                cumulatedRunoffDepthPer = ((cumulativeRainfallExcessPer[i] - self.inputs['iniLossPer']) ** 2) / (
                            (cumulativeRainfallExcessPer[i] - self.inputs['iniLossPer']) + soilStoragePer)
                cumulativeRunoffDepthPer = np.append(cumulativeRunoffDepthPer, cumulatedRunoffDepthPer)
        cumulativeRunoffDepthImp = np.array([])
        for i in range(0, cumulativeRainfallExcessImp.size):
            if cumulativeRainfallExcessImp[i] == 0:
                cumulativeRunoffDepthImp = np.append(cumulativeRunoffDepthImp, 0)
            else:
                cumulatedRunoffDepthImp = ((cumulativeRainfallExcessImp[i] - self.inputs['iniLossImp']) ** 2) / (
                            (cumulativeRainfallExcessImp[i] - self.inputs['iniLossImp']) + soilStorageImp)
                cumulativeRunoffDepthImp = np.append(cumulativeRunoffDepthImp, cumulatedRunoffDepthImp)

        # runoff depth
        runoffDepthPer = np.array([cumulativeRunoffDepthPer[0]])
        for i in range(1, cumulativeRunoffDepthPer.size):
            runoffDepthPer = np.append(runoffDepthPer, cumulativeRunoffDepthPer[i]-cumulativeRunoffDepthPer[i-1])
        checkPer = runoffDepthPer.sum()
        runoffDepthImp = np.array([cumulativeRunoffDepthImp[0]])
        for i in range(1, cumulativeRunoffDepthImp.size):
            runoffDepthImp = np.append(runoffDepthImp, cumulativeRunoffDepthImp[i] - cumulativeRunoffDepthImp[i - 1])
        checkImp = runoffDepthImp.sum()

        # unit hydrograph - factored
        uhFlowRateDimensionless = self.inputs['uhOrdinates'][1,:]
        uhFlowRateFactoredPer = np.array([])
        for i in range(0, uhFlowRateDimensionless.size):
            uhFlowRateSinglePer = (uhFlowRateDimensionless[i] * qpPer) / runoffDepth24hPer
            uhFlowRateFactoredPer = np.append(uhFlowRateFactoredPer, uhFlowRateSinglePer)
        uhFlowRateFactoredImp1 = np.array([])
        for i in range(0, uhFlowRateDimensionless.size):
            uhFlowRateSingleImp1 = (uhFlowRateDimensionless[i] * qpImp1) / runoffDepth24hImp
            uhFlowRateFactoredImp1 = np.append(uhFlowRateFactoredImp1, uhFlowRateSingleImp1)
        uhFlowRateFactoredImp2 = np.array([])
        if self.inputs['areaImp2Checked']:
            for i in range(0, uhFlowRateDimensionless.size):
                uhFlowRateSingleImp2 = (uhFlowRateDimensionless[i] * qpImp2) / runoffDepth24hImp
                uhFlowRateFactoredImp2 = np.append(uhFlowRateFactoredImp2, uhFlowRateSingleImp2)

        # unit hydrograph inflows
        uhFullPer = np.zeros((runoffDepthPer.size, runoffDepthPer.size))
        for i in range(0, runoffDepthPer.size):
            uhValuesPer = runoffDepthPer[i] * uhFlowRateFactoredPer
            if i + uhValuesPer.size > runoffDepthPer.size:
                uhFullPer[i:runoffDepthPer.size , i] = uhValuesPer[:-(i+uhFlowRateFactoredPer.size-runoffDepthPer.size)]
            else:
                uhFullPer[i:i + uhFlowRateFactoredPer.size, i] = uhValuesPer

        uhFullImp1 = np.zeros((runoffDepthImp.size, runoffDepthImp.size))
        for i in range(0, runoffDepthImp.size):
            uhValuesImp1 = runoffDepthImp[i] * uhFlowRateFactoredImp1
            if i + uhValuesImp1.size > runoffDepthImp.size:
                uhFullImp1[i:runoffDepthImp.size , i] = uhValuesImp1[:-(i+uhFlowRateFactoredImp1.size-runoffDepthImp.size)]
            else:
                uhFullImp1[i:i + uhFlowRateFactoredImp1.size, i] = uhValuesImp1

        uhFullImp2 = np.zeros((runoffDepthImp.size, runoffDepthImp.size))
        for i in range(0, runoffDepthImp.size):
            uhValuesImp2 = runoffDepthImp[i] * uhFlowRateFactoredImp2
            if i + uhValuesImp2.size > runoffDepthImp.size:
                uhFullImp2[i:runoffDepthImp.size , i] = uhValuesImp2[:-(i+uhFlowRateFactoredImp2.size-runoffDepthImp.size)]
            else:
                uhFullImp2[i:i + uhFlowRateFactoredImp2.size, i] = uhValuesImp2

        # final inflows with input interval
        inflowPer = np.array([])
        # import pydevd_pycharm
        # pydevd_pycharm.settrace('localhost', port=53100, stdoutToServer=True, stderrToServer=True)
        for i in range(0, runoffDepthPer.size):
            inflowPerSum = uhFullPer[i, :].sum()
            inflowPer = np.append(inflowPer, inflowPerSum).round(decimals=self.inputs['decimals'])

        inflowImp1 = np.array([])
        for i in range(0, runoffDepthImp.size):
            inflowImp1Sum = uhFullImp1[i, :].sum()
            inflowImp1 = np.append(inflowImp1, inflowImp1Sum).round(decimals=self.inputs['decimals'])

        inflowImp2 = np.array([])
        if self.inputs['areaImp2Checked']:
            for i in range(0, runoffDepthImp.size):
                inflowImp2Sum = uhFullImp2[i, :].sum()
                inflowImp2 = np.append(inflowImp2, inflowImp2Sum).round(decimals=self.inputs['decimals'])

        # final inflows with output interval
        inflowPerOut = np.array([0])
        inflowImp1Out = np.array([0])
        inflowImp2Out = np.array([0])
        for interval in timeOut:
            if interval == 0:
                pass
            else:
                indexPer = np.abs(timePer - interval).argmin()
                inflowPerOut = np.append(inflowPerOut, inflowPer[indexPer])
                indexImp1 = np.abs(timeImp - interval).argmin()
                inflowImp1Out = np.append(inflowImp1Out, inflowImp1[indexImp1])
                if self.inputs['areaImp2Checked']:
                    indexImp2 = np.abs(timeImp - interval).argmin()
                    inflowImp2Out = np.append(inflowImp2Out, inflowImp2[indexImp2])

        if self.inputs['areaImp2Checked']:
            inflowManual = np.column_stack((inflowPerOut, inflowImp1Out, inflowImp2Out))
        else:
            inflowManual = np.column_stack((inflowPerOut, inflowImp1Out))

        return inflowManual

    def calculateInflowGis(self, event):
        """ Calculate inflows for GIS approach.
        :return: inflowGis
        """

        # intensity
        intensity = self.getIntensityGis(event)

        # GIS inputs
        cnGis = self.inputs['cnGis']
        areaPerGis = self.inputs['areaPerGis']
        areaPerCCGis = self.inputs['areaPerCCGis']
        areaImp1Gis = self.inputs['areaImp1Gis']
        areaImp1CCGis = self.inputs['areaImp1CCGis']
        areaImp2Gis = self.inputs['areaImp2Gis']
        areaImp2CCGis = self.inputs['areaImp2CCGis']
        tpTcGis = self.inputs['tpTcGis']
        cGis = self.inputs['cGis']
        lengthGis = self.inputs['lengthGis']
        slopeGis = self.inputs['slopeGis']

        inflowGis = intensity

        return inflowGis

    def getCatchIdManual(self) -> list:
        """ Create complete catchment IDs for manual calculation.
            :return: catchIdManualList
        """

        catchIdManualList = []
        catchIdManualList.append(self.inputs["catchmentId"] + self.inputs["areaPerSuf"])
        catchIdManualList.append(self.inputs["catchmentId"] + self.inputs["areaImp1Suf"])
        if self.inputs['areaImp2Checked']:
            catchIdManualList.append(self.inputs["catchmentId"] + self.inputs["areaImp2Suf"])

        return catchIdManualList

    def getCatchIdGis(self) -> list:
        """ Create a list of complete catchment IDs for GIS calculation.
            :return: catchIdGisList
        """

        catchIdGis = self.inputs['catchIdGis']
        catchIdGisList = []
        for catch in catchIdGis:
            catchIdGisList.append(catch + self.inputs["areaPerSufGis"])
            catchIdGisList.append(catch + self.inputs["areaImp1SufGis"])
            if self.inputs['areaImp2GisChecked']:
                catchIdGisList.append(catch + self.inputs["areaImp2SufGis"])

        return catchIdGisList

    def getTpManual(self) -> tuple:
        """ Calculate time of peak for manual calculation.
            :return: tpPer, tpImp
        """

        if self.inputs['tpManualChecked']:
            tpPer = self.inputs['tpPer']
            tpImp = self.inputs['tpImp']
        elif self.inputs['tcManualChecked']:
            tpPer = self.inputs['tcPer'] / 3 * 2
            tpImp = self.inputs['tcImp'] / 3 * 2
        else:
            tpPer = (0.14*self.inputs['cPer']*(self.inputs['length']**0.66)*((self.inputs['cnPer']/
                    (200-self.inputs['cnPer']))**-0.55)*(self.inputs['slope']**-0.3))/3*2
            if tpPer < 0.11:
                tpPer = 0.11
            tpImp = (0.14 * self.inputs['cImp'] * (self.inputs['length'] ** 0.66) * ((self.inputs['cnImp'] /
                    (200 - self.inputs['cnImp'])) ** -0.55) * (self.inputs['slope'] ** -0.3)) / 3 * 2
            if tpImp < 0.11:
                tpImp = 0.11

        return tpPer, tpImp

    def getIntervalManual(self) -> tuple:
        """ Calculate interval step based on unit hydrograph step for manual calculation.
            :return: intervalPer, intervalImp
        """

        tpPer, tpImp = self.getTpManual()
        intervalPer = tpPer * self.inputs['uhStep']
        intervalImp = tpImp * self.inputs['uhStep']

        return intervalPer, intervalImp

    def getTimeManual(self) -> np.array:
        """ Calculate time column for calculations based on input interval.
            :return: timePer, timeImp
        """

        timePer = np.array([0])
        timeImp = np.array([0])
        if self.inputs['manualApproachChecked']:
            tpPer, tpImp = self.getTpManual()
            intervalPer, intervalImp = self.getIntervalManual()
            tPer = timePer[-1]
            while tPer < 23.999999:
                tPer = timePer[-1] + intervalPer
                timePer = np.append(timePer, tPer)
            timePer = timePer.round(decimals=4)
            tImp = timeImp[-1]
            while tImp < 23.999999:
                tImp = timeImp[-1] + intervalImp
                timeImp = np.append(timeImp, tImp)
            timeImp = timeImp.round(decimals=4)

        return timePer, timeImp

    def getTimeGis(self) -> np.array:
        """ Calculate time column for calculations based on input interval.
            :return: time
        """

        time = np.array([0])
        if self.inputs['gisApproachChecked']:
            t = time[-1]
            while t < 23.999999:
                t = time[-1] + self.inputs['interval']
                time = np.append(time, t)
            time = time.round(decimals=4)

        return time

    def getTimeOut(self) -> np.array:
        """ Calculate time column for output inflows based on input interval.
            :return: timeOut
        """

        timeOut = np.array([0])
        t = timeOut[-1]
        while t < 23.999999:
            t = timeOut[-1] + (self.inputs['intervalOut']/60)
            timeOut = np.append(timeOut, t)
        timeOut = timeOut.round(decimals=4)

        return timeOut

    def getIntensity(self, event, time, intensity) -> np.array:
        """ Assign intensity based on non CC, CC and time.
            :return: intensity
        """

        if 'CC' in event:
            for i in time:
                if i >= 0 and i < 5.99999:
                    intensity_value = 0.33
                    intensity = np.append(intensity, intensity_value)
                elif i >= 5.99999 and i <= 8.99999:
                    intensity_value = 0.73
                    intensity = np.append(intensity, intensity_value)
                elif i >= 8.99999 and i <= 9.99999:
                    intensity_value = 0.95
                    intensity = np.append(intensity, intensity_value)
                elif i >= 9.99999 and i <= 10.99999:
                    intensity_value = 1.40
                    intensity = np.append(intensity, intensity_value)
                elif i >= 10.99999 and i <= 11.49999:
                    intensity_value = 2.20
                    intensity = np.append(intensity, intensity_value)
                elif i >= 11.49999 and i <= 11.66666:
                    intensity_value = 3.82
                    intensity = np.append(intensity, intensity_value)
                elif i >= 11.66666 and i <= 11.83332:
                    intensity_value = 4.86
                    intensity = np.append(intensity, intensity_value)
                elif i >= 11.83332 and i <= 11.99999:
                    intensity_value = 8.86
                    intensity = np.append(intensity, intensity_value)
                elif i >= 11.99999 and i <= 12.16666:
                    intensity_value = 16.65
                    intensity = np.append(intensity, intensity_value)
                elif i >= 12.16666 and i <= 12.33332:
                    intensity_value = 5.95
                    intensity = np.append(intensity, intensity_value)
                elif i >= 12.33332 and i <= 12.49999:
                    intensity_value = 4.24
                    intensity = np.append(intensity, intensity_value)
                elif i >= 12.49999 and i <= 12.99999:
                    intensity_value = 2.92
                    intensity = np.append(intensity, intensity_value)
                elif i >= 12.99999 and i <= 13.99999:
                    intensity_value = 1.70
                    intensity = np.append(intensity, intensity_value)
                elif i >= 13.99999 and i <= 14.99999:
                    intensity_value = 1.19
                    intensity = np.append(intensity, intensity_value)
                elif i >= 14.99999 and i <= 17.99999:
                    intensity_value = 0.75
                    intensity = np.append(intensity, intensity_value)
                elif i >= 17.99999 and i <= 23.99999:
                    intensity_value = 0.39
                    intensity = np.append(intensity, intensity_value)
                else:
                    intensity_value = 0.00
                    intensity = np.append(intensity, intensity_value)
        else:
            for i in time:
                if i >= 0 and i < 5.99999:
                    intensity_value = 0.34
                    intensity = np.append(intensity, intensity_value)
                elif i >= 5.99999 and i <= 8.99999:
                    intensity_value = 0.74
                    intensity = np.append(intensity, intensity_value)
                elif i >= 8.99999 and i <= 9.99999:
                    intensity_value = 0.96
                    intensity = np.append(intensity, intensity_value)
                elif i >= 9.99999 and i <= 10.99999:
                    intensity_value = 1.40
                    intensity = np.append(intensity, intensity_value)
                elif i >= 10.99999 and i <= 11.49999:
                    intensity_value = 2.20
                    intensity = np.append(intensity, intensity_value)
                elif i >= 11.49999 and i <= 11.66666:
                    intensity_value = 3.80
                    intensity = np.append(intensity, intensity_value)
                elif i >= 11.66666 and i <= 11.83332:
                    intensity_value = 4.80
                    intensity = np.append(intensity, intensity_value)
                elif i >= 11.83332 and i <= 11.99999:
                    intensity_value = 8.70
                    intensity = np.append(intensity, intensity_value)
                elif i >= 11.99999 and i <= 12.16666:
                    intensity_value = 16.20
                    intensity = np.append(intensity, intensity_value)
                elif i >= 12.16666 and i <= 12.33332:
                    intensity_value = 5.90
                    intensity = np.append(intensity, intensity_value)
                elif i >= 12.33332 and i <= 12.49999:
                    intensity_value = 4.20
                    intensity = np.append(intensity, intensity_value)
                elif i >= 12.49999 and i <= 12.99999:
                    intensity_value = 2.90
                    intensity = np.append(intensity, intensity_value)
                elif i >= 12.99999 and i <= 13.99999:
                    intensity_value = 1.70
                    intensity = np.append(intensity, intensity_value)
                elif i >= 13.99999 and i <= 14.99999:
                    intensity_value = 1.20
                    intensity = np.append(intensity, intensity_value)
                elif i >= 14.99999 and i <= 17.99999:
                    intensity_value = 0.75
                    intensity = np.append(intensity, intensity_value)
                elif i >= 17.99999 and i <= 23.99999:
                    intensity_value = 0.40
                    intensity = np.append(intensity, intensity_value)
                else:
                    intensity_value = 0.00
                    intensity = np.append(intensity, intensity_value)

        return intensity

    def getIntensityPerManual(self, event) -> np.array:
        """ Assign pervious intensity for manual calculation.
            :return: intensityPer
        """

        intensityPer = np.array([])
        if self.inputs['manualApproachChecked']:
            timePer, timeImp = self.getTimeManual()
            intensityPer = self.getIntensity(event, timePer, intensityPer)

        return intensityPer

    def getIntensityImpManual(self, event) -> np.array:
        """ Assign impervious intensity for manual calculation.
            :return: intensityImp
        """

        intensityImp = np.array([])
        if self.inputs['manualApproachChecked']:
            timePer, timeImp = self.getTimeManual()
            intensityImp = self.getIntensity(event, timeImp, intensityImp)

        return intensityImp

    def getIntensityGis(self, event) -> np.array:
        """ Assign intensity for GIS calculation.
            :return: intensity
        """

        intensity = np.array([])
        if self.inputs['gisApproachChecked']:
            time = self.getTimeGis()
            intensity = self.getIntensity(event, time, intensity)

        return intensity

