from tetris import Tetris
from gym import spaces
import numpy as np

ACTIONS = [[-1,-1,0], [-1,-1,1], [0,-1,0], [0,-1,1], [1,-1,0], [1,-1,1], [-1,0,0], [-1,0,1], [0,0,0], [0,0,1], [1,0,0], [1,0,1],[-1,1,0],[-1,1,1], [0,1,0],[0,1,1], [1,1,0],[1,1,1]]

class TetrisEnv():
    def __init__(self, start_level = 18):
        self.start_level = start_level
        self.t = Tetris(start_level=self.start_level)
        self.prev_score = 0
        self.observation_space = spaces.Box(low=0, high=1, shape=(26,10), dtype=np.int8)
        #self.action_space = [[-1,-1,0], [-1,-1,1], [0,-1,0], [0,-1,1], [1,-1,0], [1,-1,1], [-1,0,0], [-1,0,1], [0,0,0], [0,0,1], [1,0,0], [1,0,1],[-1,1,0],[-1,1,1], [0,1,0],[0,1,1], [1,1,0],[1,1,1]]
        # self.action_space = spaces.Tuple((spaces.Discrete(3), spaces.Discrete(3), spaces.Discrete(2)))
        self.action_space = spaces.Discrete(18)

    def step(self, action):
        '''
        step() let the AI play one frame of the game. 
        action [0,0,0]
        '''
        done = False
        reward = 0
                
        passed_action = ACTIONS[action - 1]

        board, next_piece, level, lines_cleared, score, running = self.t.gameloop(passed_action)
        if running:
            reward = score - self.prev_score
        else:
            done = True
            reward = -20000


        next_piece_temp = np.zeros(shape=(4,10), dtype=np.int8)
        next_piece_temp[0:len(next_piece), 0:len(next_piece)] = next_piece

        observation = np.concatenate([board, next_piece_temp])


        return observation, reward, done 

    def reset(self):
        self.t = Tetris(start_level=self.start_level)
        self.prev_score = 0

        return np.zeros(shape=(26,10), dtype=np.int8), False


    
    def render(self):
        return 