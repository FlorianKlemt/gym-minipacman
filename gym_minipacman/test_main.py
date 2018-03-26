import gym
from envs.minipacman_env import MiniPacman
import numpy as np

mini_pacman = MiniPacman()
mini_pacman.start()
for i in range(0,1000):
    mini_pacman.step(np.random.random_integers(0,4))
    mini_pacman.render('human')

mini_pacman.close()