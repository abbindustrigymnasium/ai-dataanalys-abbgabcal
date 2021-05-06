from TFEnv import TetrisEnv
from tf_agents.environments import utils


env = TetrisEnv()

utils.validate_py_environment(env, episodes=5)
