#!/usr/bin/python3
# Josue Becerra Rico
# Intelligent Systems and Robotics

# This script reads the speed from the speed topic  
# and display it in the terminal.

# Import Libraries  
import rospy
from std_msgs.msg import Float64

def callback(data):
    '''This function prints the speed of the robot'''
    print("Speed: " + str(data.data) + " m/s")

def create_subscriber():
    rospy.init_node("speed_sub_node")
    pub = rospy.Subscriber("speed", Float64, callback)

if __name__=='__main__': # init the nodes
    create_subscriber()
    rospy.spin() # prevent script from closing
