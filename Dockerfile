#FROM ros:iron
#ARG ROS_DISTRO=iron
#WORKDIR /workspace
#
#SHELL [ "/bin/bash", "-c" ]
#
## Copy the contents of the current directory (assuming Practice02 is in the context)
#COPY . /workspace
#
#RUN rm /etc/ros/rosdep/sources.list.d/20-default.list
#RUN rosdep init && rosdep update
#
## Check if src exists before running rosdep install
#RUN if [ -d "./Practice02/src" ]; then \
#    rosdep install -y --from-path ./Practice02/src --rosdistro=${ROS_DISTRO}; \
#    else echo "src directory not found"; exit 1; \
#    fi
#
#RUN source /opt/ros/${ROS_DISTRO}/setup.bash && colcon buid

FROM ros:iron
ARG ROS_DISTRO=iron
WORKDIR workspace

SHELL [ "/bin/bash", "-c" ]

COPY . .

RUN rm /etc/ros/rosdep/sources.list.d/20-default.list
RUN rm -rf log build install/
RUN rosdep init && rosdep update
RUN rosdep install -y --from-path ./Practice02/src --rosdistro=${ROS_DISTRO}
RUN source /opt/ros/${ROS_DISTRO}/setup.bash && colcon build