from gym.envs.registration import register

register(
    id='RegularMiniPacmanNoFrameskip-v0',
    entry_point='gym_minipacman.envs:RegularMiniPacman',
)

register(
    id='AvoidMiniPacmanNoFrameskip-v0',
    entry_point='gym_minipacman.envs:AvoidMiniPacman',
)

register(
    id='HuntMiniPacmanNoFrameskip-v0',
    entry_point='gym_minipacman.envs:HuntMiniPacman',
)

register(
    id='AmbushMiniPacmanNoFrameskip-v0',
    entry_point='gym_minipacman.envs:AmbushMiniPacman',
)

register(
    id='RushMiniPacmanNoFrameskip-v0',
    entry_point='gym_minipacman.envs:RushMiniPacman',
)