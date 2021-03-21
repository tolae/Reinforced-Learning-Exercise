# Uniform distribution plan
def uniformRandomDistribution(adjacent_states):
    import numpy as np
    return np.random.randint(0, len(adjacent_states))

def optimalPolicy(adjacent_states, knowledge):
    best_action = 0
    best_state = adjacent_states[best_action]
    for action, state in enumerate(adjacent_states[1:]):
        if knowledge.state_value(state) > knowledge.state_value(best_state):
            best_state = state
            best_action = action
    return best_action
