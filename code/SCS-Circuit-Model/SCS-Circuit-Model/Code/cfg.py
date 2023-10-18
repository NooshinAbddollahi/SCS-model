'''
This is the cfg.py file for the SCS Circuit by L Medlock (Sept 16 2021)
'''
from netpyne import specs
from neuron import h
import sys
# sys.path.insert(0, 'cells')  # adding path to cells dir

cfg = specs.SimConfig()	# object of class SimConfig to store simulation configuration

###############################################################################
# SIMULATION PARAMETERS
###############################################################################
cfg.duration = 5000         # Duration of the simulation, in ms
cfg.dt = 0.025                 # Internal integration timestep to use
cfg.hParams = {'celsius': 23,'v_init': -70.0}
#cfg.vrest = cfg.hParams['v_init']
cfg.filename = 'SCS'        # Set file output names
cfg.printPopAvgRates = [ 0, 5000 ]

# Set recording traces
cfg.recordTraces['voltage'] = {'var': 'm'}
#cfg.recordTraces['mvar'] = {'var': 'm'}
#cfg.recordTraces['gGABA'] = {'sec':'soma','loc':0.5,'synMech':'inh','var':'g','index':0}
#cfg.recordTraces['iGABA1'] = {'sec':'soma','loc':0.5,'synMech':'GABA','var':'i', 'index':1}
#cfg.recordTraces['iGABA2'] = {'sec':'soma','loc':0.5,'synMech':'GABA','var':'i', 'index':2}
# cfg.recordTraces['iAMPA0'] = {'sec':'soma','loc':0.5,'synMech':'AMPA','var':'i', 'index':0}
# cfg.recordTraces['iAMPA1'] = {'sec':'soma','loc':0.5,'synMech':'AMPA','var':'i', 'index':1}
cfg.recordStep = 0.1                      

# Save and display data
#cfg.simLabel = 'model'
cfg.saveFolder = 'data'
cfg.saveJson = True
#cfg.saveMat = True
cfg.saveDataInclude = ['simData', 'simConfig', 'netParams','netCells', 'netPops']

cfg.analysis['plotTraces'] = {'include':[0,10],'ylim':[-100,50],'timeRange':[440,500],'oneFigPer':'trace', 'figSize':(8, 8), 'saveFig':True} #    'timeRange':[975,1025]
cfg.analysis['plotRaster'] = {'include':[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],'timeRange':[0,5000],'figSize':(8, 8), 'saveFig': True, 'showFig': True}
# cfg.analysis['plot2Dnet'] = {'showConns': True, 'saveFig': True}
# cfg.analysis['plotSpikeHist'] = {'include':['PAN'],'timeRange':[0,cfg.duration], 'binSize': 100, 'graphType':'bar','saveFig': True}
# cfg.analysis['plotShape'] = {'includePre':['50Hz'], 'includePost':['E_delay'],'showSyns': True, 'saveFig': True}
# cfg.analysis['plotConn'] = {'groupBy':'pop','saveFig': True}








		



