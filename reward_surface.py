import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from action_heatmap import create_grid, generate_heatmap
import gym
import gym_gazebo

def calculate_reward(state):
    reward_cap_high = 2
    reward_cap_low = 0.3
    r_true = 3
    x, y = state
    r_curr = x**2 + y**2
    error = abs(r_true - np.sqrt(r_curr))
    reward = 1 / error
    if reward > reward_cap_high:
        reward = reward_cap_high
    elif reward < reward_cap_low:
        reward = 0
    return reward

def main(env):

    state_samples = create_grid(env)
    rewards = np.asarray([calculate_reward(state_samples[i]) for i in range(state_samples.shape[0])])
    data = np.array([state_samples[:, 0], state_samples[:, 1], rewards]).T

    df = pd.DataFrame.from_dict(data)
    df.columns = ['X', 'Y', 'Reward']
    pivotted= df.pivot('Y','X','Reward')
    sns.set()
    ax = sns.heatmap(pivotted, vmin=0)#, xticklabels=100, yticklabels=100)
    ax.invert_yaxis()
    plt.show()
    return ax

if __name__ == '__main__':
    env = gym.make('GazeboEmptyTurtlebotLidarNn-v0')
    fig = main(env)
