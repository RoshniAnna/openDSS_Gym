"""
In this file the sectionalizing and tie switch details are specified. 
Also the path for the DSS file containing the circuit information is specified.
The final DSS circuit which will be used by the environment is created.
"""

import os
import networkx as nx
from  DSS_CircuitSetup import*
sectional_swt=[{'no':1,'line':'632670'},
               {'no':2,'line':'671692'}]

tie_swt=[{'no':1,'from node':'646','from conn':'.3.2', 'to node':'684','to conn':'.3.1', 'length':2000,'code':'601'},
         {'no':2,'from node':'633','from conn':'.1.2.3','to node':'692','to conn':'.1.2.3','length':2000,'code':'601'}]

def initialize():       
    FolderName=os.path.dirname(os.path.realpath("__file__"))
    DSSfile=r""+ FolderName+ "\IEEE13Nodeckt.dss"
    DSSCktobj=CktModSetup(DSSfile,sectional_swt,tie_swt) # initially the sectionalizing switches close and tie switches open
    DSSCktobj.dssSolution.Solve() #solving snapshot power flows
    G_init=graph_struct(DSSCktobj)
    return DSSCktobj,G_init
