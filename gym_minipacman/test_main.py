import gym
from envs.minipacman_env import RegularMiniPacman, AvoidMiniPacman, HuntMiniPacman, AmbushMiniPacman, RushMiniPacman
import numpy as np

mini_pacman = AvoidMiniPacman()
mini_pacman.start()
for i in range(0,1000):
    a = mini_pacman.step(mini_pacman.action_space.sample())
    print(a)
    if i%10==0:
        mini_pacman.render('human')

mini_pacman.close()