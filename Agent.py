class Agent:
    def __init__(self):
        self.current_state = None
        self.steps = 0
        self.accumulated_rewards = 0

    def update(self, next_state, rewards):
        self.current_state = next_state
        self.steps += 1
        self.accumulated_rewards += rewards
