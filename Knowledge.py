import numpy as np
import sys

class Knowledge:
    def __init__(self, world, debug=False):
        # Save a copy of the grid
        self.world = world
        # Set known probabilities from environment dynamics
        self._probabilities = [0.8, 0.05, 0.05, 0.1]
        self.gamma = 1
        # Create knowledge base state values and rewards
        self.state_value_dict = {None: 0}
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
        # Assign values through state-value valuation via Bellman's Equation
        err = self.state_value_dict[self.goal]
        while err > sys.float_info.epsilon:
            for row in world.grid:
                for cell in [c for c in row if c is not None]:
                    if cell == self.goal or cell == self.water_tile:
                        continue
                    val = self.reward_func(cell) + self.gamma * np.max([
                        self.transition_func(cell, 0),
                        self.transition_func(cell, 1),
                        self.transition_func(cell, 2),
                        self.transition_func(cell, 3),
                        self.transition_func(cell, 4)
                    ])
                    prev_val = self.state_value_dict[cell]
                    self.state_value_dict[cell] = val
                    err = np.min([err, abs(prev_val - val)])

        if debug:
            self.print_value_grid()

    def action_func(self, desired_action):
        action_list = [desired_action] + self._get_turns(desired_action) + [4] # 4 is stay in spot
        return np.random.choice(action_list, p=self._probabilities)

    def transition_func(self, curr_state, desired_action):
        adj_states = curr_state.get_adjacent_states() + [curr_state]
        return np.dot(self._probabilities, np.transpose([
            self.state_value_dict[adj_states[desired_action]],
            self.state_value_dict[adj_states[self._get_p_90(desired_action)]],
            self.state_value_dict[adj_states[self._get_m_90(desired_action)]],
            self.state_value_dict[adj_states[-1]]
        ]))

    def reward_func(self, next_state):
        if next_state == self.water_tile:
            return self.state_value_dict[self.water_tile]
        elif next_state == self.goal:
            return self.state_value_dict[self.goal]
        return -0.04

    def print_value_grid(self):
        for row in range(5):
            print("")
            for col in range(5):
                cell = self.world.grid[row][col]
                print("{:.2f}".format(self.state_value_dict[cell]), end="\t")
            print("")

    def _get_turns(self, desired_action):
        return [self._get_p_90(desired_action), self._get_m_90(desired_action)]

    def _get_p_90(self, desired_action):
        return (desired_action - 1) % 4

    def _get_m_90(self, desired_action):
        return (desired_action + 1) % 4
