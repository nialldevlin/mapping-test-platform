cmake_minimum_required(VERSION 2.8.3)
project(goliath_config)

find_package(catkin REQUIRED COMPONENTS rospy roscpp std_msgs geometry_msgs)

catkin_package(
  CATKIN_DEPENDS rospy roscpp geometry_msgs std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
