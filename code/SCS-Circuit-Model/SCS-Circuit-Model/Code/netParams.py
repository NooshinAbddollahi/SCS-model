'''
This is the netParams.py file for the SCS Model by L Medlock
'''

from netpyne import specs, sim
from neuron import h, gui
import numpy as np
import json

try:
    from __main__ import cfg
except:
    from cfg import cfg

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters
netParams.defaultThreshold = -25

# Weights for network
netParams.ItoE_weight = -80
netParams.PANtoE_weight = 120
netParams.PANtoI_weight = 120

###############################################################################
# CELL PARAMETERS
###############################################################################
# Cell Model:
netParams.cellParams['TestCell'] = {
        'secs': {'soma':{'geom': {'diam': 10, 'L': 100, 'Ra': 100.0}}}
}

###############################################################################
# POPULATION PARAMETERS
###############################################################################
## Integrate & Fire Models:
# Excitatory Neurons (n=10)
# tau values: [14.1363   15.0774   13.7859   13.8865   14.9932   16.5326   14.2303   15.3714   14.7744   16.1174]
netParams.popParams['ECell1'] = {'cellType':'TestCell','cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':14.1363, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 0
netParams.popParams['ECell2'] = {'cellType':'TestCell','cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':15.0774, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 1
netParams.popParams['ECell3'] = {'cellType':'TestCell','cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':13.7859, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 2
netParams.popParams['ECell4'] = {'cellType':'TestCell','cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':13.8865, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 3
netParams.popParams['ECell5'] = {'cellType':'TestCell','cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':14.9932, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 4
netParams.popParams['ECell6'] = {'cellType':'TestCell','cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':16.5326, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 5
netParams.popParams['ECell7'] = {'cellType':'TestCell','cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':14.2303, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 6
netParams.popParams['ECell8'] = {'cellType':'TestCell','cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':15.3714, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 7
netParams.popParams['ECell9'] = {'cellType':'TestCell','cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':14.7744, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 8
netParams.popParams['ECell10'] = {'cellType':'TestCell','cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':16.1174, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 9

# Inhibitory Neurons (n=10) 
# tau values: [10.5377   11.8339    7.7412   10.8622   10.3188    8.6923    9.5664   10.3426   13.5784   12.7694]
netParams.popParams['ICell1'] = {'cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':10.5377, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 10
netParams.popParams['ICell2'] = {'cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':11.8339, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 11
netParams.popParams['ICell3'] = {'cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':7.7412, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 12
netParams.popParams['ICell4'] = {'cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':10.8622, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 13
netParams.popParams['ICell5'] = {'cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':10.3188, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 14
netParams.popParams['ICell6'] = {'cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':8.6923, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 15
netParams.popParams['ICell7'] = {'cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':9.5664, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 16
netParams.popParams['ICell8'] = {'cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':10.3426, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 17
netParams.popParams['ICell9'] = {'cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':13.5784, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 18
netParams.popParams['ICell10'] = {'cellModel': 'LeakyIntFire', 'numCells': 1, 'm':-65, 'Iext': 0, 'taum':12.7694, 'Cm':50, 'tauref':0.1, 'tausyn': 3}  # GID = 19

# Synchronous Input (Expt - 50Hz)
# with open('SCS_sync_input_50Hz.json', 'rb') as sync_spkt: sync_spkt = json.load(sync_spkt)
# netParams.popParams['50Hz'] = {'cellModel': 'VecStim', 'numCells': 10, 'spkTimes': sync_spkt}  # GID = 11:20
# # Asynchronous Input (Expt - 1kHz) -- Remove comments from lines below to run async input
with open('SCS_async_input_1kHz.json', 'rb') as async_spkt: async_spkt = json.load(async_spkt)
netParams.popParams['1kHz'] = {'cellModel': 'VecStim', 'numCells': 10, 'spkTimes': async_spkt}  # GID = 11:20

# # Noise input
netParams.popParams['Noise1_E'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise2_E'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise3_E'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise4_E'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise5_E'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise6_E'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise7_E'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise8_E'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise9_E'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise10_E'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}

netParams.popParams['Noise1_I'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise2_I'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise3_I'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise4_I'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise5_I'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise6_I'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise7_I'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise8_I'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise9_I'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}
netParams.popParams['Noise10_I'] = {'numCells': 100, 'cellModel': 'NetStim', 'rate': 100,  'start':0.0, 'noise': 1, 'delay':0}

###############################################################################
# SYNAPTIC PARAMETERS
###############################################################################
# netParams.synMechParams['exc'] = {'mod': 'ExpSyn', 'tau': 5.0, 'e': 0}  
# netParams.synMechParams['inh'] = {'mod': 'ExpSyn', 'tau': 10.0, 'e': -85}   

###############################################################################
# CONNECTIVITY PARAMETERS
###############################################################################

##-----------------------Noise Connections -----------------------### 
netParams.connParams['Noise1_E->ECell1'] = {    
    'preConds': {'pop': 'Noise1_E'}, 
    'postConds': {'pop': 'ECell1'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
}  

netParams.connParams['Noise2_E->ECell2'] = {    
    'preConds': {'pop': 'Noise2_E'}, 
    'postConds': {'pop': 'ECell2'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
}  

netParams.connParams['Noise3_E->ECell3'] = {    
    'preConds': {'pop': 'Noise3_E'}, 
    'postConds': {'pop': 'ECell3'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
}  

netParams.connParams['Noise4_E->ECell4'] = {    
    'preConds': {'pop': 'Noise4_E'}, 
    'postConds': {'pop': 'ECell4'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
}  

netParams.connParams['Noise5_E->ECell5'] = {    
    'preConds': {'pop': 'Noise5_E'}, 
    'postConds': {'pop': 'ECell5'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
}  

netParams.connParams['Noise6_E->ECell6'] = {    
    'preConds': {'pop': 'Noise6_E'}, 
    'postConds': {'pop': 'ECell6'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
}  

netParams.connParams['Noise7_E->ECell7'] = {    
    'preConds': {'pop': 'Noise7_E'}, 
    'postConds': {'pop': 'ECell7'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
}  

netParams.connParams['Noise8_E->ECell8'] = {    
    'preConds': {'pop': 'Noise8_E'}, 
    'postConds': {'pop': 'ECell8'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
}  

netParams.connParams['Noise9_E->ECell9'] = {    
    'preConds': {'pop': 'Noise9_E'}, 
    'postConds': {'pop': 'ECell9'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
}  

netParams.connParams['Noise10_E->ECell10'] = {    
    'preConds': {'pop': 'Noise10_E'}, 
    'postConds': {'pop': 'ECell10'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
}  

netParams.connParams['Noise1_I->ICell1'] = {    
    'preConds': {'pop': 'Noise1_I'}, 
    'postConds': {'pop': 'ICell1'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
} 

netParams.connParams['Noise2_I->ICell2'] = {    
    'preConds': {'pop': 'Noise2_I'}, 
    'postConds': {'pop': 'ICell2'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
} 

netParams.connParams['Noise3_I->ICell3'] = {    
    'preConds': {'pop': 'Noise3_I'}, 
    'postConds': {'pop': 'ICell3'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
} 

netParams.connParams['Noise4_I->ICell4'] = {    
    'preConds': {'pop': 'Noise4_I'}, 
    'postConds': {'pop': 'ICell4'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
} 

netParams.connParams['Noise5_I->ICell5'] = {    
    'preConds': {'pop': 'Noise5_I'}, 
    'postConds': {'pop': 'ICell5'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
} 

netParams.connParams['Noise6_I->ICell6'] = {    
    'preConds': {'pop': 'Noise6_I'}, 
    'postConds': {'pop': 'ICell6'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
} 

netParams.connParams['Noise7_I->ICell7'] = {    
    'preConds': {'pop': 'Noise7_I'}, 
    'postConds': {'pop': 'ICell7'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
} 

netParams.connParams['Noise8_I->ICell8'] = {    
    'preConds': {'pop': 'Noise8_I'}, 
    'postConds': {'pop': 'ICell8'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
} 

netParams.connParams['Noise9_I->ICell9'] = {    
    'preConds': {'pop': 'Noise9_I'}, 
    'postConds': {'pop': 'ICell9'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
} 

netParams.connParams['Noise10_I->ICell10'] = {    
    'preConds': {'pop': 'Noise10_I'}, 
    'postConds': {'pop': 'ICell10'},  
    'probability': 1,            # probability of connection
    'weight': 1,                 # synaptic weight  
    'delay': 0                   # transmission delay (ms)
} 

# # # # # ###------------------------INPUT2ECell Connections -------------------###

netParams.connParams['PAN->ECell1'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ECell1'},  
    'probability': 1,               # probability of connection
    'weight': netParams.PANtoE_weight,                  # synaptic weight
    'delay': 0                      # transmission delay (ms)
 }     
netParams.connParams['PAN->ECell2'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ECell2'},  
    'probability': 1,               # probability of connection
    'weight': netParams.PANtoE_weight,                  # synaptic weight
    'delay': 0                      # transmission delay (ms)
 }  
netParams.connParams['PAN->ECell3'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ECell3'},  
    'probability': 1,               # probability of connection
    'weight': netParams.PANtoE_weight,                  # synaptic weight
    'delay': 0                      # transmission delay (ms)
 }  
netParams.connParams['PAN->ECell4'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ECell4'},  
    'probability': 1,               # probability of connection
    'weight': netParams.PANtoE_weight,                  # synaptic weight
    'delay': 0                      # transmission delay (ms)
 }  
netParams.connParams['PAN->ECell5'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ECell5'},  
    'probability': 1,               # probability of connection
    'weight': netParams.PANtoE_weight,                  # synaptic weight
    'delay': 0                      # transmission delay (ms)
 }  
netParams.connParams['PAN->ECell6'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ECell6'},  
    'probability': 1,               # probability of connection
    'weight': netParams.PANtoE_weight,                  # synaptic weight
    'delay': 0                      # transmission delay (ms)
 }  
netParams.connParams['PAN->ECell7'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ECell7'},  
    'probability': 1,               # probability of connection
    'weight': netParams.PANtoE_weight,                  # synaptic weight
    'delay': 0                      # transmission delay (ms)
 }  
netParams.connParams['PAN->ECell8'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ECell8'},  
    'probability': 1,               # probability of connection
    'weight': netParams.PANtoE_weight,                  # synaptic weight
    'delay': 0                      # transmission delay (ms)
 }  
netParams.connParams['PAN->ECell9'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ECell9'},  
    'probability': 1,               # probability of connection
    'weight': netParams.PANtoE_weight,                  # synaptic weight
    'delay': 0                      # transmission delay (ms)
 }  
netParams.connParams['PAN->ECell10'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ECell10'},  
    'probability': 1,               # probability of connection
    'weight': netParams.PANtoE_weight,                  # synaptic weight
    'delay': 0                      # transmission delay (ms)
 }           

###------------------------PAN2ECell Connections -------------------###
netParams.connParams['PAN->ICell1'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ICell1'},  
    'probability': 1,                 # probability of connection
    'weight': netParams.PANtoI_weight,                   # synaptic weight
    'delay': 0                        # transmission delay (ms)
 }      

netParams.connParams['PAN->ICell2'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ICell2'},  
    'probability': 1,                 # probability of connection
    'weight': netParams.PANtoI_weight,                   # synaptic weight
    'delay': 0                        # transmission delay (ms)
 }        

netParams.connParams['PAN->ICell3'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ICell3'},  
    'probability': 1,                 # probability of connection
    'weight': netParams.PANtoI_weight,                   # synaptic weight
    'delay': 0                        # transmission delay (ms)
 }   

netParams.connParams['PAN->ICell4'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ICell4'},  
    'probability': 1,                 # probability of connection
    'weight': netParams.PANtoI_weight,                   # synaptic weight
    'delay': 0                        # transmission delay (ms)
 }   

netParams.connParams['PAN->ICell5'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ICell5'},  
    'probability': 1,                 # probability of connection
    'weight': netParams.PANtoI_weight,                   # synaptic weight
    'delay': 0                        # transmission delay (ms)
 }   

netParams.connParams['PAN->ICell6'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ICell6'},  
    'probability': 1,                 # probability of connection
    'weight': netParams.PANtoI_weight,                   # synaptic weight
    'delay': 0                        # transmission delay (ms)
 }   

netParams.connParams['PAN->ICell7'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ICell7'},  
    'probability': 1,                 # probability of connection
    'weight': netParams.PANtoI_weight,                   # synaptic weight
    'delay': 0                        # transmission delay (ms)
 }   

netParams.connParams['PAN->ICell8'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ICell8'},  
    'probability': 1,                 # probability of connection
    'weight': netParams.PANtoI_weight,                   # synaptic weight
    'delay': 0                        # transmission delay (ms)
 }   

netParams.connParams['PAN->ICell9'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ICell9'},  
    'probability': 1,                 # probability of connection
    'weight': netParams.PANtoI_weight,                    # synaptic weight
    'delay': 0                        # transmission delay (ms)
 }   

netParams.connParams['PAN->ICell10'] = {    
    'preConds': {'pop': '1kHz'}, 
    'postConds': {'pop': 'ICell10'},  
    'probability': 1,                 # probability of connection
    'weight': netParams.PANtoI_weight,                   # synaptic weight
    'delay': 0                        # transmission delay (ms)
 }   

# # # # ###-----------------------I2E Connections ------------------------###
netParams.connParams['ICell1->ECell1'] = {    
    'preConds': {'pop': 'ICell1'}, 
    'postConds': {'pop': 'ECell1'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell2->ECell1'] = {    
    'preConds': {'pop': 'ICell2'}, 
    'postConds': {'pop': 'ECell1'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell3->ECell1'] = {    
    'preConds': {'pop': 'ICell3'}, 
    'postConds': {'pop': 'ECell1'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                     # transmission delay (ms)
 } 

netParams.connParams['ICell4->ECell1'] = {    
    'preConds': {'pop': 'ICell4'}, 
    'postConds': {'pop': 'ECell1'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                   # transmission delay (ms)
}

netParams.connParams['ICell5->ECell1'] = {    
    'preConds': {'pop': 'ICell5'}, 
    'postConds': {'pop': 'ECell1'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell6->ECell1'] = {    
    'preConds': {'pop': 'ICell6'}, 
    'postConds': {'pop': 'ECell1'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                    # transmission delay (ms)
 } 

netParams.connParams['ICell7->ECell1'] = {    
    'preConds': {'pop': 'ICell7'}, 
    'postConds': {'pop': 'ECell1'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell8->ECell1'] = {    
    'preConds': {'pop': 'ICell8'}, 
    'postConds': {'pop': 'ECell1'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell9->ECell1'] = {    
    'preConds': {'pop': 'ICell9'}, 
    'postConds': {'pop': 'ECell1'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell10->ECell1'] = {    
    'preConds': {'pop': 'ICell10'}, 
    'postConds': {'pop': 'ECell1'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                  # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell1->ECell2'] = {    
    'preConds': {'pop': 'ICell1'}, 
    'postConds': {'pop': 'ECell2'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell2->ECell2'] = {    
    'preConds': {'pop': 'ICell2'}, 
    'postConds': {'pop': 'ECell2'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell3->ECell2'] = {    
    'preConds': {'pop': 'ICell3'}, 
    'postConds': {'pop': 'ECell2'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                     # transmission delay (ms)
 } 

netParams.connParams['ICell4->ECell2'] = {    
    'preConds': {'pop': 'ICell4'}, 
    'postConds': {'pop': 'ECell2'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                   # transmission delay (ms)
}

netParams.connParams['ICell5->ECell2'] = {    
    'preConds': {'pop': 'ICell5'}, 
    'postConds': {'pop': 'ECell2'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell6->ECell2'] = {    
    'preConds': {'pop': 'ICell6'}, 
    'postConds': {'pop': 'ECell2'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                    # transmission delay (ms)
 } 

netParams.connParams['ICell7->ECell2'] = {    
    'preConds': {'pop': 'ICell7'}, 
    'postConds': {'pop': 'ECell2'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell8->ECell2'] = {    
    'preConds': {'pop': 'ICell8'}, 
    'postConds': {'pop': 'ECell2'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell9->ECell2'] = {    
    'preConds': {'pop': 'ICell9'}, 
    'postConds': {'pop': 'ECell2'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell10->ECell2'] = {    
    'preConds': {'pop': 'ICell10'}, 
    'postConds': {'pop': 'ECell2'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                  # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell1->ECell3'] = {    
    'preConds': {'pop': 'ICell1'}, 
    'postConds': {'pop': 'ECell3'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell2->ECell3'] = {    
    'preConds': {'pop': 'ICell2'}, 
    'postConds': {'pop': 'ECell3'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell3->ECell3'] = {    
    'preConds': {'pop': 'ICell3'}, 
    'postConds': {'pop': 'ECell3'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                     # transmission delay (ms)
 } 

netParams.connParams['ICell4->ECell3'] = {    
    'preConds': {'pop': 'ICell4'}, 
    'postConds': {'pop': 'ECell3'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                   # transmission delay (ms)
}

netParams.connParams['ICell5->ECell3'] = {    
    'preConds': {'pop': 'ICell5'}, 
    'postConds': {'pop': 'ECell3'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell6->ECell3'] = {    
    'preConds': {'pop': 'ICell6'}, 
    'postConds': {'pop': 'ECell3'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                    # transmission delay (ms)
 } 

netParams.connParams['ICell7->ECell3'] = {    
    'preConds': {'pop': 'ICell7'}, 
    'postConds': {'pop': 'ECell3'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell8->ECell3'] = {    
    'preConds': {'pop': 'ICell8'}, 
    'postConds': {'pop': 'ECell3'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell9->ECell3'] = {    
    'preConds': {'pop': 'ICell9'}, 
    'postConds': {'pop': 'ECell3'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell10->ECell3'] = {    
    'preConds': {'pop': 'ICell10'}, 
    'postConds': {'pop': 'ECell3'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                  # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell1->ECell4'] = {    
    'preConds': {'pop': 'ICell1'}, 
    'postConds': {'pop': 'ECell4'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell2->ECell4'] = {    
    'preConds': {'pop': 'ICell2'}, 
    'postConds': {'pop': 'ECell4'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell3->ECell4'] = {    
    'preConds': {'pop': 'ICell3'}, 
    'postConds': {'pop': 'ECell4'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                     # transmission delay (ms)
 } 

netParams.connParams['ICell4->ECell4'] = {    
    'preConds': {'pop': 'ICell4'}, 
    'postConds': {'pop': 'ECell4'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                   # transmission delay (ms)
}

netParams.connParams['ICell5->ECell4'] = {    
    'preConds': {'pop': 'ICell5'}, 
    'postConds': {'pop': 'ECell4'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell6->ECell4'] = {    
    'preConds': {'pop': 'ICell6'}, 
    'postConds': {'pop': 'ECell4'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                    # transmission delay (ms)
 } 

netParams.connParams['ICell7->ECell4'] = {    
    'preConds': {'pop': 'ICell7'}, 
    'postConds': {'pop': 'ECell4'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell8->ECell4'] = {    
    'preConds': {'pop': 'ICell8'}, 
    'postConds': {'pop': 'ECell4'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell9->ECell4'] = {    
    'preConds': {'pop': 'ICell9'}, 
    'postConds': {'pop': 'ECell4'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell10->ECell4'] = {    
    'preConds': {'pop': 'ICell10'}, 
    'postConds': {'pop': 'ECell4'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                  # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell1->ECell5'] = {    
    'preConds': {'pop': 'ICell1'}, 
    'postConds': {'pop': 'ECell5'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell2->ECell5'] = {    
    'preConds': {'pop': 'ICell2'}, 
    'postConds': {'pop': 'ECell5'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell3->ECell5'] = {    
    'preConds': {'pop': 'ICell3'}, 
    'postConds': {'pop': 'ECell5'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                     # transmission delay (ms)
 } 

netParams.connParams['ICell4->ECell5'] = {    
    'preConds': {'pop': 'ICell4'}, 
    'postConds': {'pop': 'ECell5'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                   # transmission delay (ms)
}

netParams.connParams['ICell5->ECell5'] = {    
    'preConds': {'pop': 'ICell5'}, 
    'postConds': {'pop': 'ECell5'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell6->ECell5'] = {    
    'preConds': {'pop': 'ICell6'}, 
    'postConds': {'pop': 'ECell5'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                    # transmission delay (ms)
 } 

netParams.connParams['ICell7->ECell5'] = {    
    'preConds': {'pop': 'ICell7'}, 
    'postConds': {'pop': 'ECell5'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell8->ECell5'] = {    
    'preConds': {'pop': 'ICell8'}, 
    'postConds': {'pop': 'ECell5'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell9->ECell5'] = {    
    'preConds': {'pop': 'ICell9'}, 
    'postConds': {'pop': 'ECell5'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell10->ECell5'] = {    
    'preConds': {'pop': 'ICell10'}, 
    'postConds': {'pop': 'ECell5'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                  # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell1->ECell6'] = {    
    'preConds': {'pop': 'ICell1'}, 
    'postConds': {'pop': 'ECell6'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell2->ECell6'] = {    
    'preConds': {'pop': 'ICell2'}, 
    'postConds': {'pop': 'ECell6'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell3->ECell6'] = {    
    'preConds': {'pop': 'ICell3'}, 
    'postConds': {'pop': 'ECell6'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                     # transmission delay (ms)
 } 

netParams.connParams['ICell4->ECell6'] = {    
    'preConds': {'pop': 'ICell4'}, 
    'postConds': {'pop': 'ECell6'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                   # transmission delay (ms)
}

netParams.connParams['ICell5->ECell6'] = {    
    'preConds': {'pop': 'ICell5'}, 
    'postConds': {'pop': 'ECell6'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell6->ECell6'] = {    
    'preConds': {'pop': 'ICell6'}, 
    'postConds': {'pop': 'ECell6'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                    # transmission delay (ms)
 } 

netParams.connParams['ICell7->ECell6'] = {    
    'preConds': {'pop': 'ICell7'}, 
    'postConds': {'pop': 'ECell6'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell8->ECell6'] = {    
    'preConds': {'pop': 'ICell8'}, 
    'postConds': {'pop': 'ECell6'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell9->ECell6'] = {    
    'preConds': {'pop': 'ICell9'}, 
    'postConds': {'pop': 'ECell6'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell10->ECell6'] = {    
    'preConds': {'pop': 'ICell10'}, 
    'postConds': {'pop': 'ECell6'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                  # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell1->ECell7'] = {    
    'preConds': {'pop': 'ICell1'}, 
    'postConds': {'pop': 'ECell7'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell2->ECell7'] = {    
    'preConds': {'pop': 'ICell2'}, 
    'postConds': {'pop': 'ECell7'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell3->ECell7'] = {    
    'preConds': {'pop': 'ICell3'}, 
    'postConds': {'pop': 'ECell7'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                     # transmission delay (ms)
 } 

netParams.connParams['ICell4->ECell7'] = {    
    'preConds': {'pop': 'ICell4'}, 
    'postConds': {'pop': 'ECell7'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                   # transmission delay (ms)
}

netParams.connParams['ICell5->ECell7'] = {    
    'preConds': {'pop': 'ICell5'}, 
    'postConds': {'pop': 'ECell7'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell6->ECell7'] = {    
    'preConds': {'pop': 'ICell6'}, 
    'postConds': {'pop': 'ECell7'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                    # transmission delay (ms)
 } 

netParams.connParams['ICell7->ECell7'] = {    
    'preConds': {'pop': 'ICell7'}, 
    'postConds': {'pop': 'ECell7'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell8->ECell7'] = {    
    'preConds': {'pop': 'ICell8'}, 
    'postConds': {'pop': 'ECell7'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell9->ECell7'] = {    
    'preConds': {'pop': 'ICell9'}, 
    'postConds': {'pop': 'ECell7'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell10->ECell7'] = {    
    'preConds': {'pop': 'ICell10'}, 
    'postConds': {'pop': 'ECell7'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                  # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell1->ECell8'] = {    
    'preConds': {'pop': 'ICell1'}, 
    'postConds': {'pop': 'ECell8'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell2->ECell8'] = {    
    'preConds': {'pop': 'ICell2'}, 
    'postConds': {'pop': 'ECell8'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell3->ECell8'] = {    
    'preConds': {'pop': 'ICell3'}, 
    'postConds': {'pop': 'ECell8'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                     # transmission delay (ms)
 } 

netParams.connParams['ICell4->ECell8'] = {    
    'preConds': {'pop': 'ICell4'}, 
    'postConds': {'pop': 'ECell8'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                   # transmission delay (ms)
}

netParams.connParams['ICell5->ECell8'] = {    
    'preConds': {'pop': 'ICell5'}, 
    'postConds': {'pop': 'ECell8'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell6->ECell8'] = {    
    'preConds': {'pop': 'ICell6'}, 
    'postConds': {'pop': 'ECell8'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                    # transmission delay (ms)
 } 

netParams.connParams['ICell7->ECell8'] = {    
    'preConds': {'pop': 'ICell7'}, 
    'postConds': {'pop': 'ECell8'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell8->ECell8'] = {    
    'preConds': {'pop': 'ICell8'}, 
    'postConds': {'pop': 'ECell8'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell9->ECell8'] = {    
    'preConds': {'pop': 'ICell9'}, 
    'postConds': {'pop': 'ECell8'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell10->ECell8'] = {    
    'preConds': {'pop': 'ICell10'}, 
    'postConds': {'pop': 'ECell8'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                  # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell1->ECell9'] = {    
    'preConds': {'pop': 'ICell1'}, 
    'postConds': {'pop': 'ECell9'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell2->ECell9'] = {    
    'preConds': {'pop': 'ICell2'}, 
    'postConds': {'pop': 'ECell9'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell3->ECell9'] = {    
    'preConds': {'pop': 'ICell3'}, 
    'postConds': {'pop': 'ECell9'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                     # transmission delay (ms)
 } 

netParams.connParams['ICell4->ECell9'] = {    
    'preConds': {'pop': 'ICell4'}, 
    'postConds': {'pop': 'ECell9'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                   # transmission delay (ms)
}

netParams.connParams['ICell5->ECell9'] = {    
    'preConds': {'pop': 'ICell5'}, 
    'postConds': {'pop': 'ECell9'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell6->ECell9'] = {    
    'preConds': {'pop': 'ICell6'}, 
    'postConds': {'pop': 'ECell9'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                    # transmission delay (ms)
 } 

netParams.connParams['ICell7->ECell9'] = {    
    'preConds': {'pop': 'ICell7'}, 
    'postConds': {'pop': 'ECell9'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell8->ECell9'] = {    
    'preConds': {'pop': 'ICell8'}, 
    'postConds': {'pop': 'ECell9'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell9->ECell9'] = {    
    'preConds': {'pop': 'ICell9'}, 
    'postConds': {'pop': 'ECell9'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell10->ECell9'] = {    
    'preConds': {'pop': 'ICell10'}, 
    'postConds': {'pop': 'ECell9'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                  # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell1->ECell10'] = {    
    'preConds': {'pop': 'ICell1'}, 
    'postConds': {'pop': 'ECell10'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell2->ECell10'] = {    
    'preConds': {'pop': 'ICell2'}, 
    'postConds': {'pop': 'ECell10'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

netParams.connParams['ICell3->ECell10'] = {    
    'preConds': {'pop': 'ICell3'}, 
    'postConds': {'pop': 'ECell10'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                     # transmission delay (ms)
 } 

netParams.connParams['ICell4->ECell10'] = {    
    'preConds': {'pop': 'ICell4'}, 
    'postConds': {'pop': 'ECell10'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                   # synaptic weight  
    'delay': 2                   # transmission delay (ms)
}

netParams.connParams['ICell5->ECell10'] = {    
    'preConds': {'pop': 'ICell5'}, 
    'postConds': {'pop': 'ECell10'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell6->ECell10'] = {    
    'preConds': {'pop': 'ICell6'}, 
    'postConds': {'pop': 'ECell10'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                    # transmission delay (ms)
 } 

netParams.connParams['ICell7->ECell10'] = {    
    'preConds': {'pop': 'ICell7'}, 
    'postConds': {'pop': 'ECell10'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell8->ECell10'] = {    
    'preConds': {'pop': 'ICell8'}, 
    'postConds': {'pop': 'ECell10'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                  # transmission delay (ms)
 } 

netParams.connParams['ICell9->ECell10'] = {    
    'preConds': {'pop': 'ICell9'}, 
    'postConds': {'pop': 'ECell10'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                # synaptic weight  
    'delay': 2                   # transmission delay (ms)
 } 

netParams.connParams['ICell10->ECell10'] = {    
    'preConds': {'pop': 'ICell10'}, 
    'postConds': {'pop': 'ECell10'},  
    'probability': 1,               # probability of connection
    'weight':netParams.ItoE_weight,                  # synaptic weight  
    'delay': 2                      # transmission delay (ms)
 } 

# # ###############################################################################
# # # STIMULATION PARAMETERS
# # ###############################################################################

# # ## Stim Source ##

# # netParams.stimSourceParams['IClamp1'] = {'type': 'IClamp', 'del': 2000, 'dur': 1000, 'amp': -100}
# # # Noise (Poisson Stimulation)
# # netParams.stimSourceParams['Noise'] = {'type': 'NetStim', 'rate': 100, 'noise': 0.4, 'start': 0}
# # netParams.stimSourceParams['Noise_E'] = {'type': 'NetStim', 'rate': 100, 'noise': 0.4, 'start': 0}

# # # # ## Stim Target ##
# # netParams.stimTargetParams['IClamp->ECell'] = {'source': 'IClamp1',  # Noise to I_tonic 1
# #                                               'conds': {'pop':'ECell'},
# #                                               'delay': 0 }

# # netParams.stimTargetParams['Noise->ECell'] = {'source': 'Noise',  # Noise to I_tonic 1
# #                                                   'conds': {'pop':'ECell'},
# #                                                   'weight': 1,
# #                                                   'delay': 0 }


