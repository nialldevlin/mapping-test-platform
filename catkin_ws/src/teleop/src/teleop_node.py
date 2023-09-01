#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

def joy_callback(msg):
    # Create a Twist message to hold the command velocity
    cmd_vel = Twist()

    # Define the axes and buttons from the Joy message
    left_vel = msg.axes[left_axis]
    right_vel = msg.axes[right_axis]

    # Set the linear and angular velocities in the Twist message
    cmd_vel.linear.x = left_vel
    cmd_vel.linear.y = right_vel

    # Publish the Twist message to the cmd_vel topic
    cmd_vel_pub.publish(cmd_vel)

if __name__ == '__main__':
    rospy.init_node('joy_to_cmd_vel_node')
    
    joy_topic = rospy.get_param('teleop/joy_topic', 'joy')
    cmd_vel_topic = rospy.get_param('teleop/cmd_vel_topic', 'cmd_vel')
    left_axis = rospy.get_param('teleop/left_axis', 0)
    right_axis = rospy.get_param('teleop/right_axis', 1)

    rospy.Subscriber(joy_topic, Joy, joy_callback)
    cmd_vel_pub = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
   
    rospy.spin()
