#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>

image_transport::Publisher pub;

void imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
  cv_bridge::CvImagePtr cv_ptr;
  cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::MONO8);
  pub.publish(cv_ptr->toImageMsg());
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "image_node");
  ros::NodeHandle nh;
  image_transport::ImageTransport it(nh);
  image_transport::Subscriber sub = it.subscribe("/usb_cam_node/image_raw", 1, imageCallback);
  pub = it.advertise("/gray_image", 1);
  ros::spin();
}
