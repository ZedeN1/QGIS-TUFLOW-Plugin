import os
from datetime import datetime, timedelta
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from qgis.core import *
from PyQt5.QtWidgets import *
import tuflow.TUFLOW_results as TuflowResults
import tuflow.TUFLOW_results2013 as TuflowResults2013
from tuflow.tuflowqgis_library import (getPathFromRel, tuflowqgis_apply_check_tf_clayer, datetime2timespec,
                                       datetime2timespec, roundSeconds, isPlotLayer)
import re
from tuflow.TUFLOW_FM_data_provider import TuFloodModellerDataProvider
from math import atan2, sin, cos, pi


class TuResults1D():
	"""
	Class for handling 1D results
	
	"""
	
	def __init__(self, TuView):
		self.tuView = TuView
		self.iface = self.tuView.iface
		self.results1d = {}  # dict -> converting result name to 1d results
		self.ids = []  # list -> str selected time series result lists
		self.domains = []  # list -> str selected time series result domains i.e. 1d, 2d, RL
		self.sources = []  # list -> str selected time series sources i.e. HU
		self.items1d = []  # list -> Dataset_View Tree node selected dataset view tree node item
		self.typesTS = []  # list -> str selected 1D time series result types
		self.pointTS = []
		self.lineTS = []
		self.regionTS = []
		# self.activeType = -1  # -1 null, 0 pointTS, 1 lineTS, 2 RegionTS, 3 XS
		self.activeType = []  # -1 null, 0 pointTS, 1 lineTS, 2 RegionTS, 3 XS
		self.typesLP = []  # list -> str selected 1D long plot result types
		self.typesXS = []  # 1D cross section types
		self.lineXS = []  # 1D cross section line types
		self.typesXSRes = []  # store results that can be plotted on XS (i.e. water level)

	def importResults(self, inFilePaths):
		"""
		Loads in the 1D result class.

		:param inFileNames: list -> str tpc file paths
		:return: bool -> True for successful, False for unsuccessful
		"""

		qv = Qgis.QGIS_VERSION_INT
		
		openResults = self.tuView.OpenResults  # QListWidget
		results = self.tuView.tuResults.results  # dict of indexed results
		
		for filePath in inFilePaths:
			
			# parse file names, ext, directory
			fdir, fname = os.path.split(filePath)
			root, ext = os.path.splitext(filePath)
			
			# 2013 results
			if ext.upper() == '.INFO':
				res = TuflowResults2013.ResData()
				res.Load(filePath, self.iface)
			
			# post 2013 results
			elif ext.upper() == '.TPC':
				res = TuflowResults.ResData()
				error, message = res.Load(filePath)
				if error:
					QMessageBox.critical(self.tuView, "TUFLOW Viewer", message)
					return False
				
			else:
				return False
			
			# index results
			index = self.getResultMetaData(res)
			self.results1d[res.displayname] = res

			if qv >= 31600:
				self.tuView.tuResults.updateDateTimes()
			
			# add result to list widget
			openResultNames = []
			for i in range(openResults.count()):
				openResultNames.append(openResults.item(i).text())
			if res.displayname not in openResultNames:
				openResults.addItem(res.displayname)  # add to widget
			k = openResults.findItems(res.displayname, Qt.MatchRecursive)[0]
			k.setSelected(True)
			
		return True

	def importResultsFM(self, gxy, dat, inFilePaths):
		"""
		Import flood modeller results using a .gxy file and any number of
		result csv files

		"""

		qv = Qgis.QGIS_VERSION_INT

		openResults = self.tuView.OpenResults  # QListWidget
		results = self.tuView.tuResults.results  # dict of indexed results
		crs = QgsProject.instance().crs()

		for i, filePath in enumerate(inFilePaths):

			simname = TuFloodModellerDataProvider.getSimulationName(filePath)
			if simname in self.results1d:
				res = self.results1d[simname]
			else:
				res = TuFloodModellerDataProvider()

			# gxy/section - only load gxy and section data once
			if i == 0:
				err, msg = res.load_gxy(gxy)
				if res.isgxyValid:
					# load into qgis
					# nodes
					uri = "point?crs={0}&field=ID:string&field=Type:string&field=Source:string&field=Unit_Type:string(20)&field=Full_Type:string(20)".format(crs.authid())
					fmNodesLayer = QgsVectorLayer(uri, '{0}_FM_PLOT_P'.format(res.gxyname), 'memory')
					feats = []
					for node in res.nodes.nodes:
						feat = QgsFeature()
						feat.setGeometry(QgsPoint(node.x, node.y))
						feat.setFields(fmNodesLayer.fields())
						feat['ID'] = node.id
						feat['Type'] = 'Node'
						feat['Source'] = 'H_V_Q_'
						feat['Unit_Type'] = node.type
						feat['Full_Type'] = node.sub_type
						feats.append(feat)
					fmNodesLayer.dataProvider().truncate()
					fmNodesLayer.dataProvider().addFeatures(feats)
					fmNodesLayer.updateExtents()
					fmNodesLayer.triggerRepaint()
					# links
					uri = "linestring?crs={0}&field=ID:string&field=Type:string&field=Source:string&field=Upstrm_Type:string(20)&field=Dnstrm_Type:string(20)".format(crs.authid())
					fmLinksLayer = QgsVectorLayer(uri, '{0}_FM_PLOT_L'.format(res.gxyname), 'memory')
					feats = []
					for link in res.links:
						feat = QgsFeature()
						feat.setGeometry(QgsGeometry.fromPolyline([QgsPoint(link.x[i], link.y[i]) for i in range(len(link.x))]))
						feat.setFields(fmLinksLayer.fields())
						feat['ID'] = str(link.index)
						feat['Type'] = 'Chan'
						feat['Source'] = 'H_'
						feat['Upstrm_Type'] = link.us_node.type
						feat['Dnstrm_Type'] = link.ds_node.type
						feats.append(feat)
					fmLinksLayer.dataProvider().truncate()
					fmLinksLayer.dataProvider().addFeatures(feats)
					fmLinksLayer.updateExtents()
					fmLinksLayer.triggerRepaint()

					if fmLinksLayer.isValid():
						self.tuView.project.addMapLayer(fmLinksLayer)
						tuflowqgis_apply_check_tf_clayer(self.iface, layer=fmLinksLayer)
					if fmNodesLayer.isValid():
						self.tuView.project.addMapLayer(fmNodesLayer)
						tuflowqgis_apply_check_tf_clayer(self.iface, layer=fmNodesLayer)
				if err:
					QMessageBox.warning(self.iface.mainWindow(), 'Import GXY File', 'WARNING: error reading {0} nodes / links:\n'.format(len(msg), msg))

				if dat is not None:
					err, msg = self.tuView.crossSectionsFM.fmLoadDat(dat)
					res.loadBedElevations(self.tuView.crossSectionsFM)
					if self.tuView.crossSectionsFM.fm_nXs:
						uri = "linestring?crs={0}&field=Source:string(50)&field=Type:string(2)&field=Flags:string(8)" \
						      "&field=Column_1:string(8)" \
						      "&field=Column_2:string(8)" \
						      "&field=Column_3:string(8)" \
						      "&field=Column_4:string(8)" \
						      "&field=Column_5:string(8)" \
						      "&field=Column_6:string(8)" \
						      "&field=Z_Incremen:double" \
						      "&field=Z_Maximum:double" \
						      "&field=Provider:string(8)" \
						      "&field=Comments:string(100)".format(crs.authid())
						fmXSLayer = QgsVectorLayer(uri,
						                           '1d_xz_{0}'.format(os.path.basename(os.path.splitext(dat)[0])),
						                           'memory')

						feats = []
						skipped_xs = []
						for xs in self.tuView.crossSectionsFM.fm_xs:
							if xs.FM_nxypnts > 0:
								# skipped_xs.append(xs.source)
								# continue
								feat = QgsFeature()
								feat.setGeometry(QgsGeometry.fromPolyline([QgsPoint(xs.FM_xloc[i], xs.FM_yloc[i]) for i in range(xs.FM_nxypnts)]))
								feat.setFields(fmXSLayer.fields())
								feat['Source'] = xs.source
								feat['Type'] = xs.type
								feat['Flags'] = ""
								feat['Column_1'] = ""
								feat['Column_2'] = ""
								feat['Column_3'] = ""
								feat['Column_4'] = ""
								feat['Column_5'] = ""
								feat['Column_6'] = ""
								feat['Z_Incremen'] = 0.
								feat['Z_Maximum'] = 0.
								feat['Provider'] = "FM"
								feat['Comments'] = '{0} points filtered for having coords (x,y) = (0,0)'.format(xs.FM_nFiltered_points) if xs.FM_nFiltered_points > 0 else ''
								xs.feature = feat
								feats.append(feat)
							elif xs.source.lower() in [x.id.lower() for x in res.nodes.nodes]:
								inode = [x.id.lower() for x in res.nodes.nodes].index(xs.source.lower())
								node = res.nodes.nodes[inode]
								feat = QgsFeature()
								link_upn = [x.us_node for x in res.links]
								link_dnn = [x.ds_node for x in res.links]
								if node in link_dnn:
									x = res.links[link_dnn.index(node)].x
									y = res.links[link_dnn.index(node)].y
								elif node in link_upn:
									x = res.links[link_upn.index(node)].x
									y = res.links[link_upn.index(node)].y
								else:
									x = [node.x - 1, node.x]
									y = [node.y, node.y]
								# line perpendicular link running through node
								length = 20.
								ang = atan2((y[1] - y[0]), (x[1] - x[0]))
								rx = [node.x + cos(ang + pi / 2.) * length / 2., node.x, node.x + cos(ang - pi / 2.) * length / 2.]
								ry = [node.y + sin(ang + pi / 2.) * length / 2., node.y, node.y + sin(ang - pi / 2.) * length / 2.]
								feat.setGeometry(QgsGeometry.fromPolyline([QgsPoint(rx[i], ry[i]) for i in range(3)]))
								feat.setFields(fmXSLayer.fields())
								feat['Source'] = xs.source
								feat['Type'] = xs.type
								feat['Flags'] = ""
								feat['Column_1'] = ""
								feat['Column_2'] = ""
								feat['Column_3'] = ""
								feat['Column_4'] = ""
								feat['Column_5'] = ""
								feat['Column_6'] = ""
								feat['Z_Incremen'] = 0.
								feat['Z_Maximum'] = 0.
								feat['Provider'] = "FM"
								feat['Comments'] = '{0} points filtered for having coords (x,y) = (0,0)'.format(
									xs.FM_nFiltered_points) if xs.FM_nFiltered_points > 0 else ''
								xs.feature = feat
								feats.append(feat)
							else:
								skipped_xs.append(xs.source)

						fmXSLayer.dataProvider().truncate()
						fmXSLayer.dataProvider().addFeatures(feats)
						fmXSLayer.updateExtents()
						fmXSLayer.triggerRepaint()

						if fmXSLayer.isValid():
							self.tuView.project.addMapLayer(fmXSLayer)
							tuflowqgis_apply_check_tf_clayer(self.iface, layer=fmXSLayer)
					if err:
						QMessageBox.warning(self.tuView, 'Import DAT File',
						                    'WARNING: error reading {0} sections:\n'.format(len(msg), '\n'.join(msg)))
					if skipped_xs:
						QMessageBox.warning(self.tuView, 'Import DAT File',
						                    'WARNING: {0} cross sections have been skipped and won\'t be displayed due to invalid spatial '
						                    'referencing X,Y data\n\n{1}'.format(len(skipped_xs), '\n'.join(skipped_xs)))

			# for filePath in inFilePaths:
			error, message = res.Load(filePath)
			if error:
				QMessageBox.critical(self.tuView, "TUFLOW Viewer", 'ERROR: {0} errors occured loading in results: {1}:\n{2}'.format(len(message), filePath, '\n'.join(message)))
				continue

			# index results
			index = self.getResultMetaData(res, hasMax=False)
			self.results1d[res.displayname] = res

			if qv >= 31600:
				self.tuView.tuResults.updateDateTimes()

			# add result to list widget
			openResultNames = []
			for i in range(openResults.count()):
				openResultNames.append(openResults.item(i).text())
			if res.displayname not in openResultNames:
				openResults.addItem(res.displayname)  # add to widget
			k = openResults.findItems(res.displayname, Qt.MatchRecursive)[0]
			k.setSelected(True)

		return True

	def openGis(self, tpc):
		"""
		Opens 1D gis files. Will check if there are any features in the layer before loading into QGIS.

		:param tpc: str -> file path to tpc file
		:return: bool -> True for successful, False for unsuccessful
		"""

		# Initialise variables
		fpath = os.path.dirname(tpc)
		gisPoints = None
		gisLines = None
		gisRegions = None
		
		# get gis file location from tpc
		with open(tpc, 'r') as fo:
			for line in fo:
				if '==' in line:
					command, value = line.split('==')
					command = command.strip()
					value = value.strip()
					if 'gis plot layer points' in command.lower():
						gisPoints = getPathFromRel(fpath, value)
					elif 'gis plot layer lines' in command.lower():
						gisLines = getPathFromRel(fpath, value)
					elif 'gis plot layer regions' in command.lower():
						gisRegions = getPathFromRel(fpath, value)
		
		# load points gis file
		if gisPoints is not None:
			layer, basename = self.loadVectorLayer(gisPoints)
			if not layer.isValid():
				return False
			if layer.featureCount():  # only load if there are any features
				self.tuView.project.addMapLayer(layer)
				tuflowqgis_apply_check_tf_clayer(self.iface, layer=layer)
		# load lines gis file
		if gisLines is not None:
			layer, basename = self.loadVectorLayer(gisLines)
			if not layer.isValid():
				return False
			if layer.featureCount():  # only load if there are any features
				self.tuView.project.addMapLayer(layer)
				tuflowqgis_apply_check_tf_clayer(self.iface, layer=layer)
		# load regions gis file
		if gisRegions is not None:
			layer, basename = self.loadVectorLayer(gisRegions)
			if not layer.isValid():
				return False
			if layer.featureCount():  # only load if there are any features
				self.tuView.project.addMapLayer(layer)
				tuflowqgis_apply_check_tf_clayer(self.iface, layer=layer)
				
		return True
	
	def loadVectorLayer(self, fpath):
		"""
		Load the vector layer i.e. .shp or .mif

		:param fpath: str
		:return: QgsVectorLayer
		:return: str -> layer name e.g. 2d_bc_M01_001_L
		"""
		
		# Parse out file names
		pattern = re.escape(r'.gpkg|layername=')
		if re.findall(pattern, fpath, re.IGNORECASE):
			basename = re.split(pattern, fpath, re.IGNORECASE)[1]
		else:
			basepath, fext = os.path.splitext(fpath)
			basename = os.path.basename(basepath)
		
		# Load vector
		layer = QgsVectorLayer(fpath, basename, 'ogr')
		
		return layer, basename

	def getResultMetaData(self, result, hasMax=True):
		qv = Qgis.QGIS_VERSION_INT
		if qv < 31600:
			self.getResultMetaData_old(result)
		else:
			self.getResultMetaData_31600(result, hasMax)
	
	def getResultMetaData_old(self, result):
		"""
		Get result types and timesteps for 1D results
		
		:param result: TUFLOW_results.ResData
		:return: bool -> True for successful, False for unsuccessful
		"""

		qv = Qgis.QGIS_VERSION_INT

		results = self.tuView.tuResults.results  # dict
		timekey2time = self.tuView.tuResults.timekey2time  # dict
		timekey2date = self.tuView.tuResults.timekey2date  # dict
		time2date = self.tuView.tuResults.time2date  # dict
		date2timekey = self.tuView.tuResults.date2timekey
		date2time = self.tuView.tuResults.date2time
		zeroTime = self.tuView.tuOptions.zeroTime  # datetime

		if result.displayname not in results.keys():
			results[result.displayname] = {}

		if self.tuView.OpenResults.count() == 0:
			self.tuView.tuOptions.zeroTime = datetime2timespec(self.getReferenceTime(result, defaultZeroTime=zeroTime),
			                                                   1, self.tuView.tuResults.timeSpec)
			if qv >= 31300:
				self.tuView.tuOptions.timeSpec = self.iface.mapCanvas().temporalRange().begin().timeSpec()
				self.tuView.tuResults.loadedTimeSpec = self.iface.mapCanvas().temporalRange().begin().timeSpec()
		self.configTemporalProperties(result)

		timesteps = result.timeSteps(datetime2timespec(self.tuView.tuOptions.zeroTime, self.tuView.tuResults.loadedTimeSpec, 1))
		for t in timesteps:
			date = self.tuView.tuOptions.zeroTime + timedelta(hours=t)
			# date = datetime2timespec(self.tuView.tuOptions.zeroTime,
			#                          self.tuView.tuResults.loadedTimeSpec,
			#                          self.tuView.tuResults.timeSpec) \
			#        + timedelta(hours=t)
			date = roundSeconds(date, 2)
			timekey2time['{0:.6f}'.format(t)] = t
			timekey2date['{0:.6f}'.format(t)] = zeroTime + timedelta(hours=t)
			time2date[t] = date
			date2timekey[date] = '{0:.6f}'.format(t)
			date2time[date] = t

			if qv >= 31300:
				date_tspec = datetime2timespec(date, self.tuView.tuResults.loadedTimeSpec, 1)
			else:
				date_tspec = date
			self.tuView.tuResults.timekey2date_tspec['{0:.6f}'.format(t)] = date_tspec
			self.tuView.tuResults.time2date_tspec[t] = date_tspec
			self.tuView.tuResults.date_tspec2timekey[date_tspec] = '{0:.6f}'.format(t)
			self.tuView.tuResults.date_tspec2time[date_tspec] = t
			self.tuView.tuResults.date2date_tspec[date] = date_tspec
			self.tuView.tuResults.date_tspec2date[date_tspec] = date

		#if 'point_ts' not in results[result.displayname].keys():
		resultTypes = result.pointResultTypesTS()
		metadata1d = (resultTypes, timesteps)
		results[result.displayname]['point_ts'] = metadata1d
		
		#if 'line_ts' not in results[result.displayname].keys():
		resultTypes = result.lineResultTypesTS()
		if 'Velocity' in resultTypes and 'Velocity' in result.pointResultTypesTS():
			resultTypes.remove('Velocity')
		metadata1d = (resultTypes, timesteps)
		results[result.displayname]['line_ts'] = metadata1d
		
		#if 'region_ts' not in results[result.displayname].keys():
		resultTypes = result.regionResultTypesTS()
		metadata1d = (resultTypes, timesteps)
		results[result.displayname]['region_ts'] = metadata1d
		
		#if 'line_lp' not in results[result.displayname].keys():
		resultTypes = result.lineResultTypesLP()
		metadata1d = (resultTypes, timesteps)
		results[result.displayname]['line_lp'] = metadata1d
		
		return True

	def getResultMetaData_31600(self, result, hasMax):
		"""
		Get result types and timesteps for 1D results

		:param result: TUFLOW_results.ResData
		:return: bool -> True for successful, False for unsuccessful
		"""

		qv = Qgis.QGIS_VERSION_INT

		results = self.tuView.tuResults.results  # dict
		timekey2time = self.tuView.tuResults.timekey2time  # dict
		zeroTime = self.tuView.tuOptions.zeroTime  # datetime

		if result.displayname not in results.keys():
			results[result.displayname] = {}

		if self.tuView.OpenResults.count() == 0:
			self.tuView.tuOptions.zeroTime = datetime2timespec(self.getReferenceTime(result, defaultZeroTime=zeroTime),
			                                                   1, self.tuView.tuResults.timeSpec)
			if qv >= 31300:
				if self.iface is not None:
					self.tuView.tuOptions.timeSpec = self.iface.mapCanvas().temporalRange().begin().timeSpec()
					self.tuView.tuResults.loadedTimeSpec = self.iface.mapCanvas().temporalRange().begin().timeSpec()
				else:
					self.tuView.tuOptions.timeSpec = 1
					self.tuView.tuResults.loadedTimeSpec = 1
		self.configTemporalProperties(result)

		timesteps = result.timeSteps()
		for t in timesteps:
			timekey2time['{0:.6f}'.format(t)] = t
		results[result.displayname]['point_ts'] = {'times': {'{0:.6f}'.format(x): [x] for x in timesteps},
		                                           'referenceTime': result.reference_time,
		                                           'hasMax': hasMax}
		results[result.displayname]['line_ts'] = {'times': {'{0:.6f}'.format(x): [x] for x in timesteps},
		                                          'referenceTime': result.reference_time,
		                                          'hasMax': hasMax}
		results[result.displayname]['region_ts'] = {'times': {'{0:.6f}'.format(x): [x] for x in timesteps},
		                                            'referenceTime': result.reference_time,
		                                            'hasMax': hasMax}
		results[result.displayname]['line_lp'] = {'times': {'{0:.6f}'.format(x): [x] for x in timesteps},
		                                          'referenceTime': result.reference_time,
		                                          'hasMax': hasMax}

		resultTypes = result.pointResultTypesTS()
		metadata1d = [resultTypes]
		results[result.displayname]['point_ts']['metadata'] = metadata1d

		# if 'line_ts' not in results[result.displayname].keys():
		resultTypes = result.lineResultTypesTS()
		if 'Velocity' in resultTypes and 'Velocity' in result.pointResultTypesTS():
			resultTypes.remove('Velocity')
		metadata1d = [resultTypes]
		results[result.displayname]['line_ts']['metadata'] = metadata1d

		# if 'region_ts' not in results[result.displayname].keys():
		resultTypes = result.regionResultTypesTS()
		metadata1d = [resultTypes]
		results[result.displayname]['region_ts']['metadata'] = metadata1d

		# if 'line_lp' not in results[result.displayname].keys():
		resultTypes = result.lineResultTypesLP()
		metadata1d = [resultTypes]
		results[result.displayname]['line_lp']['metadata'] = metadata1d

		return True
	
	def updateSelectedResults(self, layer):
		"""
		Updates selected 1D elements and 1D result class.
		
		:param layer: QgsVectorLayer
		:return: bool -> True for successful, False for unsuccessful
		"""

		# reset variables
		self.ids = []
		self.domains = []
		self.sources = []
		
		resVersion = []
		for result in self.tuView.OpenResults.selectedItems():
			if result.text() in self.tuView.tuResults.tuResults1D.results1d.keys():
				resVersion.append(self.tuView.tuResults.tuResults1D.results1d[result.text()].formatVersion)
		
		# collect ids and domain types
		for layerid, layer in QgsProject.instance().mapLayers().items():
			if not isPlotLayer(layer):
				continue
			for f in layer.selectedFeatures():
				if 1 not in resVersion:
					if 'ID' in f.fields().names() and 'Type' in f.fields().names() and 'Source' in f.fields().names():
						self.ids.append(f['ID'].strip())
						self.sources.append(f['Source'].strip())
						type = f['Type'].strip()
						if 'node' in type.lower() or 'chan' in type.lower():
							self.domains.append('1D')
						else:
							self.domains.append(type)  # 2D or RL
				elif 2 not in resVersion:
					id = f.attributes()[0]
					id = id.strip()
					self.ids.append(id)
					self.domains.append('1D')
				else:  # try both
					if 'ID' in f.fields().names() and 'Type' in f.fields().names() and 'Source' in f.fields().names():
						self.ids.append(f['ID'].strip())
						self.sources.append(f['Source'].strip())
						type = f['Type'].strip()
						if 'node' in type.lower() or 'chan' in type.lower():
							self.domains.append('1D')
						else:
							self.domains.append(type)  # 2D or RL
					else:
						id = f.attributes()[0]
						id = id.strip()
						self.ids.append(id)
						self.domains.append('1D')
					
		return True
	
	def getLongPlotConnectivity(self, res):
		"""
		Check and collect the 1D long profile connectivity.

		:param res: TUFLOW_results or TUFLOW_results2013
		:return: bool -> True if error has occured
		"""

		# make sure there is between 1 and 2 selections
		# if len(self.ids) < 3 and self.ids:
		if self.ids:
			res.LP.connected = False
			res.LP.static = False
			error = False
			
			# one selection
			if len(self.ids) == 1:
				if res.formatVersion == 1:  # 2013 version only supports 1D
					error, message = res.LP_getConnectivity(self.ids[0], None, *self.ids)
				elif res.formatVersion == 2:
					if self.domains[0] == '1D':
						error, message = res.LP_getConnectivity(self.ids[0], None, *self.ids)
			
			# two selections
			elif len(self.ids) == 2:
				if res.formatVersion == 1:
					error, message = res.LP_getConnectivity(self.ids[0], self.ids[1], *self.ids)
				elif res.formatVersion == 2:
					if self.domains[0] == '1D' and self.domains[1] == '1D':
						error, message = res.LP_getConnectivity(self.ids[0], self.ids[1], *self.ids)

			# more than 2 selections
			else:
				if res.formatVersion == 2:
					error, message = res.LP_getConnectivity(None, None, *self.ids)  # flood modeller only
			
			# if error -> break
			if not error:
				error, message = res.LP_getStaticData()
				if not error:
					return False
		
		return True
	
	def removeResults(self, resList):
		"""
		Removes the 1D results from the indexed results and ui.

		:param resList: list -> str result name e.g. M01_5m_001
		:return: bool -> True for successful, False for unsuccessful
		"""

		results = self.tuView.tuResults.results

		for res in resList:
			self.tuView.crossSectionsFM.delByLayername(res)
		
		for res in resList:
			if res in results.keys():
				# remove from indexed results
				for resultType in list(results[res].keys()):
					if '_ts' in resultType or '_lp' in resultType:
						del results[res][resultType]
				
				# check if result type is now empty
				if len(results[res]) == 0:
					del results[res]
							
			if res in self.results1d:
				del self.results1d[res]
			
			for i in range(self.tuView.OpenResults.count()):
				item = self.tuView.OpenResults.item(i)
				if item is not None and item.text() == res:
					if res not in results:
						self.tuView.OpenResults.takeItem(i)
		
		return True

	def getReferenceTime(self, result, defaultZeroTime=None):
		"""

		"""

		qv = Qgis.QGIS_VERSION_INT

		rt = result.reference_time  # assume timespec 1

		if rt is not None:
			return rt
		else:
			if defaultZeroTime is not None:
				return defaultZeroTime
			else:
				if qv >= 31600:
					return self.tuView.tuOptions.zeroTime
				else:
					return datetime2timespec(self.tuView.tuOptions.zeroTime, self.tuView.tuResults.loadedTimeSpec, 1)

	def configTemporalProperties(self, result):
		"""

		"""
		qv = Qgis.QGIS_VERSION_INT

		if qv >= 31300:
			if not result.has_reference_time or self.tuView.tuResults.loadedTimeSpec != self.tuView.tuResults.timeSpec:
				#result.reference_time = datetime2timespec(self.getReferenceTime(result),
				#                                          self.tuView.tuResults.timeSpec,
				#                                          self.tuView.tuResults.loadedTimeSpec)
				result.reference_time = self.getReferenceTime(result)

	def reloadTimesteps(self, resname):
		"""

		"""

		if resname in self.results1d:
			result = self.results1d[resname]
			if not result.has_reference_time:
				result.reference_time = datetime2timespec(self.tuView.tuOptions.zeroTime, self.tuView.tuResults.loadedTimeSpec, 1)
			self.getResultMetaData(result)