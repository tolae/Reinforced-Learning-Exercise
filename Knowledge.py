import numpy as np

class Knowledge:
    def __init__(self, world):
        # Save a copy of the grid
        self.world = world
        # Set known probabilities from environment dynamics
        self._probabilities = [0.8, 0.05, 0.05, 0.1]
        # Create knowledge base state values and rewards
        self.state_value_dict = {}
        # Initialize state values to 0
        for row in world.grid:
            for cell in row:
                self.state_value_dict[cell] = 0
        # Assign goal state
        self.goal = world.grid[4][4]
        self.water_tile = world.grid[4][2]
        # Update terminal state values
        self.state_value_dict[self.goal] = 10
        self.state_value_dict[self.water_tile] = -10
    
    def action_func(self, desired_action):
        action_list = [desired_action] + self._get_turns(desired_action) + [4] # 4 is stay in spot
        return np.random.choice(action_list, p=self._probabilities)

    def transition_func(self, curr_state, desired_action):
        adj_states = curr_state.get_adjacent_states() + [curr_state]
        return 0.8 * self.state_value_dict[adj_states[desired_action]] + \
            0.05 * self.state_value_dict[adj_states[self._get_p_90(desired_action)]] + \
            0.05 * self.state_value_dict[adj_states[self._get_m_90(desired_action)]] + \
            0.1 * self.state_value_dict[adj_states[4]]

    def reward_func(self, next_state):
        if next_state == self.water_tile:
            return self.state_value_dict[self.water_tile]
        elif next_state == self.goal:
            return self.state_value_dict[self.goal]
        return 0

    def _get_turns(self, desired_action):
        return [self._get_p_90(desired_action), self._get_m_90(desired_action)]

    def _get_p_90(self, desired_action):
        return (desired_action - 1) % 4
    
    def _get_m_90(self, desired_action):
        return (desired_action + 1) % 4
