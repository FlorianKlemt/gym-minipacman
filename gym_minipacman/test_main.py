import gym
import gym_minipacman
from envs.minipacman_env import RegularMiniPacman, AvoidMiniPacman, HuntMiniPacman, AmbushMiniPacman, RushMiniPacman
import time
from time import sleep

def env_messure_random_sample(env):
    start = time.time()
    time_steps = 5000
    for i in range(0, time_steps):
        image, reward, done, _ = env.step(env.action_space.sample())
        # print(a)
        # if i%10==0:
        #env.render('human')
        #sleep(0.01)
        if done:
            env.reset()
    end = time.time()
    print("time for ", time_steps, " steps", end - start)

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