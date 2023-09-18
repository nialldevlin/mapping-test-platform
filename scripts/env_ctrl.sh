_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
shell=$(echo $SHELL | cut -d'/' -f 4)
source ${_dir}/builder.sh
source /opt/ros/noetic/setup.$shell
source ${_dir}/../catkin_ws/devel/setup.$shell

export ROS_MASTER_URI="http://$(getip goliath):11311"

alias view_image="rosrun image_view image_view image:=/gray_image _image_transport:=theora"