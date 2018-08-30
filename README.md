# turtlebot-gym-gazebo
Training a Turtlebot to move around in circles using ROS + Gazebo and OpenAI Gym.

[Report.](report-turtlebot-circles.pdf)


## Installation 
Requirements:
* have [Docker installed](https://docs.docker.com/install/linux/docker-ce/ubuntu/ "Title").
* install nvidia-docker2 (`sudo apt-get install nvidia-docker2`)


Copy run_demo.bash somewhere, make sure it is executable (`chmod +x run_demo.bash`).

`bash run_demo.bash`

You're now inside the container.

Navigate to `~/gym-gazebo/gym_gazebo/envs/installation`, then execute the following:
* `bash setup_kinetic.bash` (might take a few minutes to finish compiling)
* `bash turtlebot_nn_setup.bash`

You should now be ready to execute any script! 

To bring up Gazebo and visualize the robot, in a separate (host) terminal, run:

* `docker exec -it --env DISPLAY --env QT_X11_NO_MITSHM=1 --privileged CONTAINER_ID bash`

   CONTAINER_ID can be obtained by running `docker ps`.
* After logging into the container, run `gzclient`.

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
    
    turtlebot_dqn_2 loads weights of the DQN trained for "Exploration without Directed Bias" (refer report). Replace with turtlebot_dqn_1 for "Exploration with Directed Bias". Run `gzclient` in a separate terminal to view the robot moving in circles.
    
 Weight files are located `./models`.
 
 To launch jupyter-notebook hosted inside the container on the host machine's browser, after the container has been launched using `run_demo.bash`:
 
`jupyter notebook --ip 0.0.0.0 --no-browser --allow-root` 
