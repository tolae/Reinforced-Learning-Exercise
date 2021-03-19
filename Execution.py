# Simple execution (doesn't contain environmental dynamics)
def execute(all_possible_states, action):
    next_state = all_possible_states[action]
    return next_state if next_state is not None else all_possible_states[-1]
