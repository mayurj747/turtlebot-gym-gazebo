# turtlebot-gym-gazebo
Training a Turtlebot to move around in circles using ROS + Gazebo and OpenAI Gym.

## Summary
Main script to check out:
* `turtlebot_circle_dqn_clean.ipynb` 

   IPython Notebook without output displayed.
   
   Has the main script for training a DQN for making a Turtlebot go in a circle.
* `turtlebot_circle_dqn_with_results.ipynb` 
   
   IPython Notebook with output displayed
   
 * `test_drive_turtlebot.py`
 
    Script for a quick demo of what the DQN has learned. To run this script, first source the environments as described in "Installation" and then:
    
    `python test_drive turtlebot.py turtlebot_dqn_2`
    
    turtlebot_dqn_2 loads weights of the DQN trained for "Exploration without Directed Bias" (refer report) . Replace with turtlebot_dqn_1 for "Exploration with Directed Bias".
    
    Weight files are located `./models`.
    
   

## Installation 
Requirements
* have [Docker installed](https://docs.docker.com/install/linux/docker-ce/ubuntu/ "Title").
* install nvidia-docker2 (`sudo apt-get install nvidia-docker2`)


Copy run_demo.bash somewhere, make sure it is executable.

`bash run_demo.bash`

You're now inside the container. 
