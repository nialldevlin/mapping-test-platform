cmake_minimum_required(VERSION 2.8.3)
project(image)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs
  image_transport
)

catkin_package(
  CATKIN_DEPENDS
  rospy
  std_msgs
  geometry_msgs
  image_transport
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(image src/image_node.cpp)
add_dependencies(image 
  ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})