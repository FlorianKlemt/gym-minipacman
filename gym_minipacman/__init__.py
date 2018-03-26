from gym.envs.registration import register

register(
    id='MiniPacman-v0',
    entry_point='gym_minipacman.envs:MiniPacman',
)