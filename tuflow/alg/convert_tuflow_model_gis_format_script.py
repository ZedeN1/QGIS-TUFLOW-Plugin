from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingParameterDefinition
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterFile
from qgis.core import QgsProcessingParameterEnum
import subprocess
import sys
import time
import re
import os
from pathlib import Path


CONTROL_FILES = [
    'GEOMETRY CONTROL FILE', 'BC CONTROL FILE', 'ESTRY CONTROL FILE', 'EVENT FILE', 'READ FILE',
    'RAINFALL CONTROL FILE', 'EXTERNAL STRESS FILE', 'QUADTREE CONTROL FILE', 'AD CONTROL FILE'
    ]


def strip_command(text):
    t = text
    c, v, comment = None, None, ''
    if t.strip() and not t[0] in ('!', '#'):
        if '!' in t or '#' in t:
            i = t.index('!') if '!' in t else 9e29
            j = t.index('#') if '#' in t else 9e29
            comment_index = k = min(i, j)
            t, comment = t[:k], t[k:].strip()
        if '==' in t:
            c, v = t.split('==', 1)
            v = v.strip()
        else:
            c, v = t, None
        if c.strip():
            prefix = re.split(r'[a-z]', c, flags=re.IGNORECASE)[0]
        c = c.strip().upper()

    return c, v


def globify(text):
    wildcards = [r'(<<.{1,}?>>)']
    new_text = text
    for wc in wildcards:
        new_text = re.sub(wc, '*', new_text, flags=re.IGNORECASE)
    if re.findall(re.escape(r'**'), new_text):
        new_text = re.sub(re.escape(r'**'), '*', new_text)

    return new_text


def count_lines(file):
    line_count = 0
    if os.path.exists(file):
        with open(file, 'r') as f:
            for line in f:
                if line.strip():
                    line_count += 1
                command, value = strip_command(line)
                if command in CONTROL_FILES:
                    line_count += 1
                    if value.upper() == 'AUTO':
                        value = '{0}.ecf'.format(os.path.splitext(os.path.basename(value))[0])
                    value = globify(value)
                    for cf in Path(file).parent.glob(value):
                        line_count += count_lines(cf)

    return line_count


GIS_FORMAT = {0: 'GPKG', 1: 'SHP', 2: 'MIF'}
GRID_FORMAT = {0: 'TIF', 1: 'GPKG', 2: 'FLT', 3: 'ASC'}
OP = {0: 'SEPARATE', 1: 'CF1', 2: 'CF2', 3: 'TCF'}


class ConvertTuflowModelGisFormat(QgsProcessingAlgorithm):
    
    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterFile('tcf', 'TCF', behavior=QgsProcessingParameterFile.File, fileFilter='TCF (*.tcf *.TCF)', defaultValue=None))
        self.addParameter(QgsProcessingParameterEnum('outputvectorformat', 'Output Vector Format', options=['GPKG','SHP','MIF'], allowMultiple=False, defaultValue=[0]))
        self.addParameter(QgsProcessingParameterEnum('outputrasterformat', 'Output Raster Format', options=['GTIFF','GPKG','FLT', 'ASC'], allowMultiple=False, defaultValue=[0]))
        self.addParameter(QgsProcessingParameterEnum('outputprofile', 'Output Profile', options=['SEPARATE','GROUP BY CONTROL FILE 1', 'GROUP BY CONTROL FILE 2','ALL IN ONE'], allowMultiple=False, defaultValue=[0]))
        self.addParameter(QgsProcessingParameterFile('outputfolder', 'Output Folder', optional=True, behavior=QgsProcessingParameterFile.Folder, fileFilter='All files (*.*)', defaultValue=None))
        param = QgsProcessingParameterFile('rootfolder', 'Root Folder', optional=True, behavior=QgsProcessingParameterFile.Folder, fileFilter='All files (*.*)', defaultValue=None)
        param.setFlags(param.flags() | QgsProcessingParameterDefinition.FlagAdvanced)
        self.addParameter(param)
        
    def processAlgorithm(self, parameters, context, model_feedback):
        line_count = count_lines(parameters['tcf']) + 3

        feedback = QgsProcessingMultiStepFeedback(line_count, model_feedback)
        feedback.pushInfo('line count: {0}'.format(line_count))

        # params
        tcf = parameters['tcf']
        gis = GIS_FORMAT[parameters['outputvectorformat']]
        grid = GRID_FORMAT[parameters['outputrasterformat']]
        op = OP[parameters['outputprofile']]
        of = parameters['outputfolder']
        rf = parameters['rootfolder']

        # script path
        script = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'convert_tuflow_model_gis_format', 'convert_tuflow_gis_format.py')

        args = ['python', '-u', script, '-tcf', str(tcf), '-gis', str(gis), '-grid', str(grid), '-op', str(op)]
        if of:
            args.extend(['-o', str(of)])
        if rf:
            args.extend(['-rf', str(rf)])

        feedback.pushInfo('args: {0}'.format(args[3:]))

        count = 0
        with subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, creationflags=subprocess.CREATE_NO_WINDOW, bufsize=0, universal_newlines=True) as proc:
            for line in proc.stdout:
                if line.strip():
                    count += 1
                feedback.setCurrentStep(count)
                feedback.pushInfo(line.strip('\n'))

                # Stop the algorithm if cancel button has been clicked
                if feedback.isCanceled():
                    proc.terminate()
        
        feedback.setProgress(line_count)
        return {}
        
    def name(self):
        return 'Convert TUFLOW Model GIS Format'

    def displayName(self):
        return self.tr(self.name())

    def group(self):
        return self.tr(self.groupId())

    def groupId(self):
        return ''

    def shortHelpString(self):
        return self.tr(
            "<a href=\"https://wiki.tuflow.com/index.php?title=Convert_TUFLOW_Model_GIS_Format\">"
            "Documentation on TUFLOW Wiki</a><p>"
            "<p>"
            "This tool runs a Python script that will convert a given TUFLOW model's vector and raster GIS files "
            "into another, or same, supported TUFLOW format. The script is similar to the package model "
            "functionality that exists in TUFLOW and will try and package files from all "
            "scenarios/events. The difference between the package model functionality and this script, "
            "is that this script will perform additional format conversion steps and update relevant control files."
            "<p>"
            "The tool also gives additional options when converting to GPKG vector and raster formats. The "
            "GPKG format is a database format and allows multiple layers within one file (including a mixture of "
            "vectors and rasters) and the tool gives options on how layers are grouped: "
            "<p>"
            "<p>"
            "Tool Inputs:<p>"
            " 1. TCF: The location of the input TUFLOW model's TCF file to be converted<p>"
            " 2. Output Vector Format - The output vector format<p>"
            " 3. Output Raster Format - The output raster format<p>"
            " 4. Output Profile - For GPKG outputs only - will determine how layers are grouped into databases. "
            "Options:<p>"
            "       a) SEPARATE will write each layer into its own database. "
            "TUFLOW commands that read multiple geometry types on a single line will all be converted into a single "
            "database.<p>"
            "       b) GROUP BY CONTROL FILE 1 - will group layers by control file<p>"
            "       c) GROUP BY CONTROL FILE 2 - similar to GROUP BY CONTROL FILE 1 but will consider "
            "TEF and TRD files as separate control files<p>"
            "       d) ALL IN ONE - will output every layer into one centralised database<p>"
            " 5. Output Folder - optional output location for the converted model and files. If none is specified "
            "a folder is created in the same location as the TCF<p>"
            " 6. Root Folder - only required if the tool can't find the the root folder (traditionally named 'TUFLOW') "
            "where all modelling files sit beneath<p>"
        )

    def shortDescription(self):
        return self.tr("Package and convert a TUFLOW model's GIS files into a different format.")

    def createInstance(self):
        return ConvertTuflowModelGisFormat()
        
    def tr(self, string):
        return QCoreApplication.translate('Processing', string)
