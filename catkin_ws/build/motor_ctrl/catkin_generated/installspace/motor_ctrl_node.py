#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO

# GPIO pins for motor control
ENA = 13  # Enable motor A
IN1 = 19  # Motor A input 1
IN2 = 26  # Motor A input 2
ENB = 12  # Enable motor B
IN3 = 16  # Motor B input 1
IN4 = 20  # Motor B input 2

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Initialize PWM for motor speed control
pwm_motor_a = GPIO.PWM(ENA, 100)  # 100 Hz frequency
pwm_motor_b = GPIO.PWM(ENB, 100)
pwm_motor_a.start(0)  # Start with 0% duty cycle
pwm_motor_b.start(0)

def cmd_vel_callback(msg):
    # Extract linear and angular velocities
    linear_vel = msg.linear.x
    angular_vel = msg.angular.z

    # Calculate motor speeds based on velocities
    left_speed = linear_vel - angular_vel
    right_speed = linear_vel + angular_vel

    # Limit speeds to an acceptable range
    left_speed = max(min(left_speed, 1.0), -1.0)
    right_speed = max(min(right_speed, 1.0), -1.0)

    # Convert speeds to PWM duty cycles (0 to 100)
    pwm_motor_a.ChangeDutyCycle(abs(left_speed) * 100)
    pwm_motor_b.ChangeDutyCycle(abs(right_speed) * 100)

    # Set motor directions based on speeds
    GPIO.output(IN1, left_speed > 0)
    GPIO.output(IN2, left_speed < 0)
    GPIO.output(IN3, right_speed > 0)
    GPIO.output(IN4, right_speed < 0)

def motor_control_node():
    rospy.init_node('motor_control_node', anonymous=True)
    rospy.Subscriber('cmd_vel', Twist, cmd_vel_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        motor_control_node()
    except rospy.ROSInterruptException:
        pass
    finally:
        # Stop PWM and cleanup GPIO on node shutdown
        pwm_motor_a.stop()
        pwm_motor_b.stop()
        GPIO.cleanup()
