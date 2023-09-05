#include <ros/ros.h>
#include <image_transport/image_transport.h>

void imageCallback(const sensor_msgs::Image::ConstPtr& msg)
{
  pub.publish(msg);
}

int main(int arc, char** argv)
{
  ros::NodeHandle nh;
  image_transport::ImageTransport it(nh);
  image_transport::Subscriber sub = it.subscribe("/camera/color/image_raw", 1, imageCallback);
  image_transport::Publisher pub = it.advertise("/gray_image", 1); 
}
