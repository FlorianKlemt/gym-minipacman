import gym
from envs.minipacman_env import MiniPacman
import numpy as np

mini_pacman = MiniPacman()
mini_pacman.start()
for i in range(0,1000):
    mini_pacman.step(mini_pacman.action_space.sample())
    if i%10==0:
        mini_pacman.render('human')

mini_pacman.close()