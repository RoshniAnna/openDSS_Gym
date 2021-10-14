
"""
In this file I define the functions to evaluate the state, reward and also implement the action
"""
import win32com.client
import numpy as np
import networkx as nx
from  DSS_CircuitSetup import*

def get_state(DSSCktobj):
    #Input: object of type DSSObj.ActiveCircuit (COM interface for OpenDSS Circuit)
    #Returns: dictionary of circuit loss, bus voltage, branch powerflow, radiality of network
    G=graph_struct(DSSCktobj) 
    node_list=list(G.nodes())
    Adj_mat=nx.adjacency_matrix(G,nodelist=node_list)
    
    DSSCktobj.dssTransformers.First
    KVA_base=DSSCktobj.dssTransformers.kva
    P_loss=(DSSCktobj.dssCircuit.Losses[0])/(1000*KVA_base)
    Q_loss=(DSSCktobj.dssCircuit.Losses[1])/(1000*KVA_base)


    Vmagpu=[]
    for b in node_list:
        V=Bus(DSSCktobj,b).Vmag
        Vmagpu.append(V)
               
    I_flow=[]
    for e in G.edges(data=True):
        branchname=e[2]['label']
        I=Branch(DSSCktobj, branchname).Cap
        I_flow.append(I)

    
    return {"loss":P_loss,"NodeFeat(BusVoltage)":np.array(Vmagpu), "EdgeFeat(branchflow)":np.array(I_flow),"Adjacency":np.array(Adj_mat.todense())}


    
def take_action(DSSCktobj,action):
    #Input :object of type DSSObj.ActiveCircuit (COM interface for OpenDSS Circuit)
    #Input: action multi binary type. i.e., the status of each switch if it is 0 open and 1 close
    #Returns:the circuit object with action implemented
    DSSCircuit=DSSCktobj.dssCircuit
    i=DSSCircuit.SwtControls.First #1
    # while (i>0): This will also work
    #       Swname=DSSCircuit.SwtControls.Name
    #       if action[i-1]==0: # i starts from 1 in DSS #if action is 0 
    #         DSSCktobj.dssText.command='Edit swtcontrol.' + Swname  + ' State=Open' #switching the line open
    #       else:
    #         DSSCktobj.dssText.command='Edit swtcontrol.' + Swname  + ' State=Close' #switching the line close
    #       i=DSSCircuit.SwtControls.Next   
    while (i>0):
           Swobj=DSSCktobj.dssCircuit.SwtControls.SwitchedObj
           DSSCircuit.SetActiveElement(Swobj)
           if action[i-1]==0: # i starts from 1 in DSS #if action is 0 
               DSSCktobj.dssText.command='open ' + Swobj +' term=1'       #switching the line open
           else:
               DSSCktobj.dssText.command='close ' + Swobj +' term=1'      #switching the line close
           i=DSSCircuit.SwtControls.Next     
          
    DSSCircuit.Solution.Solve()
    return DSSCktobj

    
def get_reward(observ_dict):
    #Input: A dictionary describing the state of the network
    #Output: reward    
    
    reward= -observ_dict['loss']
    return reward

         
    
    
    



