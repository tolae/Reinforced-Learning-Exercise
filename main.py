from Gridworld import Gridworld
from Agent import Agent
import numpy as np

# MAPE-K Imports
import Monitor
import Analyze
import Planning
import Execution
from Knowledge import Knowledge

global agent
global knowledge

def run():
        # Returns the current state of the agent
        current_state = Monitor.monitor(None, agent)
        # See what moves are available from the current positions
        adj_states = Analyze.analyze(current_state)
        # Get the next action
        desired_action = Planning.uniformRandomDistribution(adj_states)
        # Apply Environmental uncertainty
        actual_action = knowledge.action_func(desired_action)
        # Execute onto the environment
        next_state = Execution.execute(adj_states + [current_state], actual_action)

        agent.update(next_state, knowledge.state_value_dict[next_state])

if __name__ == "__main__":
    world = Gridworld(True)

    knowledge = Knowledge(world, True)

    total_accumulated_rewards = []
    for _ in range(10000):
        agent = Agent()
        agent.current_state = world.grid[0][0]
        while agent.current_state != knowledge.goal:
            run()

        # print("End in steps: " + str(agent.steps))
        # print("Total rewards: " + str(agent.accumulated_rewards))
        total_accumulated_rewards.append(agent.accumulated_rewards)

    print("Mean: " + str(np.mean(total_accumulated_rewards)))
    print("Std Dev.: " +  str(np.std(total_accumulated_rewards)))
    print("Max: " + str(np.max(total_accumulated_rewards)))
    print("Min: " + str(np.min(total_accumulated_rewards)))
