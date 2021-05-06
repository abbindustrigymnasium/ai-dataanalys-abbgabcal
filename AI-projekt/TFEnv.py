from tetris import Tetris

import abc
import tensorflow as tf
import numpy as np

from tf_agents.environments import py_environment
from tf_agents.environments import tf_environment
from tf_agents.environments import tf_py_environment
from tf_agents.environments import utils
from tf_agents.specs import array_spec
from tf_agents.environments import wrappers
from tf_agents.environments import suite_gym
from tf_agents.trajectories import time_step as ts

tf.compat.v1.enable_v2_behavior()


ACTIONS = [[-1,-1,0], [-1,-1,1], [0,-1,0], [0,-1,1], [1,-1,0], [1,-1,1], [-1,0,0], [-1,0,1], [0,0,0], [0,0,1], [1,0,0], [1,0,1],[-1,1,0],[-1,1,1], [0,1,0],[0,1,1], [1,1,0],[1,1,1]]

class TetrisEnv(py_environment.PyEnvironment):
    def __init__(self, start_level = 18):
        self.start_level = start_level
        self.t = Tetris(start_level=self.start_level)
        self.prev_score = 0

        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=0, maximum=18, name='action')
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(26, 10), dtype=np.int8, minimum=0, maximum=1, name='observation'
        )
        # self._state = np.zeros(shape=(26, 10), dtype = np.bool)
        self.observation = np.zeros(shape=(26,10), dtype=np.int8)
        self._episode_ended = False

    def action_spec(self):
        return self._action_spec
    
    def observation_spec(self):
        return self._observation_spec

    def _step(self, action):
        self._episode_ended = False
        reward = 0
                
        passed_action = ACTIONS[action - 1]

        board, next_piece, level, lines_cleared, score, running = self.t.gameloop(passed_action)
        if running:
            reward = score - self.prev_score
        elif self.t.points >= 1500000:
            reward = score - self.prev_score
            self._episode_ended= True
        else:
            self._episode_ended = True
            reward = -20000


        next_piece_temp = np.zeros(shape=(4,10), dtype=np.int8)
        next_piece_temp[0:len(next_piece), 0:len(next_piece)] = next_piece

        self.observation = np.concatenate([board, next_piece_temp])

        if self._episode_ended:
            return ts.termination(self.observation, reward)
        else:
            return ts.transition(self.observation, reward=0.0, discount=1.0)


    def _reset(self):
        self.t = Tetris(start_level=self.start_level)
        self.prev_score = 0

        return ts.restart(np.zeros(shape=(26,10), dtype=np.int8))


    
    def render(self):
        return self.observation