from DQN import Agent
import numpy as np
from environment import TetrisEnv
import tensorflow as tf

if __name__ == '__main__':
    tf.compat.v1.disable_eager_execution()
    env = TetrisEnv()
    n_actions = 1
    for space in env.action_space.spaces:
        n_actions *= space.n
    lr = 0.001
    n_games = 500
    agent = Agent(gamma=0.99, epsilon=1.0, lr=lr, input_dims=env.observation_space.shape[0], n_actions=n_actions, mem_size=1_000_000, batch_size=64, epsilon_end=0.01)
    scores = []
    eps_history = []

    for i in range(n_games):
        done = False
        score = 0
        observation = env.reset()
        while not done:
            action = agent.choose_action(observation)
            observation_, reward, done = env.step(action)
            score += reward
            agent.store_transition(observation, action, reward, observation_, done)
            observation = observation_
            agent.learn()
        eps_history.append(agent.epsilon)
        scores.append(score)

        avg_score = np.mean(scores[-100:])
        print("Episdode: ", i, "score: %.2f" % score, "average_score %.2f" % avg_score, "epsilon %.2f" % agent.epsilon)