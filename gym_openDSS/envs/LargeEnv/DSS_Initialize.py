"""
In this file the sectionalizing and tie switch details are specified. 
Also the path for the DSS file containing the circuit information is specified.
The final DSS circuit which will be used by the environment is created.
"""

import os
import networkx as nx
from  DSS_CircuitSetup import*
sectional_swt=[{'no':1,'line':'L19'},
               {'no':2,'line':'L24'},
               {'no':3,'line':'L26'},
               {'no':4,'line':'L43'},
               {'no':5,'line':'L58'},
               {'no':6,'line':'L67'},
               {'no':7,'line':'L81'},
               {'no':8,'line':'L86'},
               {'no':9,'line':'L101'},
               {'no':10,'line':'sw2'},
               {'no':11,'line':'sw3'},
               {'no':12,'line':'sw4'},
               {'no':13,'line':'sw5'},
               {'no':14,'line':'sw8'},
               {'no':15,'line':'sw7'}]

# tie_swt=[{'no':1,'from node':'56','from conn':'.1.2.3', 'to node':'92','to conn':'.1.2.3', 'length':0.350,'code':'6', 'name':'118'},
#          {'no':2,'from node':'83','from conn':'.1.2.3', 'to node':'95','to conn':'.1.2.3', 'length':1.975,'code':'2', 'name':'119'},
#          {'no':3,'from node':'25','from conn':'.1.2.3', 'to node':'35','to conn':'.1.2.3', 'length':0.906,'code':'2', 'name':'120'},
#          {'no':4,'from node':'250','from conn':'.1.2.3', 'to node':'300','to conn':'.1.2.3', 'length':1.364,'code':'3', 'name':'121'},
#          {'no':5,'from node':'51','from conn':'.1.2.3', 'to node':'65','to conn':'.1.2.3', 'length':0.600,'code':'4', 'name':'122'},
#          {'no':6,'from node':'101','from conn':'.1.2.3', 'to node':'151','to conn':'.1.2.3', 'length':1.600,'code':'3', 'name':'123'},
#          {'no':7,'from node':'79','from conn':'.1.2.3', 'to node':'450','to conn':'.1.2.3', 'length':1.304,'code':'5', 'name':'124'}]

tie_swt=[{'no':1,'from node':'56','from conn':'.1.2.3', 'to node':'92','to conn':'.1.2.3', 'length':0.350,'code':'6', 'name':'118'},
         {'no':2,'from node':'56','from conn':'.1.2.3', 'to node':'92','to conn':'.1.2.3', 'length':0.350,'code':'6', 'name':'118'},
    {'no':3,'from node':'56','from conn':'.1.2.3', 'to node':'92','to conn':'.1.2.3', 'length':0.350,'code':'6', 'name':'118'},
          {'no':2,'from node':'83','from conn':'.1.2.3', 'to node':'95','to conn':'.1.2.3', 'length':1.975,'code':'2', 'name':'119'},
          {'no':3,'from node':'25','from conn':'.1.2.3', 'to node':'35','to conn':'.1.2.3', 'length':0.906,'code':'2', 'name':'120'},
          {'no':4,'from node':'250','from conn':'.1.2.3', 'to node':'300','to conn':'.1.2.3', 'length':1.364,'code':'3', 'name':'121'},
          {'no':5,'from node':'51','from conn':'.1.2.3', 'to node':'65','to conn':'.1.2.3', 'length':0.600,'code':'4', 'name':'122'},
          {'no':6,'from node':'101','from conn':'.1.2.3', 'to node':'151','to conn':'.1.2.3', 'length':1.600,'code':'3', 'name':'123'},
          {'no':7,'from node':'79','from conn':'.1.2.3', 'to node':'450','to conn':'.1.2.3', 'length':1.304,'code':'5', 'name':'124'}]

def initialize():       
    FolderName=os.path.dirname(os.path.realpath("__file__"))
    DSSfile=r""+ FolderName+ "\IEEE123Master.dss"
    DSSCktobj=CktModSetup(DSSfile,sectional_swt,tie_swt) # initially the sectionalizing switches close and tie switches open
    DSSCktobj.dssSolution.Solve() #solving snapshot power flows
    if DSSCktobj.dssSolution.Converged:
       conv_flag=1
    else:
       conv_flag=0
    G_init=graph_struct(DSSCktobj)
    return DSSCktobj,G_init,conv_flag
