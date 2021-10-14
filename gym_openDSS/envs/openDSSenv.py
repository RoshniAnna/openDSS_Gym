import gym
import win32com.client
from gym import spaces
import numpy as np
import logging

from DSS_Initialize import * 
from DSS_CircuitSetup import *


from gym.utils import seeding

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.WARNING)

class openDSSenv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        
        print("initializing 13-bus env with sectionalizing and tie switches")
        self.DSSCktObj,self.G_init=initialize() # the DSSCircuit is set up and initialized
        # Set up action and observation space variables
        n_actions=len(sectional_swt)+len(tie_swt) # the switching actions 
        self.action_space = spaces.MultiBinary(n_actions)
        self.observation_space=spaces.Dict({"loss":spaces.Box(low=0,high=2,shape=(1,)),
            "NodeFeat(BusVoltage)":spaces.Box(low=0, high=2, shape=(len(G_init.nodes()),3)),
            "EdgeFeat(branchflow)":spaces.Box(low=0, high=2,shape=(len(G_init.edges()),)),
            "Adjacency":spaces.Box(low=0, high=1,shape=(len(G_init.nodes()),len(G_init.nodes())))
            })

        print('Env initialized')



    def step(self, action):
        # Getting observation before action is executed
        observation = get_state(self.DSSCktobj) #function to get state of the network
        
        # Executing the switching action
        self.DSSCktobj=take_action(self.DSSCktobj,action) #function to implement the action
        
        self.DSSCktobj.dssSolution.Solve()  # Solve Circuit
        
        #Getting observation after action is taken
        obs_post_action = get_state(self.DSSCktobj)
        reward = get_reward(obs_post_action) #function to calculate reward
        done = True
        info = {}
        logging.info('Step success')
        return observation, reward, done, info


    def reset(self):
        logging.info('resetting environment...')
        self.DSSCktObj,base_loops=initialize()
        # Get state observations from initial default load configuration for now
        # We will implememnt load variation in reset
        self.DSSCktobj.dssSolution.Solve()  # Solve Circuit
        logging.info("reset complete\n")
        obs = get_state(self.DSSCktobj)
        return obs

    def render(self, mode='human', close=False):
        pass
