from gym.envs.registration import register

register(id='openDSS13-v0', entry_point='gym_openDSS.envs.SmallEnv:openDSSenv13')


register(id='openDSS34-v0', entry_point='gym_openDSS.envs.MediumEnv:openDSSenv34')


register(id='openDSS123-v0', entry_point='gym_openDSS.envs.LargeEnv:openDSSenv123')