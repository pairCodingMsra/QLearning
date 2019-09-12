import Bot
import numpy as np


class Bot_QL(Bot):

    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        super(Bot_QL, self).__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = np.random.random((99, 99))

    def update(self, state, action, reward, next_state):
        self.q_table[state, action] = (1 - self.alpha) * self.q_table[state, action] + \
                                      self.alpha * (reward + self.gamma * np.max(self.q_table[next_state]))

    def get_action(self, state):
        if np.random.rand() < self.epsilon:
            action = np.random.choice(range(1, 100, 1))
        else:
            action = np.argmax(self.q_table[state])
        return action
