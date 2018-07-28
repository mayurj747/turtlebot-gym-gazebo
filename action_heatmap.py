import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

import gym
import gym_gazebo

from keras.models import load_model

def create_grid(env):
    xmin, xmax, ymin, ymax = env.env.get_env_constraints(flag='state_space')
    X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    positions = np.vstack([X.ravel(), Y.ravel()]).T
    return np.around(positions, 2)

def generate_heatmap(data):
    """
    This function generates a heatmap for an N x 3 array with col 0, 1 being
    locations on the heatmap and col 3 being the scalar value
    """

    df = pd.DataFrame.from_dict(data)
    df.columns = ['X', 'Y', 'Angular Velocity']
    pivotted= df.pivot('Y','X','Angular Velocity')
    sns.set()
    ax = sns.heatmap(pivotted)#, xticklabels=100, yticklabels=100)
    ax.invert_yaxis()
    plt.show()
    return ax

def main(env, model):

    """
    This script is designed to take in the current state of a network,
    create a grid overlaid on the 2D statespace in question, extract the actions
    (and correspnding actuator values) and produce a heatmap
    """

    state_samples = create_grid(env)
    qvalues = model.predict(state_samples)
    action = np.argmax(qvalues, axis=1)
    ang_vel = env.env.env.calculate_ang_vel(action)
    data = np.array([state_samples[:, 0], state_samples[:, 1], ang_vel]).T
    ax = generate_heatmap(data)
    return ax

if __name__ == '__main__':
    env = gym.make('GazeboEmptyTurtlebotLidarNn-v0')
    trainedDQN = load_model('./models/turtlebot_dqn_test_1.h5')
    fig = main(env, trainedDQN)
