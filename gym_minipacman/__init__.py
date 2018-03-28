from gym.envs.registration import register

register(
    id='RegularMiniPacmanNoFrameskip-v0',
    entry_point='gym_minipacman.envs:RegularMiniPacman',
)

register(
    id='AvoidMiniPacman-v0',
    entry_point='gym_minipacman.envs:AvoidMiniPacman',
)

register(
    id='HuntMiniPacman-v0',
    entry_point='gym_minipacman.envs:HuntMiniPacman',
)

register(
    id='AmbushMiniPacman-v0',
    entry_point='gym_minipacman.envs:AmbushMiniPacman',
)

register(
    id='RushMiniPacman-v0',
    entry_point='gym_minipacman.envs:RushMiniPacman',
)