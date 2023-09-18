_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source ${_dir}/builder.sh

export ROS_MASTER_URI="http://$(getip goliath):11311"

alias view_image="rosrun image_view image_view image:=/gray_image _image_transport:=theora"