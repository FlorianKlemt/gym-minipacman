# Gym MiniPacman

This repository implements a minimal version (19x15 pixels) of the Atari game MsPacman as OpenAI Gym environment.
The smaller size leads to a much easier learning task than the normal MsPacman environment (https://gym.openai.com/envs/MsPacman-v0/) which is played on 210x160 pixels.

The code is taken from https://github.com/vasiloglou/mltrain-nips-2017/blob/master/sebastien_racaniere/I2A%20-%20NIPS%20workshop.ipynb , with small adjustments and integration in gym by me.

In order to install MiniPacman run:

```
git clone https://github.com/FlorianKlemt/gym-minipacman.git
cd gym-minipacman
pip3 install -e .
```

To test if the installation was successful run the following in a python console:
```
import gym
import gym_minipacman
env = gym.make("RegularMiniPacmanNoFrameskip-v0")
env.reset()
env.render()
```

There are the following 5 different gym environments included:
* Regular MiniPacman (RegularMiniPacmanNoFrameskip-v0)
* Avoid MiniPacman (AvoidMiniPacmanNoFrameskip-v0)
* Hunt MiniPacman (HunMiniPacmanNoFrameskip-v0)
* Ambush MiniPacman (AmbushMiniPacmanNoFrameskip-v0)
* Rush MiniPacman (RushMiniPacmanNoFrameskip-v0)

Each environment has different rewards and conditions to go to the next level, as shown in the following table:


| Environment | Regular | Avoid | Hunt | Ambush | Rush |
| :----------- | :-----------: | :-----------: | :-----------------: | :-----------------: | :----------: |
| Step Reward       | 0 | 0.1 | 0 | 0 | 0 |
| Food Reward       | 1 | -0.1 | 0 | -0.1 | -0.1 |
| Power Pill Reward | 2 | -5 | 1 | 0 | -10 |
| Kill Ghost Reward | 5 | -10 | 10 | 10 | 0 |
| Death Reward      | 0 | -20 | -20 | -20 | 0 |
| Next level if all power pills eaten | No | No | No | No | Yes |
| Next level if all ghosts killed | No | No | Yes | Yes | No |
| Next level if all food eaten | Yes | Yes | No | No | No |
| Next level when surviving n timesteps | Never | 128 | 80 | 80 | Never |

If you have any questions or suggestions write me under florian.klemt@tum.de.
