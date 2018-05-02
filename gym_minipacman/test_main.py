import gym
import gym_minipacman
from envs.minipacman_env import RegularMiniPacman, AvoidMiniPacman, HuntMiniPacman, AmbushMiniPacman, RushMiniPacman
import numpy as np
import time


def env_messure_random_sample(env):
    start = time.time()
    for i in range(0, 1000):
        a = env.step(env.action_space.sample())
        # print(a)
        # if i%10==0:
        #    mini_pacman.render('human')
    end = time.time()
    print("time for 1000 steps", end - start)

print("\nRegular MiniPacman")
start = time.time()
mini_pacman = RegularMiniPacman()
mini_pacman.start()
end = time.time()
print("init", end - start)

env_messure_random_sample(mini_pacman)

mini_pacman.close()


print("\nPongDeterministic-v4")
start = time.time()
pong = gym.make('PongDeterministic-v4')
pong.reset()
end = time.time()
print("init", end - start)

env_messure_random_sample(pong)

pong.close()