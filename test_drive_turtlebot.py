import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import sys
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # comment this and the following line to use GPUs (if available)
os.environ["CUDA_VISIBLE_DEVICES"] = ""

# gym stuff
import gym
import gym_gazebo

# keras stuff
from keras.models import load_model


def update_line(hl, state):
    hl.set_xdata(np.append(hl.get_xdata(), state[0, 0]))
    hl.set_ydata(np.append(hl.get_ydata(), state[0, 1]))
    fig.canvas.draw()


model_name = sys.argv[1]
trainedDQN = load_model('./models/' + str(model_name) + '.h5')

MAX_PATH_LENGTH = 5000
env = gym.make('GazeboEmptyTurtlebotLidarNn-v0')
env._max_episode_steps = MAX_PATH_LENGTH

# init plotting variables for tracing robot trajectory
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
hl, = ax.plot([], [], 'k.', markersize=1)

xmin, xmax, ymin, ymax = env.env.get_env_constraints(flag='state_space')
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.xlabel('X')
plt.ylabel('Y')

state = env.reset()  # initialize env, get state
state = np.reshape(state, [1, state.size])

for episode in range(10):
    print("Now running episode ", episode, " ...")

    while True:
        # Plot new position
        update_line(hl, state)

        # Get action from Q-network
        qvalue = trainedDQN.predict(state)[0]
        action = np.argmax(qvalue)

        # Take action, get new state and reward
        next_state, reward, done, _ = env.step(action)

        state = np.reshape(next_state, [1, state.size])
        if done and episode == 9:
            state = env.env.soft_reset()
            state = np.reshape(state, [1, state.size])
            fig.savefig('turtlebot_trained_trajectory.png')
            break
