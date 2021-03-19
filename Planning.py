# Uniform distribution plan
def uniformRandomDistribution(adjacent_states):
    import numpy as np
    return np.random.randint(0, len(adjacent_states))