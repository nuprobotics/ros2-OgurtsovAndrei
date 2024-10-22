#!/bin/bash

echo "Working in $(pwd)"

# Stop and remove any existing container named ros2-iron-main
docker stop ros2-iron-main
docker rm ros2-iron-main

# Run the container in detached mode (-d), so it runs in the background
docker build -t my_ros2_image .
#docker run --name ros2-iron-main -it my_ros2_image bash -c "source /opt/ros/iron/setup.bash && source /workspace/install/setup.bash && exec bash"
docker run --name ros2-iron-main -it my_ros2_image bash -c "source /opt/ros/iron/setup.bash && source /workspace/install/setup.bash && ros2 launch task02 task02.launch  && exec bash"

# ros2 launch task02 task02.launch