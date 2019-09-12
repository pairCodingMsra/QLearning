
class Bot(object):

    def __init__(self):
        self.score = 0
        self.rank = 0
        self.action_history = []
        pass

    def update(self, state, action, reward):
        self.score += reward
        pass

    def get_action(self, state):
        pass

    def show_score(self):
        print(self.score)

    def show_rank(self):
        print(self.rank)

    def show_action_history(self):
        print(self.action_history)
